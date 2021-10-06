import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import tqdm
import os

from quantum_systems import construct_quest_system_rhf
from quantum_systems.time_evolution_operators import DipoleFieldInteraction
from coupled_cluster.rccsd import RCCSD, TDRCCSD
from gauss_integrator import GaussIntegrator
from scipy.integrate import complex_ode

from coupled_cluster.mix import DIIS, AlphaMixer
from adiabatic_laser import AdiabaticLaser

##################       System parameters         ######################

mol = sys.argv[1] 
F_str = float(sys.argv[2])
magnetic_field_direction = sys.argv[3]
polarization_direction = int(sys.argv[4])  

n = 10 
nuclear_repulsion_energy = 0 

h = np.load('H_' + mol + magnetic_field_direction + '.npy')
u = np.load('eri_' + mol + magnetic_field_direction +'.npy')
l = h.shape[0]
nuclear_repulsion_energy = 0
mo_coef = np.load('moc_'+ mol + magnetic_field_direction +'.npy')
dip_int = np.load("dipole_integrals_" + mol + magnetic_field_direction +".npy")
s = np.load("s_" + mol + magnetic_field_direction +".npy")

system = construct_quest_system_rhf(n, l, h, s,u, mo_coef, nuclear_repulsion_energy, dip_int, np=np)

conv_tol = 1e-8
rccsd = RCCSD(system, mixer=AlphaMixer, verbose=False)

t_kwargs = dict(tol=conv_tol, theta=0)
l_kwargs = dict(tol=conv_tol, theta=0)

rccsd.compute_ground_state(t_kwargs=t_kwargs, l_kwargs=l_kwargs)

print("Ground state energy in time independent part")
print("Ground state energy: {0}".format(rccsd.compute_energy()))

#####################     Laser parameters      ########################

omega = 10.11391
t_cycle = 2 * np.pi / omega
switch = 'quadratic'
n_switch = 1
n_after = 5
n_cycle = n_switch + n_after
tfinal = np.floor(n_cycle*t_cycle + 1)

polarization = np.zeros(3)
polarization[polarization_direction] = 1

pulse = AdiabaticLaser(F_str, omega, n_switch=n_switch, switch=switch)
system.set_time_evolution_operator(
    DipoleFieldInteraction(
        pulse,
        polarization_vector=polarization,
    )
)

########################################################################

dt = 1e-2

cc_kwargs = dict(verbose=False)
amps0 = rccsd.get_amplitudes(get_t_0=True)
y0 = amps0.asarray()

print("TDRCCSD initiated")
tdrccsd = TDRCCSD(system)

r = complex_ode(tdrccsd).set_integrator("GaussIntegrator", s=3, eps=1e-8)
r.set_initial_value(y0)

num_steps = int(tfinal / dt)
n_samples = num_steps + 1

# Initialize arrays to hold different "observables".

time_points = np.zeros(n_samples)
energy = np.zeros(n_samples, dtype=np.complex128)
dip_x = np.zeros(n_samples, dtype=np.complex128)
dip_y = np.zeros(n_samples, dtype=np.complex128)
dip_z = np.zeros(n_samples, dtype=np.complex128)

# Set initial values
t, l = amps0

time_points[0] = r.t
energy[0] = tdrccsd.compute_energy(r.t, r.y)
dip_x[0] = tdrccsd.compute_one_body_expectation_value(
    r.t,
    r.y,
    system.dipole_moment[0],
    make_hermitian=False,
)

dip_y[0] = tdrccsd.compute_one_body_expectation_value(
    r.t,
    r.y,
    system.dipole_moment[1],
    make_hermitian=False,
)

dip_z[0] = tdrccsd.compute_one_body_expectation_value(
    r.t,
    r.y,
    system.dipole_moment[2],
    make_hermitian=False,
)

for i in tqdm.tqdm(range(num_steps)):
    r.integrate(r.t + dt)
    if not r.successful():
#        print(f"\n\nWARNING: integrator failed at time step {i+1}\n\n")
        break
    # use amps0 as template
    t, l = amps0.from_array(r.y)
    # save current time in time_points
    time_points[i + 1] = r.t
    energy[i + 1] = tdrccsd.compute_energy(r.t, r.y)
    dip_x[i + 1] = tdrccsd.compute_one_body_expectation_value(
        r.t,
        r.y,
        system.dipole_moment[0],
        make_hermitian=False,
    )

    dip_y[i + 1] = tdrccsd.compute_one_body_expectation_value(
        r.t,
        r.y,
        system.dipole_moment[1],
        make_hermitian=False,
    )
    
    dip_z[i + 1] = tdrccsd.compute_one_body_expectation_value(
        r.t,
        r.y,
        system.dipole_moment[2],
        make_hermitian=False,
    )

arr = ['x','y','z']

if(polarization_direction == 0):
    np.save(str(F_str) + magnetic_field_direction + "pol_y" + arr[polarization_direction] + ".npy",  dip_y)
    np.save(str(F_str) + magnetic_field_direction + "pol_z" + arr[polarization_direction] + ".npy",  dip_z)


if(polarization_direction == 1):
    np.save(str(F_str) + magnetic_field_direction + "pol_x" + arr[polarization_direction] + ".npy",  dip_x)
    np.save(str(F_str) + magnetic_field_direction + "pol_z" + arr[polarization_direction] + ".npy",  dip_z)


if(polarization_direction == 2):
    np.save(str(F_str) + magnetic_field_direction + "pol_x" + arr[polarization_direction] + ".npy",  dip_x)
    np.save(str(F_str) + magnetic_field_direction + "pol_y" + arr[polarization_direction] + ".npy",  dip_y)

np.save("time_points_B0.npy", time_points)
np.save("energy_ccsd_B0.npy", energy)
