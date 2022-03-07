import math as math
import random as random

print("Please enter a positive scalar mu.")

mu = float(input())

lamb = 1
summationX = 0
m = 0

while(summationX < mu):
    x = random.random()
    sample = (lamb * -1) ** -1 * (math.log(1 - x))
    m = m + 1
    summationX = summationX + sample



print(m)

