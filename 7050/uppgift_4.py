tal = int(input("mata in ett tal:" ))
if tal >= 0 and tal <= 9:
    print("talet är ensiffrigt tal")
elif tal >= 10 and tal <= 99:
    print("är tvåsiffrigt tal")
elif tal >= 100 and tal <= 999:
    print("talet är tresiffrigt tal")
else: 
    print("talet är minst fyrsiffriga tal")


