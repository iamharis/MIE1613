import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def t_mean_confidence_interval(data,alpha):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = stats.t.ppf(1-alpha/2, n-1)*se
    return m, m-h[0], m+h[0]

AllWait = []

m = 55000
d = 5000
MeanTBA = 1.0 # average interarrival time
MeanST = 0.8 # average service time

np.random.seed(1)

for Rep in range(0,10,1):
    Y = 0
    SumY = 0
    for i in range(0,d,1):
        A = np.random.exponential(MeanTBA, 1)
        # Service time distribution is Erlang-3 
        X = np.sum(np.random.exponential(MeanST/3,3))
        Y = max(0, Y + X - A)
        
    for i in range(d,m,1):
        A = np.random.exponential(MeanTBA, 1)
        X = np.sum(np.random.exponential(MeanST/3,3))
        Y = max(0, Y + X - A)
        SumY = SumY + Y
    AllWait.append(SumY/(float(m-d)))
    print (Rep+1,SumY/(float(m-d)))


print ("CI for the expected steady-state wait:", t_mean_confidence_interval(AllWait,0.05))