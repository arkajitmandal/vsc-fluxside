import numpy as np
from glob import glob
import os, sys

prefix = 'wc'

mainfold = sys.argv[1]
os.chdir(mainfold)
folders = glob(f"{prefix}-*")

print (folders)


tEnd = 8 * 41351 # ps 

fsdat = np.zeros((3, len(folders)))

for indx, i  in enumerate(folders):
    try:
        os.system(f"python ../avg.py {i}")
        dat = np.loadtxt(f"{i}/fs.txt")[:,1]

        finTime = np.loadtxt(f"{i}/fs.txt")[-1,0]
        totT = len(dat)
        print (finTime)
        
        k = dat[-1]
        wc = i.split("-")[1]
        dk = np.loadtxt(f"{i}/fs.txt")[-1,2]
        print (k, wc)
        fsdat[:,indx] = np.array([wc, k, dk])
    except Exception as e:
        print (e)
        print (f"Not Doing it : {i}")
sorts = np.argsort(fsdat[0,:])

fsdat[0,:] = fsdat[ 0,sorts ]
fsdat[1,:] = fsdat[ 1,sorts ]
fsdat[2,:] = fsdat[ 2,sorts ]

print(fsdat[0,sorts ])
np.savetxt(f"fs-{prefix}.txt",fsdat.T)