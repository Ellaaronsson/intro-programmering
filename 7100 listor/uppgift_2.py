import random
#lägg talen 2-100 i tal_lista
tal_lista = list(range(2, 100))
#primtal är tom lista
primtal = []
#om tal_lista inte är tom lägg sista talet i tal_lista i primtal
while tal_lista: 
    prim=tal_lista.pop(0)
    primtal.append(prim)
    #lägg till index här
    #är indexet större än ett är tal_lista[i] delbat med sista talet i listan primtal
    tal_lista = [tal for tal in tal_lista if tal % prim !=0]
print(primtal)


