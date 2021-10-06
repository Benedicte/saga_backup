import LonRead
import numpy as np
import sys 

fileName = sys.argv[1]
molecule = sys.argv[2]
magnetic_dir = sys.argv[3]


restricted = True

if restricted == False:

    K = LonRead.LonRead(fileName + ".out.data",'KinEneInts')
    V = LonRead.LonRead(fileName + ".out.data",'NucAttInts')
    eri = LonRead.LonRead(fileName + ".out.data",'EleRepInts')
    mol_orb_eigs = LonRead.LonRead(fileName + ".out.data",'MolOrbEigs')
    dipole_integrals = LonRead.LonRead(fileName + ".out.data",'DipMomInts')
    mol_orb_vecs = LonRead.LonRead(fileName + ".out.data", 'MolOrbVecs')
 
    K = K["KinEneInts"]
    V = V["NucAttInts"]
    eri = eri["EleRepInts"]
    mo_coef = mol_orb_vecs["MolOrbVecs"]

    dipole_integrals = dipole_integrals["DipMomInts"]
    dipx = dipole_integrals[:,:,0]
    dipy = dipole_integrals[:,:,1]
    dipz = dipole_integrals[:,:,2]
    dipole_integrals = np.zeros((3,dipx.shape[0],dipx.shape[0]),dtype = np.complex128)
    dipole_integrals[0] = dipx
    dipole_integrals[1] = dipy
    dipole_integrals[2] = dipz

if restricted == True:

    K = LonRead.LonRead(fileName + ".out.data",'KinEneIntAO')
    V = LonRead.LonRead(fileName + ".out.data",'NucAttIntAO')
    eri = LonRead.LonRead(fileName + ".out.data",'EleRepIntAO')
    s = LonRead.LonRead(fileName + ".out.data", 'OviIntAO')
    mo_coef = LonRead.LonRead(fileName + ".out.data", 'CMO_0')
    mo_coef_1 = LonRead.LonRead(fileName + ".out.data", 'CMO_1')
    dipole_integrals = LonRead.LonRead(fileName + ".out.data", 'DipMomIntAO')
   
    K = K["KinEneIntAO"]
    V = V["NucAttIntAO"]
    eri = eri["EleRepIntAO"]
    eri =  np.transpose(eri, [0, 2, 1, 3])
    mo_coef = mo_coef["CMO_0"]
    s = s['OviIntAO']
    np.save('s_' + molecule + magnetic_dir, s)

    dipole_integrals = dipole_integrals["DipMomIntAO"]
    dipx = dipole_integrals[:,:,0]
    dipy = dipole_integrals[:,:,1]
    dipz = dipole_integrals[:,:,2]
    dipole_integrals = np.zeros((3,dipx.shape[0],dipx.shape[0]),dtype = np.complex128)
    dipole_integrals[0] = dipx
    dipole_integrals[1] = dipy
    dipole_integrals[2] = dipz


H = K+V

np.save('H_' + molecule + magnetic_dir, H)
np.save('eri_' + molecule + magnetic_dir, eri)
np.save('dipole_integrals_' + molecule + magnetic_dir, dipole_integrals)
np.save('moc_' + molecule + magnetic_dir, mo_coef)
np.save('moc1_' + molecule + magnetic_dir, mo_coef_1)

print("use_lonread ended successfully")
