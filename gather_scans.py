import numpy as np
from glob import glob
import os, sys

prefix = 'wc'

mainfold = sys.argv[1]
os.chdir(mainfold)
folders = glob(f"{prefix}-*")

print (folders)


tEnd = 8 * 41351 # ps 

fsdat = np.zeros((2, len(folders)))

for indx, i  in enumerate(folders):
    try:
        #os.system(f"python avg.py {i}")
        dat = np.loadtxt(f"{i}/fs.txt")[:,-1]

        finTime = np.loadtxt(f"{i}/fs.txt")[-1,0]
        totT = len(dat)
        print (finTime)

        end = int(totT * tEnd/finTime) 
        avgrange = 10
        print (end)
        
        k = dat[-avgrange + end: end]
        
        k = np.sum(k) /len(k)
        wc = i.split("-")[1]
        print (wc)
        fsdat[:,indx] = np.array([wc, k])
    except Exception as e:
        print (e)
        print (f"Not Doing it : {i}")
sorts = np.argsort(fsdat[0,:])

fsdat[0,:] = fsdat[ 0,sorts ]
fsdat[1,:] = fsdat[ 1,sorts ]


print(fsdat[0,sorts ])
np.savetxt(f"fs-{prefix}.txt",fsdat.T)