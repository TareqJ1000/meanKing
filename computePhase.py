import numpy as np
import sympy as sp
from scipy.optimize import minimize
from compSuccessProb import successProb
import yaml 
from yaml import Loader

shift = 1 # Might be able to adapt this into a parser
# Detector modes
c_0 = sp.Symbol('c_0')
d_0 = sp.Symbol('d_0')
e_0 = sp.Symbol('e_0')
f_0 = sp.Symbol('f_0')
g_0 = sp.Symbol('g_0')
h_0 = sp.Symbol('h_0')

stream = open("configs/optim.yaml", 'r')
cnfg = yaml.load(stream, Loader=Loader)

# Parameters (FOR 2D)
detectorSet = [eval(detect) for detect in cnfg['detectorSet']]
DIM = cnfg['DIM']
vaaFun = cnfg['vaaFun']
singleDetect = cnfg['singleDetect']

bnds = np.array([(-np.pi,np.pi) for z in range(12)])
best = None
bests = []

for ii in range(200000):
        initPhases = [np.random.uniform(-np.pi,np.pi) for z in range(12)]
        res = minimize(successProb, initPhases,args=(detectorSet, DIM, vaaFun, singleDetect), bounds=bnds)
        bests.append(res.x)
        if best is None or res.fun < best.fun:
            best = res
            print(f"Best Phases Set: {best.x}")
            np.save(f"bestPhases/{cnfg['output']}.npy",best.x)
            
            



