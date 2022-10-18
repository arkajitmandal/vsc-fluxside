import numpy as np 
import os, sys
 
nfold = int(sys.argv[1]) 
try :
    offset = int(sys.argv[2])
except:
    offset = 0
#os.system("rm -rf traj-*")
for n in np.arange(offset, offset + nfold):

    os.mkdir("traj-%s"%(n)) 
    os.chdir("traj-%s"%(n)) 
    os.mkdir("log")
    os.system("cp ../vv.py ./")
    os.system("cp ../main.py ./")
    os.system("cp ../model.py ./")
    os.system("cp ../condor* ./")
    os.system("cp ../input.txt ./")
    #dat = np.array([traj, wc])

    os.system("condor_submit condor.sub")
 
    os.chdir("../") 