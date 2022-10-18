import numpy as np
import os
import sys
nfold = 300
fold  = sys.argv[1]
itry = 0
while itry<nfold:
    try: 
        n     = len(np.loadtxt(f"{fold}/traj-{itry}/fs.txt")[:,0])
        col   = len(np.loadtxt(f"{fold}/traj-{itry}/fs.txt")[0,:])
        break 
    except:
        itry += 1
    
dat   = np.zeros((n,col)) 

actraj = 0
for i in range(nfold):
    try:
        fl = np.loadtxt(fold+"/traj-%s/fs.txt"%(i))
        for c in range(col):
            dat[:,c] += fl[:,c]
        actraj += 1
    except:
        pass
        #print (f"no {i}")

dat = dat/actraj

print (f"{fold}, traj = {actraj}")
np.savetxt("%s/fs.txt"%(fold),dat)
    


