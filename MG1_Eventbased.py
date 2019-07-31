# Event-based simulation of the M/G/1 queue

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def t_mean_confidence_interval(data,alpha):
    a = 1.0*np.array(data)
    n = len(a)
    m, se = np.mean(a), stats.sem(a)
    h = stats.t.ppf(1-alpha/2, n-1)*se
    return m, m-h, m+h

# Input parameters
MeanST = 0.8
MeanTBA = 1.0
RunTime = 50000
Warmup = 5000
n = 10

def EndSim():
    global Area
    Area = Area + Slast * (clock - Tlast)
    
def ClearSim():
    global Area
    global Tlast
    global NextClearSim

    Area = 0
    Tlast = clock
    NextClearSim = float('inf')
    

def Arrival():
    global X
    global Slast
    global Tlast
    global Area
    global NextArrival
    global NextDeparture

    X += 1
    NextArrival = clock + np.random.exponential(MeanTBA)
    if X == 1:
        NextDeparture = clock + np.sum(np.random.exponential(MeanST/3,3))
    Area = Area + Slast * (clock - Tlast)
    Slast = X
    Tlast = clock

def Departure():
    global X
    global Slast
    global Tlast
    global Area
    global NextDeparture

    X -= 1
    if X > 0:
        NextDeparture = clock + np.sum(np.random.exponential(MeanST/3,3))
    else:
        NextDeparture = float('inf')
    Area = Area + Slast * (clock - Tlast)
    Slast = X
    Tlast = clock

def Timer():
    global clock

    if NextEndSim < min(NextArrival, NextDeparture):
        result = "End"
        clock = NextEndSim
        
    elif NextClearSim < min(NextArrival, NextDeparture):
        result = "Clear"
        clock = NextClearSim

    elif NextArrival < NextDeparture:
        result = "Arrival"
        clock = NextArrival
    else:
        result = "Departure"
        clock = NextDeparture
    return result 


np.random.seed(1)
# list to keep samples of the time averages across replications
Avelist = [] 
print ("Rep", "Average Num. in System")

# Replication loop
for reps in range(n):
    # initialize clock, state, and next events
    clock = 0
    X = 0
    NextArrival = np.random.exponential(MeanTBA)
    NextDeparture = float('inf')
    NextEndSim = RunTime
    NextClearSim = Warmup

    Slast = X
    Tlast = clock
    Area = 0

    while clock < RunTime: 
        NextEvent = Timer()

        if NextEvent == "Arrival":
            Arrival()
        elif NextEvent == "Departure":
            Departure()
        elif NextEvent == "Clear":
            ClearSim()
        else:
            EndSim()
    # add samples to the lists
    print (reps+1,Area/(clock-Warmup))
    Avelist.append(Area/(clock-Warmup))

# print the estimate and a 95% confidence interval
# for the expected time-average
print ("CI for expected ave. # of customers in system:",
       t_mean_confidence_interval(Avelist,0.05))