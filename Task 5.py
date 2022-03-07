import random as random
import math as math


lamb = .5
numIterations = 100
i = 0
sample1 = []
sum = 0
var = 0
while (i < numIterations):
    x = random.random()
    sample = (lamb * -1) ** -1 * (math.log(1 - x))
    i = i + 1
    sample1.append(sample)
    sum = sum + sample

sum = sum / numIterations
i = 0
while (i < numIterations ):
    var = var + (sample1[i] - sum) ** 2
    i = i + 1

var = var / numIterations
print("The mean of the sample with n = 100 is:" , sum, " and the variance is: ", var)





lamb = .5
numIterations = 5000
i = 0
sample1 = []
sum = 0
var = 0
while (i < numIterations):
    x = random.random()
    sample = (lamb * -1) ** -1 * (math.log(1 - x))
    i = i + 1
    sample1.append(sample)
    sum = sum + sample

sum = sum / numIterations
i = 0
while (i < numIterations ):
    var = var + (sample1[i] - sum) ** 2
    i = i + 1

var = var / numIterations
print("The mean of the sample with n = 5000 is:" , sum, " and the variance is: ", var)
