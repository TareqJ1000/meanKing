# -*- coding: utf-8 -*-
"""
WIP: Code that computes the detection probabilities for two-detector clicks in the MKP setup. 
"""
import numpy as np
import sympy as sp
from compSuccessProb import computeProb, createCompleteSet, MostProbClicks, calcCoeffsNeo 
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
import math 

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

bestPhases = [np.random.uniform(-np.pi,np.pi) for z in range(6)]
#bestPhases = np.load('bestPhases/3D_MKP_Phase.npy')
DIM = 3
mkpFun = 'expansionFuncs/3D_MKP.txt'
vaaFun = 'expansionFuncs/3D.txt'
singleDetect = False
detectorSet = [c_0,d_0,e_0,f_0,g_0,h_0]

coeffLists = computeProb(bestPhases,vaaFun,DIM)

colors = cm.rainbow(np.linspace(0, 1, 9))

# Create float list of coefficents
keyLists = []
detectorSets = createCompleteSet(detectorSet,singleDetect)

for detect in detectorSets:
  prod = f"${detect}$" 
  prod2 = prod.replace("*",'') 
  keyLists.append(prod2)
  
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(10,10))
  
# Make subplots (for 3D case)

for i, ax in enumerate(axes.flatten()):
    ax.set_title(f'$|\phi_{i}>$')  # Set a title for each subplot
    sns.barplot(x=keyLists, y=coeffLists[i], ax=ax,color=colors[math.floor(i)])
    ax.tick_params(axis='x', rotation=45)
    ax.set_ylim([0,1])
    
plt.tight_layout()
plt.savefig('MKP_3D_successProbs.pdf', format='pdf')
    





'''

plt.figure(figsize=(20,20))
plt.subplot(331)
fig = plt.bar(range(len(keyLists)), coeffLists[0],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[0])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(332)
fig = plt.bar(range(len(keyLists)), coeffLists[1],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[1])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(333)
fig = plt.bar(range(len(keyLists)), coeffLists[2],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[2])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(334)
fig = plt.bar(range(len(keyLists)), coeffLists[3],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[3])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(335)
fig = plt.bar(range(len(keyLists)), coeffLists[4],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[4])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(336)
fig = plt.bar(range(len(keyLists)), coeffLists[5],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[5])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(337)
fig = plt.bar(range(len(keyLists)), coeffLists[6],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[6])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(338)
fig = plt.bar(range(len(keyLists)), coeffLists[7],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[7])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplot(339)
fig = plt.bar(range(len(keyLists)), coeffLists[8],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[8])
plt.ylabel("Detection Probability")
#plt.ylim([0,1])
plt.xticks(rotation=45);
plt.subplots_adjust(left = -0.50)
plt.savefig("3D_MKP_DetectorProb_V1.pdf", format='pdf')
'''