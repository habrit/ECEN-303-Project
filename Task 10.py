import math as math
import random as random
waitTimeList = []
meanWaitTime = 0
k = 0
var = 0
while (k < 1000000):
    waitTime = 0
    muVisitsSet = 5
    muCustomersSet = 2
    lamb = 1
    summationXVisits = 0
    mVisits = 0
    mCustomers = 0

    while(summationXVisits < muVisitsSet):
        summationXCustomers = 0
        x = random.random()
        sample = (lamb * -1) ** -1 * (math.log(1 - x))
        mVisits = mVisits + 1
        summationXVisits = summationXVisits + sample
    if (mVisits != 0):
        while(summationXCustomers < muCustomersSet):
            x = random.random()
            sample = (lamb * -1) ** -1 * (math.log(1 - x))
            mCustomers = mCustomers + 1
            summationXCustomers = summationXCustomers + sample
        if (mCustomers != 0):
            j = 0
            while(j < mCustomers):
                lamb = .5
                x = random.random()
                sample = (lamb * -1) ** -1 * (math.log(1 - x))
                waitTime = waitTime + sample
                j = j + 1
    print(waitTime)
    meanWaitTime = meanWaitTime + waitTime
    waitTimeList.append(waitTime)
    k = k + 1

h = 0
meanWaitTime = meanWaitTime / 1000000
while (h < 1000000):
    var = var + (waitTimeList[h] - meanWaitTime)**2
    h = h + 1
var = var / 1000000

print(meanWaitTime, var)

print("Based off of the calculated mean and variance from the code I estimate that the mean is 6 and the variance is 20.")
