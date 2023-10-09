import numpy as np
import sympy as sp
from compSuccessProb import computeProb, createCompleteSet, MostProbClicks, calcCoeffsNeo 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from vaaGen import striation_func

# The following functions are used to compute the set of VAA states corresponding to each possible eignestate

def compVAASet(DIM):
    vaaOrtho = {}
    count = 0
    for j in np.arange(0,DIM):
        for i in np.arange(0,DIM):
            listor = []
            for m in np.arange(0, DIM+1):
                listor.append((m, striation_func(DIM,m,i,j)))
            vaaOrtho[count] = listor
            count = count+1
    return vaaOrtho

# Compute set of VAA sets for the eigenstates of a given basis

def compBasis(DIM,m):
    vaaOrtho = compVAASet(DIM)
    basis = []
    for ii in range(DIM):
        temp = []
        for count, raga in enumerate(vaaOrtho.values()):
            if(raga[m][1] == ii):
                temp.append(count)
        basis.append(temp)
    return basis


# Function that computes the sucess probability for Alice's mean king measurement
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
    return np.average(basisSU)

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
m_0 = sp.Symbol('m_0')
n_0 = sp.Symbol('n_0')
o_0 = sp.Symbol('o_0')
p_0 = sp.Symbol('p_0')
#zeroBasis =  compBasis(3,0)
'''
bestPhases = np.load('bestPhases/7D_MKP.npy')
DIM = 7
mkpFun = 'expansionFuncs/7D_MKP.txt'
vaaFun = 'expansionFuncs/7D.txt'
singleDetect = False
detectorSet = [c_0,d_0,e_0,f_0,g_0,h_0,i_0,j_0,k_0,l_0,m_0,n_0,o_0,p_0]
coeffLists = computeProb(bestPhases,mkpFun,DIM)
mostProbs = MostProbClicks(bestPhases,detectorSet, DIM, vaaFun, singleDetect)
detectorSets = createCompleteSet(detectorSet,singleDetect)


# Compute MKP Sucess Probability for first two bases in 5D

zeroBasis = compBasis(5,0)
oneBasis =  compBasis(5,1)
twoBasis =  compBasis(5,2)
threeBasis =  compBasis(5,3)
fourBasis = compBasis(5,4)
fiveBasis =  compBasis(5,5)



# For 3D

# in 3D

zeroBasis =  compBasis(3,0)
oneBasis = compBasis(3,1)
twoBasis = compBasis(3,2)
threeBasis = compBasis(3,3)

# For 7D

zeroBasis = compBasis(7,0)
oneBasis =  compBasis(7,1)
twoBasis =  compBasis(7,2)
threeBasis =  compBasis(7,3)
fourBasis = compBasis(7,4)
fiveBasis =  compBasis(7,5)
sixBasis = compBasis(7,6)
sevenBasis =  compBasis(7,7)


zerBase = computeMKPSU(zeroBasis, detectorSets, mostProbs, coeffLists[0:7])
oneBase = computeMKPSU(oneBasis, detectorSets, mostProbs, coeffLists[7:14])
twoBase = computeMKPSU(twoBasis, detectorSets, mostProbs, coeffLists[14:21])
threeBase = computeMKPSU(threeBasis, detectorSets, mostProbs, coeffLists[21:28])
fourBase = computeMKPSU(fourBasis, detectorSets, mostProbs, coeffLists[28:35])
fiveBase = computeMKPSU(fiveBasis, detectorSets, mostProbs, coeffLists[35:42])
computeMKPSU(sixBasis, detectorSets, mostProbs, coeffLists[42:49])
computeMKPSU(sevenBasis, detectorSets, mostProbs, coeffLists[49:56])
'''



