import random as random
import math as math

print ("Please enter a positive scalar lambda.")
lamb = float(input())

print("Please enter the number of iterations.")
numIterations = int(input())
abovefif = 0
i = 0
while (i < numIterations):
    x = random.random()
    sample = (lamb * -1) ** -1 * (math.log(1 - x))
    i = i + 1
    print(sample)
