import numpy as np
import sympy as sp
from scipy.optimize import minimize
from compSuccessProb import successProb, mostProbOptim
import yaml 
from yaml import Loader
import time

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
m_0 = sp.Symbol('m_0')
n_0 = sp.Symbol('n_0')
o_0 = sp.Symbol('o_0')
p_0 = sp.Symbol('p_0')
q_0 = sp.Symbol('q_0')
c_1 = sp.Symbol('c_1')
d_1 = sp.Symbol('d_1')

def optimPhase(cnfg):
    shift = 1 # Might be able to adapt this into a parser
    # Detector modes
    # Parameters
    detectorSet = [eval(detect) for detect in cnfg['detectorSet']]
    DIM = cnfg['DIM']
    vaaFun = cnfg['vaaFun']
    singleDetect = cnfg['singleDetect']
    numOfPhases = cnfg['numOfPhases']
    
    bnds = np.array([(-np.pi,np.pi) for z in range(numOfPhases)])
    best = None
    bests = []
    
    totalStartTime = time.time()
    
    for ii in range(1000):
            startTime = time.time()
            initPhases = [np.random.uniform(-np.pi,np.pi) for z in range(numOfPhases)]
            #print(initPhases)
            res = minimize(successProb, initPhases,args=(detectorSet, DIM, vaaFun, singleDetect), bounds=bnds)
            bests.append(res.x)
            if best is None or res.fun < best.fun:
                best = res
                np.save(f"bestPhases/{cnfg['output']}.npy",best.x)
            print(f"Iteration: {ii}")
            print(f"Best success Prob: {best.fun}")
            print(f"Excecution Time: {time.time() - startTime}")
            
    print(f"Optimization Finished!\nTotal Execution time: {time.time() - totalStartTime}")

stream = open("configs/optim0.yaml", 'r')
cnfg = yaml.load(stream, Loader=Loader)
optimPhase(cnfg)





            
            



