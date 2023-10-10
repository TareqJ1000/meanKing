import numpy as np
import sympy as sp

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

# Initialize symbols
# Input modes
a_0 = sp.Symbol('a_0')
a_1 = sp.Symbol('a_1')
a_2 = sp.Symbol('a_2')
a_3 = sp.Symbol('a_3')
a_4 = sp.Symbol('a_4')

b_0 = sp.Symbol('b_0')
b_1 = sp.Symbol('b_1')
b_2 = sp.Symbol('b_2')
b_3 = sp.Symbol('b_3')
b_4 = sp.Symbol('b_4')


# Converts phases from polar coordinates (exp(1*z) to cartesian coordinates (a+ib). 
# Note that this forces any phase we apply onto our system to lie on the unit circle around the origin
# z - list (float) - sets of phases 

def polarToCart(z):
    return [np.exp(1j*v) for v in z]


# Creates the complete set of possible two-detector clicks in the setup
# detectorSet -- list -- list of all detector modes in the setup

def createCompleteSet(detectorSet, singleDetect):
    completeSet = []
    alreadyCheck = []
    for alpha in detectorSet:
        for beta in detectorSet:
            if (alpha != beta and beta not in alreadyCheck):
                completeSet.append(alpha*beta)
            alreadyCheck.append(alpha)
    if singleDetect:
        for alpha in detectorSet:
            completeSet.append(alpha*alpha)
    return completeSet

# Let's seperately list all the possible single detector clicks present in our setup 

def createSingleDetect(detectorSet):
    singleSet = []
    for alpha in detectorSet:
        singleSet.append(alpha*alpha)
        
    return singleSet 

def normalizeVAANeo(coeffs):
    sum = 0
    for jj in range(len(coeffs)):
            sum += np.abs(coeffs[jj])**2
            
    coeffs = [coeff*(1/np.sqrt(float(sum))) for coeff in coeffs]
    # We verify that the states are normed now
    newSum = 0
    for coeff in coeffs:
        newSum += np.abs(coeff)**2
        
    return coeffs
    

def calcDetectorProbs(detectorSet,coeffs,singleDetect):
    completeSet = createCompleteSet(detectorSet, singleDetect)
    detectorProbs = {}
    for ii, detector in enumerate(completeSet):
        temp = []
        for jj in range(len(coeffs)):
            temp.append((jj, np.abs(coeffs[jj][ii])**2))
        detectorProbs[detector] = temp
    return detectorProbs


def calcMostProbs(detectorProbs):
    mostProb = {}
    for detector in detectorProbs.keys():
        mostProb[detector] = max(detectorProbs[detector], key = lambda item:item[1])
    return mostProb

def calcCondProb(detectorProbs):
    condProb = {}
    mostProb = calcMostProbs(detectorProbs)
    for detector in detectorProbs.keys():
        condProb[detector] = mostProb[detector][1]/(sum(j for i,j in detectorProbs[detector])+1e-20)
    return condProb

# The following functions are used to compute the success probability of our measurement 

def calcTotalProb(detectorProbs,DIM):
    totalProb = {}
    for detector in detectorProbs.keys():
        totalProb[detector] = sum(j for i,j in detectorProbs[detector])/(DIM**2)
    return totalProb 

def calcCoeffsNeo(phases,vaaFun,DIM):
    functions = {}
    exec(open(vaaFun).read(), globals(),functions)
    phase = polarToCart(phases)
    coeffs = []
    normCoeffs = []
    for ii in range(len(functions)):
        coeffs.append(functions[f'superVAA_{ii}'](phase))
    
    for coeff in coeffs:
        normCoeffs.append(normalizeVAANeo(coeff))
    return(normCoeffs)


def computeProb(phases, vaaFun, DIM):
    normCoeffs = calcCoeffsNeo(phases, vaaFun, DIM)
    probAmplitudes = []
    for ii in range(len(normCoeffs)):
        temp = [np.abs(cc)**2 for cc in normCoeffs[ii]]
        probAmplitudes.append(temp)
    return probAmplitudes

def MostProbClicks(phases,detectorSet,DIM,vaaFun,singleDetect):
    coeffs = calcCoeffsNeo(phases,vaaFun,DIM)
    detectorProbs = calcDetectorProbs(detectorSet, coeffs, singleDetect)
    mostProbs = calcMostProbs(detectorProbs)
    return mostProbs 

 
def successProb(phases, detectorSet,DIM,vaaFun,singleDetect):
    coeffs = calcCoeffsNeo(phases,vaaFun,DIM)
    detectorProbs = calcDetectorProbs(detectorSet, coeffs,singleDetect)
    totalProb = calcTotalProb(detectorProbs,DIM)
    condProb = calcCondProb(detectorProbs)
    successProb = 0 
    #singleDetect = createSingleDetect(detectorSet)
    for detector in detectorProbs.keys():
        successProb = successProb + (condProb[detector]*totalProb[detector])
    print(-successProb)
    return -successProb


def mostProbOptim(phases, vaaFun, DIM): # Here, we are interested if we maximize the probability of one of the two detector clicks
    probAmplitudes = computeProb(phases, vaaFun, DIM)
    return -probAmplitudes[0][0]
    
    

