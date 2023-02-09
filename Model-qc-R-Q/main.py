import numpy as np
from vv import *
from model import *
import sys
import copy
from numpy.random import normal as gran
import time



def run(param, output=False, idx = 0):
    nskip = 10
    ndof = param.ndof
    t0 = time.time()
    t = np.arange(0,param.t,param.dt) 
    xavg = np.zeros(len(t)) 
    fs = np.zeros(len(t)) 
    fs0 = 0.0
    try:
        np.random.seed(param.SEED)
        print (f"ID: {param.ID}, SEED: {param.SEED}")
    except:
        pass

    for itraj in range(param.traj): 
        print (itraj)  
        x = np.zeros(ndof)  
        p = np.zeros(ndof)

        # Sample
        x, p, S = init(param)

        if itraj%2 != 0:
            p[0]  = -pLast
        else :
            pLast = p[0]


        p0   = p[0] 
        fs0 += (p0  > 0) * p0  

        f1 = force(x, param)
        for ti in range(len(t)):

            x, p, S, f1 = vvgle(x, p, S, param, f1)
            xavg[ti] += x[0] 
            fs[ti] += (x[0]>0) * p0

    xavg = xavg/param.traj
    fs = fs/(fs0)
    if output:
        #np.savetxt(f"x.txt",np.c_[t[::nskip],xavg[::nskip]])
        np.savetxt(f"fs-{idx}-{param.traj}.txt",np.c_[t[::nskip],fs[::nskip]])
    print (f"Time: {time.time()-t0}")
    return fs



if __name__ == "__main__": 
    dat = np.loadtxt("input.txt")
    traj = int(dat[0])
    par = param(dat[1], dat[2], dat[3])
    par.traj = traj
    idx = sys.argv[1]
    run(par, output=True, idx = idx)
