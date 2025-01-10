import random
def rovarsprak (ord):
    vokaler="aeiouyåäö"
    översatt = ""

    for konsonant in ord:
        if konsonant.lower() not in vokaler:
            översatt += ord + 'o' + ord.lower()