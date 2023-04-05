import numpy as np
import sympy as sp
from compSuccessProb import computeProb, createCompleteSet, MostProbClicks, calcCoeffsNeo 
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#Detector modes
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

bestPhases = np.load('bestPhases/5D_MKP_SD.npy')
DIM = 5
mkpFun = 'expansionFuncs/superV_5D_SD_MKP.txt'
vaaFun = 'expansionFuncs/superV_5D_SD.txt'
singleDetect = True
detectorSet = [c_0,d_0,e_0,f_0,g_0,h_0,i_0,j_0,k_0,l_0]
coeffLists = computeProb(bestPhases,mkpFun,DIM)
mostProbs = MostProbClicks(bestPhases,detectorSet, DIM, vaaFun, singleDetect)
detectorSets = createCompleteSet(detectorSet,singleDetect)

# Compute MKP Sucess Probability for first two bases in 5D

zeroBasis = [[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
oneBasis = [[0,6,12,18,24],[4,5,11,17,23], [3,9,10,16,22],[2,8,14,15,21], [1,7,13,19,20]]
twoBasis = [[0,8,11,19,22], [2,5,13,16,24], [4,7,10,18,21], [1,9,12,15,23], [3,6,14,17,20]]
threeBasis = [[0,7,14,16,23], [3,5,12,19,21], [1,8,10,17,24], [22,15,13,6,4], [3,9,11,18,20]]
fourBasis = [[0,9,13,17,21], [1,5,14,18,22], [2,10,19,23,6], [3,7,11,15,24], [20,16,12,8,4]]
fiveBasis = [[0,5,10,15,20], [1,6,11,16,21], [2,7,12,17,22], [3,8,13,18,23], [4,9,14,19,24]]

def computeMKPSU(basis,detectorSets,mostProbs,coeffLists):
    basisSU = []
    for ii, sl in enumerate(basis):
        temp = 0
        for item in sl:
            for jj, detect in enumerate(detectorSets):
                if (mostProbs[detect][0] == item):
                    temp += coeffLists[ii][jj]
        basisSU.append(temp)
    print(f"success probabilities (state-by-state): {basisSU}")
    print(f"average success probability: {np.average(basisSU)}")


