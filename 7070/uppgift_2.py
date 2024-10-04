import random
svar= input("vill du spela?:") 
while svar=='j':
    tärning_1=random.randint(1,6)
    tärning_2=random.randint(1,6)
    print("träning_1, tärning_2")
    if tärning_1==6 or tärning_2==6:
        print("vinst")
        else:
        print("förlust")
        svar=input("vill du spela mer?:")
if svar == 'n':
    print("vad roligt att du ville spela en stund!")

