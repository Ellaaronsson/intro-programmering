import math

for n in range(1, 50000):  # testar upp till 1000, vilket räcker
    if n == sum(math.factorial(int(d)) for d in str(n)):
        print(n)