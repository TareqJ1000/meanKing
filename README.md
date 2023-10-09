# meanKing
Analysis code for the paper "Experimental Solutions to the High-Dimensional Mean King's Problem" by Jaouni et al. The code can 

- Generate the VAA states for any prime dimension (except 2, which is hard-coded in the analysis code) following the Hayashi construction. 
- Computes the path mode polynomials corresponding to each input VAA state when they are each set onto experimental setups. The experimental setups are represented mathematically by the transformations that they apply to input photon modes, and have to be computed by hand. 
- Computes/plots the detector probabilities and the success probability of measurement on any given VAA state, as well as the probability that Alice succeeds against the mean king. Options avaliable for with and without single detector clicks,  and also for detector probabilities when sending MKP states as input. 
- Fine tune the phases in the setup using a post-processing BFGS optimization routine.

The CalculateSetups.ipynb or CompMKPExpansion.ipynb codes can be run to output a .txt file containing functions which implements the transformations from input to output. You then specify this in the .yaml file, then run computePhase to fine-tune the phases. The AnalyzeSetupProb.ipynb runs the analysis on the setups. 



