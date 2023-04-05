import numpy as np
import sympy as sp
from scipy.optimize import minimize
from compSuccessProb import successProb
import yaml 
from yaml import Loader

c_0 = sp.Symbol('c_0')
d_0 = sp.Symbol('d_0')
e_0 = sp.Symbol('e_0')
f_0 = sp.Symbol('f_0')
g_0 = sp.Symbol('g_0')
h_0 = sp.Symbol('h_0')
i_0 = sp.Symbol('i_0')
j_0 = sp.Symbol('j_0')
k_0 = sp.Symbol('k_0')
l_0 = sp.Symbol('l_0')

def optimPhase(cnfg):
    shift = 1 # Might be able to adapt this into a parser
    # Detector modes
    
    # Parameters
    detectorSet = [eval(detect) for detect in cnfg['detectorSet']]
    DIM = cnfg['DIM']
    vaaFun = cnfg['vaaFun']
    singleDetect = cnfg['singleDetect']
    
    bnds = np.array([(-np.pi,np.pi) for z in range(60)])
    best = None
    bests = []
    
    for ii in range(200000):
            initPhases = [np.random.uniform(-np.pi,np.pi) for z in range(60)]
            res = minimize(successProb, initPhases,args=(detectorSet, DIM, vaaFun, singleDetect), bounds=bnds)
            bests.append(res.x)
            if best is None or res.fun < best.fun:
                best = res
                print(f"Best Phases Set: {best.x}")
                np.save(f"bestPhases/{cnfg['output']}.npy",best.x)


stream = open("configs/optim.yaml", 'r')
cnfg = yaml.load(stream, Loader=Loader)
optimPhase(cnfg)





            
            



