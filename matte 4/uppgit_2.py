from math import*
v = pi/180
summa = 0
while v<= 179:
    v=v+1
    summa = summa + sin (v*pi/180)
    print ("summan är", summa)
