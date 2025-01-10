import random
tärningar = []
for i in range(10):
    tärningar.append (random.randint(1,6))
print(tärningar)
print("min", min(tärningar))
print("max", max (tärningar))
print("summa", sum(tärningar))
medel = sum (tärningar) / len(tärningar)
print("medel:", medel)
print("antal sexor", tärningar.count(6))

antal_sexor=0
for tärning in tärningar:
    if tärning == 6:
        antal_sexor = antal_sexor + 1
print("antal sexor", antal_sexor)
for tärning in tärningar:
    tärning = 7 - tärning
print(tärningar)
for i in range(len(tärningar)):
    tärningar[i]= 7 - tärningar [i]
print (tärningar)



