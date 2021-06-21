import numpy as np
import matplotlib.pyplot as plt
from extract_response_functions import ExtractResponseFunctions


time = np.load("time_points.npy")
omega = 0.01
dt = 5e-2

after_pulse = int((2 * np.pi / omega)/ dt)
time_points =  time[after_pulse:]-time[after_pulse]

F = 0.001 
w = np.array((omega,))


### Polarization in X direction #####

pos_F_xx = np.load('0.001dir0_x.npy')[after_pulse:]
pos_F_xy = np.load('0.001dir0_y.npy')[after_pulse:]
pos_F_xz = np.load('0.001dir0_z.npy')[after_pulse:]

neg_F_xx =  np.load('-0.001dir0_x.npy')[after_pulse:]
neg_F_xy =  np.load('-0.001dir0_y.npy')[after_pulse:]
neg_F_xz =  np.load('-0.001dir0_z.npy')[after_pulse:]

pos_2F_xx =  np.load('0.002dir0_x.npy')[after_pulse:]
pos_2F_xy =  np.load('0.002dir0_y.npy')[after_pulse:]
pos_2F_xz =  np.load('0.002dir0_z.npy')[after_pulse:]

neg_2F_xx =  np.load('-0.002dir0_x.npy')[after_pulse:]
neg_2F_xy =  np.load('-0.002dir0_y.npy')[after_pulse:]
neg_2F_xz =  np.load('-0.002dir0_z.npy')[after_pulse:]


### Polarization in Z direction #####

pos_F_zx = np.load('0.001dir2_x.npy')[after_pulse:]
pos_F_zy = np.load('0.001dir2_y.npy')[after_pulse:]
pos_F_zz = np.load('0.001dir2_z.npy')[after_pulse:]

neg_F_zx =  np.load('-0.001dir2_x.npy')[after_pulse:]
neg_F_zy =  np.load('-0.001dir2_y.npy')[after_pulse:]
neg_F_zz =  np.load('-0.001dir2_z.npy')[after_pulse:]

pos_2F_zx =  np.load('0.002dir2_x.npy')[after_pulse:]
pos_2F_zy =  np.load('0.002dir2_y.npy')[after_pulse:]
pos_2F_zz =  np.load('0.002dir2_z.npy')[after_pulse:]

neg_2F_zx =  np.load('-0.002dir2_x.npy')[after_pulse:]
neg_2F_zy =  np.load('-0.002dir2_y.npy')[after_pulse:]
neg_2F_zz =  np.load('-0.002dir2_z.npy')[after_pulse:]


### Polarization in Y direction #####

pos_F_yx = np.load('0.001dir1_x.npy')[after_pulse:]
pos_F_yy = np.load('0.001dir1_y.npy')[after_pulse:]
pos_F_yz = np.load('0.001dir1_z.npy')[after_pulse:]

neg_F_yx =  np.load('-0.001dir1_x.npy')[after_pulse:]
neg_F_yy =  np.load('-0.001dir1_y.npy')[after_pulse:]
neg_F_yz =  np.load('-0.001dir1_z.npy')[after_pulse:]

pos_2F_yx =  np.load('0.002dir1_x.npy')[after_pulse:]
pos_2F_yy =  np.load('0.002dir1_y.npy')[after_pulse:]
pos_2F_yz =  np.load('0.002dir1_z.npy')[after_pulse:]

neg_2F_yx =  np.load('-0.002dir1_x.npy')[after_pulse:]
neg_2F_yy =  np.load('-0.002dir1_y.npy')[after_pulse:]
neg_2F_yz =  np.load('-0.002dir1_z.npy')[after_pulse:]


inst = ExtractResponseFunctions(F)

first_order_xx = inst.extract_first_order(F, w, time_points, pos_F_xx, neg_F_xx, pos_2F_xx, neg_2F_xx)
first_order_xy = inst.extract_first_order(F, w, time_points, pos_F_xy, neg_F_xy, pos_2F_xy, neg_2F_xy)
first_order_xz = inst.extract_first_order(F, w, time_points, pos_F_xz, neg_F_xz, pos_2F_xz, neg_2F_xz)

first_order_yx = inst.extract_first_order(F, w, time_points, pos_F_yx, neg_F_yx, pos_2F_yx, neg_2F_yx)
first_order_yy = inst.extract_first_order(F, w, time_points, pos_F_yy, neg_F_yy, pos_2F_yy, neg_2F_yy)
first_order_yz = inst.extract_first_order(F, w, time_points, pos_F_yz, neg_F_yz, pos_2F_yz, neg_2F_yz)

first_order_zx = inst.extract_first_order(F, w, time_points, pos_F_zx, neg_F_zx, pos_2F_zx, neg_2F_zx)
first_order_zy = inst.extract_first_order(F, w, time_points, pos_F_zy, neg_F_zy, pos_2F_zy, neg_2F_zy)
first_order_zz = inst.extract_first_order(F, w, time_points, pos_F_zz, neg_F_zz, pos_2F_zz, neg_2F_zz)

print("Polarizabilities, real components")

print("x")
print(first_order_xx.real)
print(first_order_xy.real)
print(first_order_xz.real)

print("y")
print(first_order_yx.real)
print(first_order_yy.real)
print(first_order_yz.real)

print("z")
print(first_order_zx.real)
print(first_order_zy.real)
print(first_order_zz.real)



