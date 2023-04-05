# meanKing
Analysis code for the paper "Experimental Solutions to the High-Dimensional Mean King's Problem" by Jaouni et al. The code can 
- Generate VAA states for any prime dimension using the Hayashi paper construction 
- Computes the path mode polynomials corresponding to each input VAA state when they are each set onto the experimental setup
- Computes/Plots the detector probabilities and the success probability of measurement on a VAA state. Options avaliable for with and without single detector clicks   and also for detector probabilities when sending MKP states as input
- Fine tune the phases in the setup using a naive optimization routine (more or less default configuration from scipy.minimize)

To do: 
- Implement way to systematically compute the probability of a successful measurement for MKP. 
- The dimensionality of our optimization space is very likely way, way bigger than is needed (5-Dimensions in particular has 60 PHASE SHIFTERS to optimize). We could    try doing some kind of sensitivity analysis to reduce the dimensionality of the optimization problem. In turn, this may allow us to converge to better solutions. 



