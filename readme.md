[![DOI](https://zenodo.org/badge/553673903.svg)](https://zenodo.org/badge/latestdoi/553673903)



# Flux-Side code to obtain transmission coefficient 

Here a molecular system, described with a symmetric double well potential, is coupled to a unstructured dissipative solvent environment (described by Debye spectral density) a cavity radiation mode which is also coupled to a dissipative environment (described by Debye spectral density).

Requires (no additional installation): Python 3, numpy 
This has been tested on M1 macs and Ht-condor based systems.

In this repository there are three main codes,

* main.py : propgates the dynamics and computes the transmission coefficient. Creates a 'fs.txt' file with two column :time, transmission coefficient. 

* model.py : describes the model system. Provides forces on each degree of freedom (DOF) and initializes all variables.

* vv.py : velocity Verlet like algorithm that propagates the generalized Langevin equation [see J. Chem. Phys. 139, 044107 (2013)]. 

There is a input file: input.txt that takes in 4 parameters: (1) Number of trajectories (INT) (2) Photon frequency $\omega_c$ (FLOAT) in a.u. (3) Light-matter coupling η in a.u. and (4) Solvent friction parameter $a$ such that solvent friction is $\eta_s$ = $a \cdot$  $\omega_b$. 

Directly running the following code in the terminal works.
```
python main.py
```

Additional scripts are provided for parallelizing the program in ht-condor based systems,

* scan-bath.py : submits jobs for a range of bath parameters with no coupling to the cavity (generates the Kramers Turnover) 
* scan-wc.py : Computes transmission coefficient for a range of photon frequencies $\omega_c$. 

The script 'gather_scans.py' can be used to gather all the transmission coefficient with respect to photon frequency or bath coupling (using 'scan-wc.py' or 'scan-bath.py'). 

## Other Model

For other model systems such as qc-R-Q or qc-Q-R see the folders 'Model-qc-R-Q' and 'Model-qc-Q-R' which has the same file structure as the one discussed above. 

## IR
Finally find the IR code in the 'IR' folder. Running the 'main.py' create the R(t)R correlation function. A code 'ftir.py' is provided that can produce the final fourier transformed IR spectrum. 
