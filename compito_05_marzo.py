import datetime

# Funzione per la ricerca lineare migliorata
def ricerca_lineare_migliorata(lista, strumento_cercato):
    for i in range(len(lista)):
        if lista[i] == strumento_cercato:
            lista.insert(0, lista.pop(i))
            return True 
    return False

# Caricare gli strumenti musicali da un file
def carica_strumenti(nome_file):
    strumenti = []
    with open(nome_file, 'r') as file:
        for linea in file:
            strumenti.append(linea.strip())  # Aggiungi ogni strumento alla lista
    return strumenti

# Carica gli strumenti dal file
strumenti = carica_strumenti('strumenti.txt')


strumento_cercato = input("Inserisci il nome dello strumento da cercare: ").strip()

# Avvia la ricerca lineare migliorata
if ricerca_lineare_migliorata(strumenti, strumento_cercato):
    print("Lo strumento richiesto c'è")
else:
    print("Lo strumento richiesto non c'è")

