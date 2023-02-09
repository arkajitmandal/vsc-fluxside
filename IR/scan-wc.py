import numpy as np
import os
files = ['model.py', 'main.py', 'vv.py', 'condor.sh', 'condor.sub', 'run.py']
wc = np.linspace(0.0,0.05*6, 21)[2:3]#[4:-3] #+ 0.01

#dwc = (wc[1] - wc[0])/2

wc = wc #+ dwc
#wc = np.linspace(0.0,0.05*6, 21)[:][1:2]
eta = 0.00125 * 0
traj = 200
folds = 250
bath = 0.1
offset = 0


folderName = "scans"
def cp(a,b):
    try:
        os.mkdir(f"{b}")
    except:
        print (f"{b} exists")
    os.system(f"cp {a} {b}/")
try:
    os.mkdir(folderName)
except :
    pass

os.chdir(folderName)

for iwc in range(len(wc)):
    
    for jfile in files:
        cp(f"../{jfile}", f"wc-{int(wc[iwc]*1000)/1000}")
    if wc[iwc] == 0:
        np.savetxt(f'wc-{int(wc[iwc]*1000)/1000}/input.txt', np.array([traj, wc[iwc]/27.2114,   0, bath]))
    else:
        np.savetxt(f'wc-{int(wc[iwc]*1000)/1000}/input.txt', np.array([traj, wc[iwc]/27.2114, eta, bath]))



    os.chdir(f'wc-{int(wc[iwc]*1000)/1000}')
    os.system(f"python run.py {folds} {offset}")
    os.chdir('../')

