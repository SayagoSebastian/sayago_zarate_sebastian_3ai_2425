def ricercaLineareBase(lista, numDaCercare):
    for numero in lista:
        if numero == numDaCercare:
            return True
    return False
 

def ricercaLineareMigliorata(lista, numDaCercare):
    for numero in lista:
        if numero == numDaCercare:
            return True
        elif numero > numDaCercare:
            break  
    return False
 

lista = [1, 3, 5, 7, 9, 11, 13]
 

print("Ricerca Lineare Base:")
print(ricercaLineareBase(lista, 5))  
 

print("Ricerca Lineare Migliorata:")
print(ricercaLineareMigliorata(lista, 5))  
print(ricercaLineareMigliorata(lista, 4))  