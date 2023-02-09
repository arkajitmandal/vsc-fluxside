import numpy as np
import os, glob
import sys

fold  = sys.argv[1]
itry = 0

files = glob.glob(f"{fold}/fs-*")
 
n     = len(np.loadtxt(f"{files[0]}")[:,0])
col   = len(np.loadtxt(f"{files[0]}")[0,:])

    
dat   = np.zeros((n,col+1)) 

 
for i in range(len(files)):
    fl = np.loadtxt(f"{files[i]}")
    for c in range(col):
        dat[:,c] += fl[:,c] 
     
dat[:,:col] = dat[:,:col]/len(files)


for i in range(len(files)):
    fl = np.loadtxt(f"{files[i]}")
    dat[:,col] += (fl[:,1] - dat[:,1])**2  
dat[:,col] =  ((dat[:,col]/len(files))**0.5)/len(files)**0.5


print (f"{fold}, traj = {len(files)}")
np.savetxt("%s/fs.txt"%(fold),dat)
    


