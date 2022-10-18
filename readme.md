# Flux-Side code to obtain transmission coefficient 

Here a molecular system, described with a symmetric double well potential, is coupled to a unstructured dissipative solvent environment (described by Debye spectral density) a cavity radiation mode which is also coupled to a dissipative environment (described by Debye spectral density).

In this repository there are three main codes,

* main.py : propgates the dynamics and computes the transmission coefficient. Creates a 'fs.txt' file with two column :time, transmission coefficient. 

* model.py : describes the model system. Provides forces on each degree of freedom (DOF) and initializes all variables.

* vv.py : velocity Verlet like algorithm that propagates the generalized Langevin equation [see J. Chem. Phys. 139, 044107 (2013)]. 

There is a input file: input.txt that takes in 4 parameters: (1) Number of trajectories (INT) (2) Photon frequency ω$_c$ (FLOAT) in a.u. (3) Light-matter coupling η in a.u. and (4) Solvent friction parameter a such that solvent friction is η$_s$ = a * ω$_b$. 

Directly running the following code in the terminal works.
```
python main.py
```

Additional scripts are provided for parallelizing the program in ht-condor based systems,

* scan-bath.py : submits jobs for a range of bath parameters with no coupling to the cavity (generates the Kramers Turnover) 
* scan-wc.py