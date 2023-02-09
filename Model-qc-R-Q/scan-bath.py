import numpy as np
import os
files = ['model.py', 'main.py', 'vv.py', 'condor.sh', 'condor.sub', 'run.py']
wc = 0.05 
eta = 0.0
traj = 1000
bath = np.arange(0.1, 3.0, 0.2)
folds = 50

def cp(a,b):
    try:
        os.mkdir(f"{b}")
    except:
        print (f"{b} exists")
    os.system(f"cp {a} {b}/")

#os.mkdir("scans")
os.chdir("scans")
for ib in range(len(bath)):
    
    for jfile in files:
        cp(f"../{jfile}", f"bath-{bath[ib]}")
    np.savetxt(f'bath-{bath[ib]}/input.txt', np.array([traj, wc/27.2114, eta, bath[ib]]))

    os.chdir(f'bath-{bath[ib]}')
    os.system(f"python run.py {folds}")
    os.chdir('../')

