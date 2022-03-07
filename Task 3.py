import math as math
import random as random
import matplotlib.pyplot as plt

print ("Please input lambda.")
lamb = float(input())

print ("Please input the number of iterations.")
numIterations = int(input())

print("Please enter the minimum x.")
minX = float(input())

print("Please enter the max x.")
maxX = float(input())

print("Please enter delta x")
deltaX = float(input())

listOfXs = []

i = 0
while (i < numIterations):
    x = random.random()
    sample = (lamb * -1) ** -1 * (math.log(1 - x))
    listOfXs.append(sample)
    i = i + 1

j = 0
i = 0
listOfXs.sort()
sum = []
while(j < numIterations):
    if(listOfXs[i] <= minX):
        sum.append((i/numIterations))
    if(minX <= maxX):
        minX = minX + (i * deltaX)
    i = i + 1
    j = j + 1
print(sum)
