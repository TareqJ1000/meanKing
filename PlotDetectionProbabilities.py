# -*- coding: utf-8 -*-
"""
WIP: Code that computes the detection probabilities for two-detector clicks in the MKP setup. 
"""
import numpy as np
import sympy as sp
from compSuccessProb import computeProb, createCompleteSet 
import matplotlib.pyplot as plt

#Detector modes
c_0 = sp.Symbol('c_0')
d_0 = sp.Symbol('d_0')
e_0 = sp.Symbol('e_0')
f_0 = sp.Symbol('f_0')
g_0 = sp.Symbol('g_0')
h_0 = sp.Symbol('h_0')

bestPhases = np.load('best_3D_1.npy')
coeffLists = computeProb(bestPhases)

import matplotlib.cm as cm
colors = cm.rainbow(np.linspace(0, 2, 18))

# Create float list of coefficents
keyLists = []
detectorSets = createCompleteSet([c_0,d_0,e_0,f_0,g_0,h_0])

#bestCoeffs = createVAACoeffs(polarToCart(initPhase))

for detect in detectorSets:
  prod = f"${detect}$" 
  prod2 = prod.replace("*",'') 
  keyLists.append(prod2)
  

plt.figure(figsize=(20,20))
plt.subplot(331)
fig = plt.bar(range(len(keyLists)), coeffLists[0],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[0])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(332)
fig = plt.bar(range(len(keyLists)), coeffLists[1],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[1])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(333)
fig = plt.bar(range(len(keyLists)), coeffLists[2],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[2])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(334)
fig = plt.bar(range(len(keyLists)), coeffLists[3],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[3])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(335)
fig = plt.bar(range(len(keyLists)), coeffLists[4],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[4])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(336)
fig = plt.bar(range(len(keyLists)), coeffLists[5],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[5])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(337)
fig = plt.bar(range(len(keyLists)), coeffLists[6],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[6])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(338)
fig = plt.bar(range(len(keyLists)), coeffLists[7],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[7])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplot(339)
fig = plt.bar(range(len(keyLists)), coeffLists[8],  width = 0.8, tick_label = keyLists, align = 'center', color = colors[8])
plt.ylabel("Detection Probability")
plt.xticks(rotation=45);
plt.subplots_adjust(left = -0.75)
plt.savefig("3D_VAA_DetectorProb_V1.png")