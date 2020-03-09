'''
This module implements the Bayesian network for Thrun's confounding clause example.

@author: kvlinden
@version Jan 2, 2013
@student: Sarah Whitten, March 8 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# from figure in Exercise 5.3
happy = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
])

print()

# Exercise 5.3 PART A
# i. P(Raise | Sunny)
print("a. i.  ", enumeration_ask('Raise', dict(Sunny=T), happy).show_approx())
# ii. P(Raise | Happy ^ Sunny)
print("   ii. ", enumeration_ask('Raise', dict(Happy=T, Sunny=T), happy).show_approx())

# Exercise 5.3 PART B
# i. P(Raise | Happy)
print("b. i.  ", enumeration_ask('Raise', dict(Happy=T), happy).show_approx())
# ii. P(Raise | Happy ^ ¬Sunny)
print('   ii. ', enumeration_ask('Raise', dict(Happy=T, Sunny=F), happy).show_approx())

'''
Work by hand:
a) i.  P(Raise | Sunny) = P(Raise)
                        = < P(Raise), P(¬Raise) >
                        = < 0.99, 0.01 >
   ii. P(Raise | Happy ^ Sunny) = ɑ P(Raise) * ( P(Sunny) * P(Happy | Raise, Sunny) )
                                = ɑ < P(Raise) * ( P(Sunny) * P(Happy | Raise, Sunny) ),
                                      P(¬Raise) * ( P(Sunny) * P(Happy | ¬Raise, Sunny) ) >
                                = ɑ < 0.01 * (0.7 * 1.0), 0.99 * (0.7 * 0.7) >
                                = ɑ < 0.01 * 0.7, 0.99 * 0.49 >
                                = ɑ < 0.007, 0.4851 >
                                = < 0.0142, 0.986 >
b) i.  P(Raise | Happy) = ɑ P(Raise) * (( P(Sunny) * P(Happy | Raise, Sunny) ) + 
                            ( P(¬Sunny) * P(Happy | Raise, ¬Sunny) ))
                        = ɑ < P(Raise) * (( P(Sunny) * P(Happy | Raise, Sunny) ) +
                              ( P(¬Sunny) * P(Happy | Raise, ¬Sunny) )),
                              P(¬Raise) * (( P(Sunny) * P(Happy | ¬Raise, Sunny) ) +
                              ( P(¬Sunny) * P(Happy | ¬Raise, ¬Sunny) )) >
                        = ɑ < 0.01 * ((0.7 * 1.0) + (0.3 * 0.9)), 0.99 * ((0.7 * 0.7) + (0.3 * 0.1)) >
                        = ɑ < 0.01 * (0.7 + 0.27), 0.99 * (0.49 + 0.03) >
                        = ɑ < 0.01 * 0.97, 0.99 * 0.52 >
                        = ɑ < 0.097, 0.5148 >
                        = < 0.0185, 0.982 >
   ii. P(Raise | Happy ^ ¬Sunny) = ɑ P(Raise) * ( P(¬Sunny) * P(Happy | Raise, ¬Sunny) )
                                 = ɑ < P(Raise) * ( (P(¬Sunny) * P(Happy | Raise, ¬Sunny) ),
                                       P(¬Raise) * ( (P(¬Sunny) * P(Happy | ¬Raise, ¬Sunny) ) >
                                 = ɑ < 0.01 * (0.3 * 0.9), 0.99 * (0.3 * 0.1) >
                                 = ɑ < 0.01 * 0.27, 0.99 * 0.03 >
                                 = ɑ < 0.027, 0.0297 >
                                 = < 0.0833, 0.917 >

a) i.  This answer was makes sense and is easy to find because the probability of getting a raise is independent of
       the weather. It is just hte probability of getting a raise.
   ii. This answer makes sense because we know that the person is happy, which makes it likely that the person received 
       a raise. However we also know that the weather is sunny, which also makes the person happy and therefore lowers 
       the probability of the happiness being due to a raise instead of the weather.
b) i.  Here, we found the probability of the person receiving a raise and all we know is that they are happy. So we
       took into account the probabilities of being happy with all of the combinations of the weather being sunny and 
       having received a raise or not.
   ii. This answer makes sense because we know that the person is happy, which makes it likely that the person received
       a raise. We also know that the weather is not sunny, which makes it even more likely that the person is happy
       because of receiving a raise instead of because of the weather.
'''
