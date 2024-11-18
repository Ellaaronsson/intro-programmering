import random

kassa = 3
svar = 'j'

while svar != 'n' and kassa > 0:
    svar = input("för att spela (j) och för att avsluta (n): ") 

    if svar == 'j':
        kassa -= 1

        tal_1=random.randint(0, 9)
        tal_2=random.randint(0, 9)
        tal_3=random.randint(0, 9)
        print (tal_1,tal_2, tal_3)
        tal_1 = 0
        tal_2 = 0
        tal_3 = 0
        if tal_1 == tal_2 == tal_3:
            print("vinst + 50 kr")
            kassa += 50
        elif tal_1==7 or tal_2==7 or tal_3==7:
            print("sjuvinst + 2 kr")
            kassa += 2
        elif tal_1 == tal_2 or tal_3 == tal_2 or tal_1==tal_3:
            print("mini vinst + 5kr")
            kassa += 5
        elif tal_1 == tal_2 == tal_3 == 7:
            print("dubbel vinst")
            kassa += 100
        else:
            print("förlust")

        print('Kvar att spela för: ' + str(kassa) + " kronor")
    elif svar == 'n':
        print ("tack för att du spelade, välkommen åter!")