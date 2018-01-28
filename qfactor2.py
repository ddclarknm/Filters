# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:10:06 2018

@author: ddcla
"""

import numpy as np
import matplotlib.pyplot as pl

import importlib
import filterhelpers as fh

importlib.reload(fh)


f0 = 500e3
C = 1e-6
Z0 = 50e3

f = np.logspace(1,6, num=50000)
w = 2 * np.pi * f

L = 1 / (C * (2 * np.pi * f0)**2)

print(L)

Zc = 1 / (1j * w * C)
Zl = 1j * w * L

Zlc = fh.parallel(Zc, Zl)

H = Z0 / (Z0 + Zlc)

figno = 0

figno += 1
pl.figure(figno)
pl.clf()

pl.semilogx(f, np.abs(Zlc))

figno += 1
bodeplot = pl.figure(figno)
bodeplot.clf()

magax = bodeplot.add_subplot(211)
phax = bodeplot.add_subplot(212)

magax.semilogx(f, 20 * np.log10(np.abs(H)))
phax.semilogx(f, np.angle(H))
