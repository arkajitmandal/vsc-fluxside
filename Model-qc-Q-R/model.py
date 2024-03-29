import numpy as np
from numpy import sum  
from numpy.random import normal as gran
from numpy import pi as π

def dV(x, param):
    ωc = param.ωc
    ωQ = param.ωQ
    χ =  param.χ
    dv = np.zeros(len(x))
    c  = χ * (2.0 /ωc**3.0)**0.5 # check
    cQ = param.cQ
    #-----------------------------------------------------------------!
    # Nuclear DOFs ---------------------------------------------------!
    #-----------------------------------------------------------------!
    dv[0]  =  dE(x[0])                                            # Molecular part
    # dv[0] +=  (ωc**2.0) * (x[1] + c * x[0]) * c                 # Cavity
    dv[0] +=  (ωQ**2.0) * (x[2] + (cQ/ωQ**2) * x[0]) * (cQ/ωQ**2) # Q mode
    #-----------------------------------------------------------------!
    # Cavity DOFs ----------------------------------------------------!
    #-----------------------------------------------------------------!
    dv[1]   =  (ωc**2.0) * (x[1] + c * x[2])  
    #-----------------------------------------------------------------!
    # Solvent DOF ----------------------------------------------------!
    #-----------------------------------------------------------------!
    dv[2]  =  (ωQ**2.0) * (x[2] + (cQ/ωQ**2) * x[0])  
    dv[2] +=  (ωc**2.0) * (x[1] + c * x[2]) * c          # Cavity
    return dv

def force(x, param):
    return -1.0 * dV(x, param)

def E(R):
    ωb = 0.004556335 # 1000 cm-1
    Eb = 0.01025175  # 2250 cm-1
    a =  ωb**4/(16*Eb) #/10.0
    b = -ωb**2/2 #/10.0

    return a*(R**4) + b*(R**2) #+ c * R

def dE(R):
    ωb = 0.004556335 # 1000 cm-1
    Eb = 0.01025175  # 2250 cm-1
    a =  ωb**4/(16*Eb) #/10.0
    b = -ωb**2/2 #/10.0
    return 4.0 * a * (R**3) + 2.0 * b * R #+ c * R

def init(param):

    β = param.β
    ndof = param.ndof


    # All mode frequencies
    ω = np.zeros((ndof))
    σx = np.zeros((ndof))
    ω[1] = param.ωc        # 1 --> Cavity
    ω[2] = param.ωQ        # 1 --> Q Mode
    
    
    σx[1:] = (1/ (β * ω[1:]**2.0) ) ** 0.5
    σp = (1/β)**0.5 
    #-------- Nuclear DOF ----------
    x = np.zeros(ndof)
    x[0]  = 0.0            # Nuclear DOF
    x[1]  = gran(0, σx[1]) # Cavity DOF 
    x[2]  = gran(0, σx[2]) # Q DOF 
    #-------------------------------
    p =  gran(0,σp,ndof)


    # Auxilary Modes
    S = np.zeros((ndof))
    S[0] = gran(0, (2 * param.Λ[0]/β/ param.dt)**0.5)
    S[1] = gran(0, (2 * param.Λ[1]/β/ param.dt)**0.5)
    S[2] = gran(0, (2 * param.Λ[2]/β/ param.dt)**0.5)
    return x, p, S


# Loss -----------------------------------------------
def λc(tau, ωc, g, beta):
    fs =  41.341374575751
    lr = 1.0/(tau*fs)
    return lr * ωc/4.0*(1.0-np.exp(-beta*ωc)) * (g*g+ωc*ωc)/(ωc*g) 


class param:
    def __init__(self, ωc, η = 0.0025, bath = 0.1):
        self.ωc = ωc
        self.ndof = 3 

        self.T = 300.0
        self.β = 315774/self.T  
        self.m = np.ones(self.ndof) 

        self.t =  4200 * 20 
        self.dt = 15.0
        self.χ  = self.ωc * η
        self.traj = 1

        # ------ Cavity Loss ----------------------
        self.Γc  = 0.0009113 * 5 # 1000 cm-1
        self.Λc  = λc(1000.0, ωc, self.Γc, self.β) 

        # ------ Solvent Bath ---------------------
        self.ΓB  = 0.0009113     # 200 cm-1
        ωb = 0.004556335 
        ɑ  = bath * ωb
        self.ΛB  = ɑ * self.ΓB /2 


        
        # ------- Q Mode ---------------------------
        self.ωQ  = 0.0054676        # 1200 cm-1
        self.cQ  =  5 * (10**(-6))  # 5x10^-6
        self.ΛQ  = 6.7 * (10**(-7)) 
        self.ΓQ  = 0.0009113 * 5 # 1000 cm-1
        #-------------------------------------------
        
        
        # Solvent
        self.Λ = np.array([self.ΛB, self.Λc, self.ΛQ])
        self.Γ = np.array([self.ΓB, self.Γc, self.ΓQ])
        
        
        self.nskip = 10