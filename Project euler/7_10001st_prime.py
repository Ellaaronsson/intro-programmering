def är_primtal(n):
    #kontrollera om n är ett primtal
    if n < 2:
        return False 
    for i in range(2, int(n ** 0.5) + 1): #testa alla tal upp till roten av n
        if n % i == 0:
            return False
    return True
def hitta_nte_primtal(n):
    #Hittar det n:te primtalet
    antal_primtal = 0
    nummer = 1 # nummer håller reda på vilket tal vi just nu undersöker för att se om det är ett primtal
    while antal_primtal < n:
        nummer +=1
        if är_primtal(nummer):
            antal_primtal += 1
    return nummer
nte_primtal = hitta_nte_primtal (10001)
print("Det 10001:a primtalet är" + str(nte_primtal)) #f-string för att kunna infoga variabler i strängarprint(f"Det 10001:a primtalet är {nte_primtal}") 
