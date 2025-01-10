import random
tärningar = [random.randint(1,6) for _ in range(5)]
tärningar = [5,5,5,5,5]
print("tärningskast",tärningar )
if all(tärning == tärningar[0] for tärning in tärningar):
    print("yatzy")
else:
    print("inte yatzy")