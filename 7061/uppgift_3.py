gissningar=0
gissningar=gissningar+1
tal=int(input("mata in ett tal:"))

while svar !=42 and gissningar > 3:
    gissningar=gissningar+1
    if svar < 42:
        print("talet är för litet")
    elif svar > 42:
        print("talet är för stort")
    svar =int(input("fel, Du får en chans till. Gissa igen."))