import numpy as np 
import model
from numpy.random import normal as gran

def vvgle(x, p, S, param, f1):

    ndof = len(x)
    β  = param.β
    dt = param.dt
    Λ = param.Λ #/ param.m
    Γ = param.Γ 
    v = p/param.m

    #---- Advance v by half step -----------
    v += (f1 + S) * dt/2  
    #---- X update -----------
    x += (v * dt)
    #---- S update -----------
    θ = np.exp(-dt * Γ)
    αk = ((1-θ)**2/dt)**0.5
    ck = 2 * Λ/Γ
    B  = np.random.normal(size=ndof)
    S = θ * S - (1 - θ) * ck * v + αk * B * (2 * ck/β)**0.5 
    #---- V update -----------    
    f2 = model.force(x, param)
    v +=  (f2 + S) * dt/2
    #-------------------------

    return x, v * param.m, S, f2