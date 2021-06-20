import numpy as np
#import numdifftools
import matplotlib.pyplot as plt

from extract_response_functions import ExtractResponseFunctions


time = np.load("total_time_points.npy")

omega = 0.1
dt = 1e-2

after_pulse = int((2 * np.pi / omega)/ dt)
time_points = time[after_pulse:] - time[after_pulse]
#time_points = time[after_pulse:]


print("After pulse")
print(after_pulse)

print("length og time points")
print(len(time_points))

F = 0.0005 
w = np.array((0.1,))


### Polarization in X direction #####

pos_F_xx = np.load('0.0005dir0.npy')[after_pulse:]
neg_F_xx =  np.load('-0.0005dir0.npy')[after_pulse:]
pos_2F_xx =  np.load('0.001dir0.npy')[after_pulse:]
neg_2F_xx =  np.load('-0.001dir0.npy')[after_pulse:]


### Polarization in Z direction #####

pos_F_zz = np.load('0.0005dir2.npy')[after_pulse:]
neg_F_zz =  np.load('-0.0005dir2.npy')[after_pulse:]
pos_2F_zz =  np.load('0.001dir2.npy')[after_pulse:]
neg_2F_zz =  np.load('-0.001dir2.npy')[after_pulse:]


### Polarization in Y direction #####

pos_F_yy = np.load('0.0005dir1.npy')[after_pulse:]
neg_F_yy =  np.load('-0.0005dir1.npy')[after_pulse:]
pos_2F_yy =  np.load('0.001dir1.npy')[after_pulse:]
neg_2F_yy =  np.load('-0.001dir1.npy')[after_pulse:]


#print("length pos") 
#print(len(pos_F_xz))
#print("length neg")
#print(len(neg_F_xz))

inst = ExtractResponseFunctions(F)

first_order_xx = inst.extract_first_order(F, w, time_points, pos_F_xx, neg_F_xx, pos_2F_xx, neg_2F_xx)
first_order_zz = inst.extract_first_order(F, w, time_points, pos_F_zz, neg_F_zz, pos_2F_zz, neg_2F_zz)
first_order_yy = inst.extract_first_order(F, w, time_points, pos_F_yy, neg_F_yy, pos_2F_yy, neg_2F_yy)


