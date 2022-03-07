import math as math
import random as random

listOfSamples = []
mu = 5
mean = 0
var = 0
lamb = 1
summationX = 0
m = 0
i = 0

while(i < 5000):
    summationX = 0
    m  = 0
    while (summationX < mu):
        x = random.random()
        sample = (lamb * -1) ** -1 * (math.log(1 - x))
        m = m + 1
        summationX = summationX + sample
    listOfSamples.append(m)
    mean = mean + m
    i = i + 1
mean = mean / 5000

j = 0
while(j < 5000):
    var = var + (listOfSamples[j] - mean) ** 2
    j = j + 1
var = var / 5000
print(mean, var)

print("The difference between the calculated mean and the actual mean of a poisson random variable is equal to ", abs(5 - mean))
print("The difference between the calculated variance and the actual variance of a poisson random variable is equal to ", abs(5 - var))

