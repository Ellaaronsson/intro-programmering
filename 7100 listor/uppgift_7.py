import random

# Kasta fem tärningar och lägg resultaten i en lista
tärningar = []
for _ in range(5):
    tärningar.append(random.randint(1, 6))
tärningar=[4,4,4,4,4]
#skriv ut tärningar
print("tärningarna visar:", tärningar)

#kontrollera om alla tärningar visar samma värde
if tärningar.count(tärningar[0]) == len(tärningar):
    print("yatzy")
else:
    print("inte yatzy")
