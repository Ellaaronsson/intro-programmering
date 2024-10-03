tal_1 = float(input("Ange ett tal: "))
tal_2 = float(input("Ange ett andra tal: "))
tal_3 = float(input("Ange ett tredje tal: "))
if tal_1 < tal_2 and tal_1 < tal_3:
    print(tal_1, "är minst")
elif tal_2 < tal_1 and tal_2 < tal_3:
    print(tal_2, "är minst")
elif tal_3 < tal_1 and tal_3 < tal_2:
    print(tal_3, "är minst")
    
