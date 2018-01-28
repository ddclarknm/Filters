# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:41:47 2018

@author: ddcla
"""

import numpy as np
import matplotlib.pyplot as pl

R = 10e3
C1 = 3.0e-7
C2 = 1.5e-7

f0 = 50e3

f = np.linspace(0, 1e6, num = 5000)


def Zsallenkey(C1, C2, R, f):
    
    w = 2 * np.pi * f
    
    ZC1 = 1 / (1j * w * C1)
    ZC2 = 1 / (1j * w * C2)
    
    return R + (ZC1 * (R + ZC2)) / (ZC1 + ZC2 + R)


Z = Zsallenkey(C1, C2, R, f)

Zf0 = np.abs(Zsallenkey(C1, C2, R, f0))
print(Zf0)

figno = 0

figno += 1
pl.figure(figno)
pl.clf()


pl.semilogx(f, np.abs(Z))
pl.axvline(f0)
pl.axhline(Zf0)