# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 14:59:47 2016

@author: Ivan

Given a sample space {'sunny', 'rainy', 'snowy'},
produces two finite random variables:
W, whose alphabet is a mapping of the sample space OMEGA to {'sunny', 'rainy', 'snowy'} (don't change)
and I, whose alphabet is a mapping of the sample space to {0, 1} 
"""

import comp_prob_inference # import all necessary stuff

# define the sample space (OMEGA) and the probability of each outcome
prob_space = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}

# define the mapping alphabet of the W finite random variable
W_mapping = {'sunny': 'sunny', 'rainy': 'rainy', 'snowy': 'snowy'}

# define the mapping alphabet of the I finite random variable
I_mapping = {'sunny': 1, 'rainy': 0, 'snowy': 0}


# generate a random sample outcome for random variables W and I
random_outcome = comp_prob_inference.sample_from_finite_probability_space(prob_space)

W = W_mapping[random_outcome]

I = I_mapping[random_outcome]

print ('W =', W)
print ('I =', I)