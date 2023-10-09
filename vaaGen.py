# For now, this is used to compute the optimal phases for high-dim MKP setups
# using some optimization routines (we're using ga for now). 

import numpy as np
import sympy as sp


# MKP state generation functions. PRIME DIMENSIONS ONLY

# Used in the formula for generating eigenstates for prime dimensions. Starts from the current 'l' in the summation 
# dim - int - dimension of state 
# l - int - current index of summation 

def sum_func(dim,l):
  sum_terms = []
  for i in np.arange(0,dim):
    sum_terms.append(i)
  return(np.sum(sum_terms[l::]))

# Generate eigenstates. We express them in terms of either vector notation or in terms of photonic paths. 
# dim - int - dimension of interest
# isBar - boolean - determines if we compute the barred eigenstate (essentially taking the complex congugate of the state)

def eigenstate(dim, isBar, vectorMode):
  numOfEigenstates = dim
  numOfBases = dim + 1
  qew = np.exp(1j*(2*np.pi)/dim) # dth root of unity
  input_modes_a = []
  input_modes_b = []
  eigenstates = []
  
  if(vectorMode):
   for i in np.arange(0,numOfEigenstates):
     temp_arr_a = np.array([np.zeros(dim)]).transpose()
     temp_arr_b = np.array([np.zeros(dim)]).transpose()
     temp_arr_a[i][0] = 1
     temp_arr_b[i][0] = 1
     input_modes_a.append(temp_arr_a)
     input_modes_b.append(temp_arr_b)
  else:
   for i in np.arange(0,numOfEigenstates):
     temp_a = sp.Symbol(f'a_{i}')
     temp_b = sp.Symbol(f'b_{i}')
     input_modes_a.append(temp_a)
     input_modes_b.append(temp_b)

  if (isBar):
    eigenstates.append(input_modes_a)
  else: 
    eigenstates.append(input_modes_b)
 
  for m in np.arange(1,numOfBases):
    temp = []
    for i in np.arange(0, numOfEigenstates):
      temp2 = 0
      for j in np.arange(0, numOfEigenstates):
        san = sum_func(dim,j)
        if (isBar):
         temp2 += np.conj((1/np.sqrt(dim))*qew**(i*(dim-j) - m*san)) * input_modes_a[j]
        else:
         temp2 += (1/np.sqrt(dim))*qew**(i*(dim-j) - m*san)*input_modes_b[j]
      temp.append(temp2)
    eigenstates.append(temp)

  return(eigenstates)
  
# Computes the tensor product between two kets. It is expected that the kets are expressed as vectors
# a_0, b_0 - np.ndarray - vector form of our kets

def tensorProd(a_0,b_0):  
 c = np.tensordot(a_0,b_0,axes=0)
 c_full = np.concatenate((c[:]), axis=1)
 c_full = c_full.reshape(-1, *c_full.shape[:-2])
 return(c_full)

# This computes the inner product of two kets.
# a_0, b_0 - np.ndarray - vector form of our kets

def compute_magnitude(a_0,b_0): 
 magnitude = np.dot(np.conj(a_0).transpose(),b_0)
 return magnitude[0][0]

# Computes the two-qudit states in terms of computational basis
# dim - int - desired dimension
# vectorMode - boolean - expresses the states as ndarrays

def twoKets(dim,vectorMode):
  numOfEigenstates = dim
  numOfBases = dim+1
  eigenstates_a = eigenstate(dim,False,vectorMode)
  eigenstates_b = eigenstate(dim,True,vectorMode)
  twoKets = []
  for m in np.arange(0,numOfBases):
    temp = []
    for i in np.arange(0,numOfEigenstates):
      if (vectorMode):
       temp.append(tensorProd(eigenstates_a[m][i],eigenstates_b[m][i]))
      else:
       temp.append(eigenstates_a[m][i]*eigenstates_b[m][i])
    twoKets.append(temp)
  return twoKets

# Function used to construct the D^2 orthogonal latin squares (with each one corresponding to a VAA state). This link was found cruically through the Hayashi paper.
# dim - int - desired dimension
# m - int - desired basis
# i, j - int - indices of the latin square

def striation_func(dim,m,i,j):
  if m < dim:
    return (j-m*i)%dim
  else:
    return (i)%dim

# Generates the MKP states 
# dim - int - desired dimension
# vectorMode - boolean - if true, expresses states in terms of ndarrays rather than path modes

def mkpGEN(dim,vectorMode):
  num_of_bases = dim + 1
  MEAN_KING = []
  eigenstates = twoKets(dim,vectorMode)
  if (vectorMode):
   psi_0 = (1/np.sqrt(dim)) * np.add.reduce(eigenstates[0])
  else:
   psi_0 = (1/np.sqrt(dim)) * np.sum(eigenstates[0])
  # Define indices for striation function
  for j in np.arange(0,dim):
    for i in np.arange(0,dim):
      phi = -psi_0
      for m in np.arange(0,num_of_bases):
        map = striation_func(dim,m,i,j)
        phi = phi + (1/np.sqrt(dim))*eigenstates[m][map]
      MEAN_KING.append(phi)
  return MEAN_KING






