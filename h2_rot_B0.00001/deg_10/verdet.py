import numpy as np
#import numdifftools
import matplotlib.pyplot as plt
import scipy.constants as sp

from extract_response_functions import ExtractResponseFunctions

np.printoptions(precision=5)


time = np.load("time_points.npy")
#energy = np.load("energy_cc2.npy")

omega = 0.11391
dt = 1e-2

after_pulse = int((2 * np.pi / omega)/ dt)
time_points = time[after_pulse:] - time[after_pulse]
time_points = time[after_pulse:]

F = 0.001 
w = np.array((omega,))

def calc_constant(omega):
    ''' (omega/2c)(2*piN/4*pi*e0)(e/2me)'''
    constant = omega*0.00764177
    return constant 

### Polarization in magnetic X direction #####

pos_Fx_yz =   np.load('0.001xpol_yz.npy')[after_pulse:]
neg_Fx_yz =  np.load('-0.001xpol_yz.npy')[after_pulse:]
pos_2Fx_yz =  np.load('0.002xpol_yz.npy')[after_pulse:]
neg_2Fx_yz = np.load('-0.002xpol_yz.npy')[after_pulse:]

pos_Fx_zy =   np.load('0.001xpol_zy.npy')[after_pulse:]
neg_Fx_zy =  np.load('-0.001xpol_zy.npy')[after_pulse:]
pos_2Fx_zy =  np.load('0.002xpol_zy.npy')[after_pulse:]
neg_2Fx_zy = np.load('-0.002xpol_zy.npy')[after_pulse:]

### Polarization in magnetic Y direction #####

pos_Fy_xz =   np.load('0.001ypol_xz.npy')[after_pulse:]
neg_Fy_xz =  np.load('-0.001ypol_xz.npy')[after_pulse:]
pos_2Fy_xz =  np.load('0.002ypol_xz.npy')[after_pulse:]
neg_2Fy_xz = np.load('-0.002ypol_xz.npy')[after_pulse:]

pos_Fy_zx =   np.load('0.001ypol_zx.npy')[after_pulse:]
neg_Fy_zx =  np.load('-0.001ypol_zx.npy')[after_pulse:]
pos_2Fy_zx =  np.load('0.002ypol_zx.npy')[after_pulse:]
neg_2Fy_zx = np.load('-0.002ypol_zx.npy')[after_pulse:]

### Polarization in magnetic Z direction #####

pos_Fz_xy =   np.load('0.001zpol_xy.npy')[after_pulse:]
neg_Fz_xy =  np.load('-0.001zpol_xy.npy')[after_pulse:]
pos_2Fz_xy =  np.load('0.002zpol_xy.npy')[after_pulse:]
neg_2Fz_xy = np.load('-0.002zpol_xy.npy')[after_pulse:]

pos_Fz_yx =   np.load('0.001zpol_yx.npy')[after_pulse:]
neg_Fz_yx =  np.load('-0.001zpol_yx.npy')[after_pulse:]
pos_2Fz_yx =  np.load('0.002zpol_yx.npy')[after_pulse:]
neg_2Fz_yx = np.load('-0.002zpol_yx.npy')[after_pulse:]

inst = ExtractResponseFunctions(F)

yz_lx = inst.extract_first_order(F, w, time_points, pos_Fx_yz, neg_Fx_yz, pos_2Fx_yz, neg_2Fx_yz, verbose = False)
zy_lx = inst.extract_first_order(F, w, time_points, pos_Fx_zy, neg_Fx_zy, pos_2Fx_zy, neg_2Fx_zy, verbose = False)

xz_ly = inst.extract_first_order(F, w, time_points, pos_Fy_xz, neg_Fy_xz, pos_2Fy_xz, neg_2Fy_xz, verbose = False)
zx_ly = inst.extract_first_order(F, w, time_points, pos_Fy_zx, neg_Fy_zx, pos_2Fy_zx, neg_2Fy_zx, verbose = False)

xy_lz = inst.extract_first_order(F, w, time_points, pos_Fz_xy, neg_Fz_xy, pos_2Fz_xy, neg_2Fz_xy, verbose = False)
yx_lz = inst.extract_first_order(F, w, time_points, pos_Fz_yx, neg_Fz_yx, pos_2Fz_yx, neg_2Fz_yx, verbose = False)


#print("xy_lz")
print(xy_lz.imag)

#print("yx_lz")
print(yx_lz.imag)

#print("xz_ly")
print(xz_ly.imag)

#print("zx_ly")
print(zx_ly.imag)

#print("yz_lx")
print(yz_lx.imag)

#print("zy_lx")
print(zy_lx.imag)



print("sum")


delta_elec_pol_2 = (xy_lz - yx_lz - xz_ly + zx_ly + yz_lx - zy_lx) 

print(delta_elec_pol_2.imag)


