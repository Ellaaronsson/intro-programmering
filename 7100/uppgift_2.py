import random
tal_lista = list(range(2, 100))
primtal = []
while tal_lista:
    prim=tal_lista.pop(0)
    primtal.append(prim)
    tal_lista = [tal for tal in tal_lista if tal % prim != 0]
primtal.reverse()
print(primtal)


