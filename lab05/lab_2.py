'''
This module implements the Bayesian network for Thrun's 2-test cancer example.

@author: kvlinden
@version Jan 2, 2013
@student: Sarah Whitten, March 8 2020
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# from figure in Exercise 5.2
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2})
])

print()

# Exercise 5.2
# i. P(Cancer | Test1, Test2)
print("a. ", enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())
# ii. P(Cancer | Test1, ¬Test2)
print("b. ", enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
I wasn't really that surprised that the probability of the patient having cancer given both tests came back positive
was as low it was because of the small likelihood of the patient having cancer in the first place. When I first got
the probability results I was surprised but then remembered that P(Cancer)=0.01, and then the result seemed reasonable.
I'm also not surprised by how low the probability is of the patient having cancer when one of the tests is negative
and the other is positive, because the outcome of one test strongly affects the probability of having cancer. 

Work by hand:
a) P(Cancer | Test1, Test2) = ɑ P(Cancer, Test1, Test2)
                            = ɑ P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer)
                            = ɑ < P(Cancer) * P(Test1 | Cancer) * P(Test2 | Cancer), 
                                  P(¬Cancer) * P(Test1 | ¬Cancer) * P(Test2 | ¬Cancer) >
                            = ɑ < 0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2 >
                            = ɑ < 0.0081, 0.0396 >
                            = < 0.17, 0.83 >
b) P(Cancer | Test1, ¬Test2) = ɑ P(Cancer, Test1, ¬Test2)
                             = ɑ P(Cancer) * P(Test1 | Cancer) * P(¬Test2 | Cancer)
                             = ɑ < P(Cancer) * P(Test1 | Cancer) * P(¬Test2 | Cancer),
                                   P(¬Cancer) * P(Test1 | ¬Cancer) * P(¬Test2 | ¬Cancer) >
                             = ɑ < 0.01 * 0.9 * 0.1, 0.99 * 0.8 * 0.2 >
                             = ɑ < 0.0009, 0.1584 >
                             = < 0.00565, 0.994 >
'''
