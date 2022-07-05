# -*- coding: utf-8 -*-
"""
Created on Wed May  5 08:17:12 2021

@author: JoshuaL
"""

import math

# Set Vessel Volume
vol = input("Enter vessel volume: ")
Vol = int(vol)        #litres

vessel_vol = f"For a {Vol}L vessel the length of coil required is"
other = "Please select 22 or 16 litre vessels"

# Set Pump Data
v_p = 2800       #ml/min

# Set Steam Data
V_H = Vol/1000  #m3
rho_H = 1.65    #kg/m3
Cp_H = 2.257    #kj/kg*k
R_fi = 9e-5     #K/W
h_i = 6000      #W/m2*K

# Set Boiler Inlet and Outlet Temp
T_Hi = 134      #°C
T_Ho = 20       #°C

# Set Coolant Data
V_C = v_p/6e7   #m3
rho_C = 1050    #kg/m3
Cp_C = 4.219    #kj/kg*k
R_fo = 2e-4     #K/W
h_o = 1300      #W/m2*K

# Overall Heat Transfer Rate
Q = ((V_H*rho_H)*(Cp_H*1000)*(T_Hi-T_Ho))

# Set Coil Inlet Temp
T_Ci = 20       #°C
T_Co = (T_Ci)+(Q/(V_C*rho_C*(Cp_C*1000)))

# Log Mean Temp
T_lm = ((T_Co-T_Ho)-(T_Hi-T_Ci))/(math.log((T_Co-T_Ho)/(T_Hi-T_Ci)))

# Thermal Resistance
R_tot = (T_lm+273.15)/Q
R_t = ((1/h_i)+R_fi+R_fo+(1/h_o))

# Tube Diameter
D = 6.4         #mm
# Coil Results
A = R_t/R_tot
L = A/(math.pi*(D/1000))
coil_length = f"{round(L, 2)}m"

if Vol > 1:
    print(f"{vessel_vol} {coil_length}")
else:
    print(f"{other}")

