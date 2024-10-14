import random
kassa = 100
def kasta_tärning():
svar= input("vill du spela?:") 
while svar=='j':
    tärning_1=random.randint(1,6)
    tärning_2=random.randint(1,6)
    print(tärning_1, tärning_2)
    if tärning_1 == tärning_2 + 1 or tärning_1== tärning_2- 1:
        print("grattis du har vunnit, 3 kr")
    elif tärning_1==6 or tärning_2==6:
        print("grattis du har vunnit, 3 kr")
    elif tärning_1 == tärning_2:
        print("grattis du har vunnit, 5 kr")
    else:
        print("förlust")
        svar=input("vill du spela mer?:")
if svar == 'n':
    print("vad roligt att du ville spela en stund!")