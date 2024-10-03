svar=int(input("vad är talet?"))
while svar !=42:
    if svar < 42:
        print("talet är för litet")
    if svar > 42:
        print("talet är för stort")
    svar =int(input("fel, Du får en chans till. Gissa igen."))
print("rätt")


