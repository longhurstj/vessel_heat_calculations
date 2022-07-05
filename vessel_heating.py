# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:04:20 2021

@author: JoshuaL
"""

from sympy.abc import t
from sympy import init_printing, plot, lambdify
from sympy import symbols
from sympy import Function, Derivative, dsolve, oo, Eq, solve
import numpy as np

''' Import Data '''
import pandas as pd
import csv

vessel_data = pd.read_csv (r'C:\Users\longh\OneDrive\_uni\_Final Year Project\XCOS\vessel_data.txt', header = None)
vessel_data.columns = ['time','values']
vessel_data.to_csv (r'C:\Users\longh\OneDrive\_uni\_Final Year Project\XCOS\vessel_data.csv', index=None)
data = list(pd.read_csv (r'C:\Users\longh\OneDrive\_uni\_Final Year Project\XCOS\vessel_data.csv',usecols=(0,1)))

vessel_heating_data = np.loadtxt(r'C:\Users\longh\OneDrive\_uni\_Final Year Project\Data\cycle_heating_numerical.txt')
vessel_empirical_data = np.loadtxt(r'C:\Users\longh\OneDrive\_uni\_Final Year Project\Data\cycle_heating_empirical.txt')

T = Function ('T')
k, T_oo, T_o = symbols ('k, T_oo, T_o', positive=True)

eq1 = Derivative(T(t),t)+k*(T(t)-T_oo)
eq2 = dsolve(eq1,T(t),ics={T(0): T_o})

'''Specific problem'''
"Know that after 1.1 hours temperature is 38.4"
eq3 = eq2.subs({T_o: 136, T_oo: 30})
eq4 = eq3.subs({T(t): 38.4, t: 1.1})
#eq5 = Eq(k,solve(eq4,k)[0])

eq6 = eq3.subs(k, 2.30473398932982)
#plot(eq6.rhs,(t,0,2))

''' Help the solver along'''
"substitute values into equation for k"
eq7 = Eq(k,solve(eq2,k)[0])
eq8 = eq7.subs({T_o: 136, T_oo: 30, T(t): 38.4, t: 1.1})


import numpy as np
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(vessel_heating_data[:,0], vessel_heating_data[:,1], 'b--', label = 'XCOS PID Heating')
plt.plot(vessel_empirical_data[:,0], vessel_empirical_data[:,1], 'g-', label = 'Real Heating Data')
t_s=np.linspace(0,2.5,num=30);
T_s=lambdify(t, eq6.rhs)
#plt.plot(t_s,T_s(t_s),'r.',  label = 'ANSYS data')
#plt.errorbar(t_s,T_s(t_s),'ro', label = 'Analytic')
# Add graph labels
plt.xlabel('Time (Seconds)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid()
plt.title('Vessel Heating Comparison')