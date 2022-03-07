import math as math
import random as random

k = 0
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
    k = k + 1

