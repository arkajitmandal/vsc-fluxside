import numpy as np 
import os, sys
 
nfold = int(sys.argv[1]) 
try :
    offset = int(sys.argv[2])
except:
    offset = 0
#os.system("rm -rf traj-*")
os.mkdir("log")
 
np.savetxt('submit.dat', np.arange(offset, offset + nfold))
os.system("condor_submit condor.sub")
 
 