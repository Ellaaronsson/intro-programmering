import random
svar = input("vill du spela? j/n:")
while svar == 'j':
    tärning_1 = random.randint(1,6) 
    tärning_2 = random.randint(1,6)
    print(tärning_1, tärning_2)
    if tärning_1 == tärning_2:
        print("vinst")
    else:
        print ("förlust")
    svar = input("vill du spela mer? j/n:")
if svar == 'n':
    print("Vad roligt att du spelade en stund!")
   

