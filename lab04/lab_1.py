'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version: Jan 1, 2013
@student: Sarah Whitten, March 1 2020
'''

import sys
sys.path.insert(0, '../tools/aima')

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC1 = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print('Probability of having a cavity when there is a toothache: ')
print(PC1.show_approx())

# Compute the value of P(Cavity|Catch)
PC2 = enumerate_joint_ask('Cavity', {'Catch': T}, P)

'''
    First compute P(Cavity|Catch) by hand:
    
                      P(Cavity && Catch)
    P(Cavity|Catch) = ------------------
                           P(Catch)
    
    P(Cavity && Catch) = P[T, T, T] + P[F, T, T] = 0.108 + 0.072 = 0.180
    P(Catch) = P[T, T, T] + P[F, T, T] + P[T, F, T] + P[F, F, T] = 0.108 + 0.072 + 0.016 + 0.144 = 0.340
    P(Cavity|Catch) = 0.180 / 0.340 = 0.529
    
    boldP(Cavity|Catch) = < 0.529, 0.471 >
'''

# verify answer using AIMA approximation
print('Probability of having a cavity when there is a catch: ')
print(PC2.show_approx())

'''
    Compute the probability of two coins both landing heads up
    
                     P(Coin2 && Coin1)
    P(Coin2|Coin1) = -----------------
                         P(Coin1)
                         
    P(Coin2 && Coin1) = 0.5 * 0.5 = 0.25
    P(Coin1) = 0.5
    P(Coin2|Coin1) = 0.25 / 0.5 = 0.5
    
    boldP(Coin2|Coin1) = < 0.5, 0.5 >
'''

# verify answer using AIMA approximation
P = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False                          # where True is Heads and False is Tails
P[T, T] = P[T, F] = P[F, F] = P[F, T] = 0.25

PC3 = enumerate_joint_ask('Coin2', {'Coin1': T}, P)
print('Probability of Coin2 landing heads up given Coin1 lands heads up: ')
print(PC3.show_approx())

# the answer does confirm what I believe to be true
# about the probabilities of flipping coins
