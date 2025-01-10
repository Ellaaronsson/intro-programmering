import random

svar = 'j'

while svar != 'n':
    svar = input("skriv j för att spela och n för att sluta: ") 
    if svar == 'j':
        tal_1=random.randint(0, 9)
        tal_2=random.randint(0, 9)
        tal_3=random.randint(0, 9)
        print (tal_1,tal_2, tal_3)
        if tal_1 == tal_2 ==tal_3:
            print("vinst")
        elif tal_1 == tal_2 or tal_3 == tal_2 or tal_1==tal_3:
         print("mini vinst")
        elif tal_1 == tal_2 == tal_3 == 7:
            print("dubbel vinst")
        else:
            print("förlust")
    elif svar == 'n':
        print ("tack för att du spelade, välkommen åter!")