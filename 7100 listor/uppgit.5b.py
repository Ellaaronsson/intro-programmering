import random
# kasta fem tärningar
tärningar = [random.randint(1,6) for _ in range(5)]
print("tärningarna visar: ",tärningar)
# alla tärningar är samma kontroll
if all(i == tärningar[0]for i in tärningar):
    print("Yatzy")
else:
    print("inte yatzy")
