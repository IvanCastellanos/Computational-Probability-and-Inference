# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:08:56 2016

@author: Ivan
In this second approach, we are going to write directly 
the probability tables, for random finite variables W and I
"""

import comp_prob_inference # import all required stuff

# define the table of the finite random variable W
W_table = {'sunny': 1/2, 'rainy': 1/6, 'snowy': 1/3}

# define the table of the finite random variable I
I_table = {0: 1/2, 1: 1/2}

# treating tables as probability spaces, draw samples for W and I each
W = comp_prob_inference.sample_from_finite_probability_space(W_table)
I = comp_prob_inference.sample_from_finite_probability_space(I_table)

print('W =', W)
print('I =', I)