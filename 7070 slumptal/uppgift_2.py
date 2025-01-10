import random
svar= input("vill du spela?:") 
while svar=='j':
    tärning_1=random.randint(1,6)
    tärning_2=random.randint(1,6)
    print(tärning_1, tärning_2)
    if tärning_1==6 and tärning_2==6:
        print("sex-vinst")
    elif tärning_1 == tärning_2:
        print("vinst")
    else:
        print("förlust")
        svar=input("vill du spela mer?:")
if svar == 'n':
    print("vad roligt att du ville spela en stund!")

