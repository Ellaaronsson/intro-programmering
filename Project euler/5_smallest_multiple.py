def multiple():
    tal = 20
    while True:
        if all(tal % i == 0 for i in range (1,21)):
            return tal
        tal += 20
resultat = multiple()
print("Det minsta talet som är delbart med alla tal 1 till 20 år:", resultat)


