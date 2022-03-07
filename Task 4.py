import math as math
import random as random
import matplotlib.pyplot as plt
import numpy as np


lamb = .5


numIterations = 100

minX = 0


maxX = 15


deltaX = .01

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
xaxisValues1 = []
yaxisvalues1 = []
sum = []
while(j < numIterations):
    if((listOfXs[j] <= minX) & (minX <= maxX)):
        sum.append((i/numIterations))
        xaxisValues1.append(minX)
        i = i + 1
    if(minX <= maxX):
        minX = minX + (i * deltaX)
        i = i + 1
    j = j + 1


plt.plot(xaxisValues1, sum, label = "n = 100")

lamb = .5

numIterations = 5000

minX = 0


maxX = 15


deltaX = .01

listOfX1s = []
i = 0
while (i < numIterations):
    x = random.random()
    sample = (lamb * -1) ** -1 * (math.log(1 - x))
    listOfX1s.append(sample)
    i = i + 1

j = 0
i = 0
listOfX1s.sort()
xaxisValues = []
sum1 = []
while(j < numIterations):
    if((listOfX1s[j] <= minX) & (minX <= maxX)):
        sum1.append((j/numIterations))
        xaxisValues.append(minX)
        i = i + 1
    if(minX <= maxX):
        minX = minX + (deltaX)

        i = i + 1
    j = j + 1
plt.plot(xaxisValues, sum1, label = "n = 5000")
k = 0

xCDFValues = []
y = []
while (k < 15):
    y.append((1 - math.exp(-1 * .5 * k)))
    xCDFValues.append(k)
    k = k + .01

plt.plot(xCDFValues,y, label = "CDF of exponential")
plt.legend()
plt.show()
