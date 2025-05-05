a, b = 1, 2 
jämn_summa = 0
while a <=4000000:
    if a % 2 == 0:
        jämn_summa += a
    a, b = b, a + b
print("summan av de jämna Fibonacci-talen under 4 miljoner är:", jämn_summa)