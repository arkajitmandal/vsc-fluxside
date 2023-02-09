import numpy as np
import sys

from numpy.fft import fft

dat = np.loadtxt("./scans/wc-0.03/fs.txt")[:,:]
ω = np.arange(0,0.3,0.001)/27.2114

I = ω * 0.0 + 0j
t = dat[:,0]
Rt = dat[:,1]


for iω, ωi  in enumerate(ω):
    β = 1052.8 # change according to temperature
    pre  = (ωi * (1- np.exp(-β * ωi)))
    I[iω] = pre * np.sum(  np.exp(- 1j * ωi * t)  * Rt   ) + pre * np.sum(  np.exp(1j * ωi * t) * Rt  )

 

np.savetxt("ir.txt", np.c_[ω, I.real, I.imag])
 
 