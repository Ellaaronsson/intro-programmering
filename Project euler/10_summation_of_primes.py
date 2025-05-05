def summa_primtal(limit): 
    primtal = [True] * limit 
    primtal[0] = primtal[1] = False 

    for i in range(2, int(limit**0.5) + 1): 
        if primtal[i]: 
            for j in range(i * i, limit, i): 
                primtal[j] = False 

    return sum(i for i in range(limit) if primtal[i]) 

resultat = summa_primtal(2000000) 
print("Summan av alla primtal under två miljoner är:", resultat) 

 