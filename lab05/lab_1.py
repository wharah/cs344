'''
This module implements the Bayesian network shown in the text, Figure 14.2. It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
@student: Sarah Whitten, March 8 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask, rejection_sampling

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

print()
# Compute P(Burglary | John and Mary both call).
print('enumeration: ', enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print('elimination: ', elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print('gibbs: ', gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.
print('rejection: ', rejection_sampling('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())

'''
Exercise 5.4

The enumeration_ask and elimination_ask algorithms produce the same results, but the gibbs_ask algorithm does not.
According to the comment above the elimination_ask() call, it's just a dynamic processing version of the 
enumeration_ask() method. The rejection_sampling() call wasn't originally included, so I added it in. Both the 
gibbs method and rejection_sampling methods produced different answers each time I ran the code. Neither of them match
the results from the enumeration_ask and elimination_ask algorithms. This is because they are sampling
'''

print()

# Exercise 5.1
# i. P(Alarm | Burglary ^ ¬Earthquake)
print("i.   ", enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# ii. P(JohnCalls | Burglary ^ ¬Earthquake)
print("ii.  ", enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# iii. P(Burglary | Alarm)
print("iii. ", enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# iv. P(Burglary | JohnCalls ^ MaryCalls)
print("iv.  ", enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
