# -*- coding: utf-8 -*-
"""
Converted from VBASim by
Yujing Lin, Linda Pei & Barry L Nelson
Last update 8/15/2018
"""

import SimRNG
import math
import matplotlib.pyplot as plt
 
ZRNG = SimRNG.InitializeRNSeed()

N = 1000
c = 0
tp = 5
Y_list = []
for rep in range(0,N,1):
    X = []
    for i in range(0,tp,1):
        X.append(SimRNG.Expon(1.0,7))
    Y = max(X[0] + X[3], X[0] + X[2] + X[4], X[1] + X[4])
    Y_list.append(Y)
    if Y > tp:
        c = c + 1
Theta_hat = float(c)/N
Theta = 1- ((tp ** 2 / 2.0 - 3 * tp - 3) * math.exp(-2 * tp) + (-tp ** 2 / 2.0 - 3 * tp + 3) * math.exp(-tp) + 1 - math.exp(-3 * tp))        

print("Exact probability:", Theta)
print("Estimated probability:", Theta_hat, "+/-", 1.96*math.sqrt((Theta_hat*(1-Theta_hat))/N))

plt.hist(Y_list, bins=25, cumulative = True,
                label = "Project duration")
plt.xlabel("Project duration")
plt.ylabel("Frequency")
plt.show()