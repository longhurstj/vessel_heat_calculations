# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:04:20 2021

@author: Josh
"""

import sympy
from sympy.abc import t
from sympy import init_printing, plot, lambdify
from sympy import symbols
from sympy import Function, Derivative, dsolve, oo, Eq, solve

T = Function ('T')
k, T_oo, T_o = symbols ('k, T_oo, T_o', positive=True)

eq1 = Derivative(T(t),t)+k*(T(t)-T_oo)
eq2 = dsolve(eq1,T(t),ics={T(0): T_o})

"Specific problem"
"We know that after 0.0986 hours temperature is 79.14"
eq3 = eq2.subs({T_o: 134, T_oo: 20})
eq4 = eq3.subs({T(t): 79.14, t: 0.0986})
eq5 = Eq(k,solve(eq4,k)[0])

eq6 = eq3.subs(k, 3600/20/(750-25))
plot(eq6.rhs,(t,0,24))

import numpy as np
import matplotlib.pyplot as plt

t_s=np.linspace(0,130,131);
T_s=lambdify(t, eq6.rhs)
plt.plot(t_s,T_s(t_s),'o')