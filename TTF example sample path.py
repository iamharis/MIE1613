### Generates one sample path of $S(t)$ and computes the time to failure (TTF)

import numpy as np
import matplotlib.pyplot as plt

#np.random.seed(1) # fix random number seed

# start with 2 functioning components at time 0
clock = 0
S = 2

# fix random number seed
#np.random.seed(1)

# initialize the time of events
NextRepair = float('inf')
NextFailure = np.ceil(6*np.random.random())
# lists to keep the event times and the states
EventTimes = [0]
States = [2]

while S > 0:
    # advance the time
    clock = min(NextRepair, NextFailure)
    
    if NextRepair < NextFailure:
        # next event is completion of a repair
        S = S + 1
        # a failure is still pending so no need to schedule a new one
        NextRepair = float('inf')
    else:
        # next event is a failure
        S = S - 1
        if S == 1:
            NextRepair = clock + 2.5
            NextFailure = clock + np.ceil(6*np.random.random())
    
    # save the time and state
    EventTimes.append(clock)
    States.append(S)

# plot the sample path
print ('TTF was:', clock)
plt.plot(EventTimes, States, drawstyle = 'steps-post')
# Set labels of the plot
plt.xlabel('t')
plt.ylabel('S(t)')
plt.show()



