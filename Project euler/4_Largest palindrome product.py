def is_palindrome(tal):
    # tal är en string
    # sista indexet -1
    for i in range(len(tal) // 2):
    # från slutet dvs -1, -2, ....
        j=i* -1 -1 # i framifrån, j bakifrån -(i+1)
        if tal[i] == tal[j]:
            #allt är bra
            None
        else:
            return False
    return True

mina_palindrom=[] #sparar palindrom här
for tal_1 in range(100,1000):
    for tal_2 in range(100,1000):
        tal = tal_1*tal_2
        # är palindrom?
        text = str(tal)
        if is_palindrome(text):
            mina_palindrom.append(tal)
print(max(mina_palindrom))

