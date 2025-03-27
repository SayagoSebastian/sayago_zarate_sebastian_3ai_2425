import json

strumenti = {}

def salva():
    with open("strumenti.json", "w") as file:
        json.dump(strumenti, file)

def carica():
    global strumenti
    try:
        with open("strumenti.json", "r") as file:
            dati = file.read()
            if dati:
                strumenti = json.loads(dati)
                strumenti = json.loads(dati)
                strumenti = {tuple(k): v for k, v in strumenti.items()}  # Convertire le chiavi da lista a tuple
            else:
                strumenti = {}
    except Exception:
        strumenti = {}

def aggiungi_strumento():
    nome = input("Inserisci il nome dello strumento: ")
    marca = input("Inserisci la marca dello strumento: ")
    modello = input("Inserisci il modello dello strumento: ")
    
    try:
        pezzi = int(input("Inserisci il numero di pezzi disponibili: "))
        if pezzi <= 0:
            print("Numero di pezzi non valido. Riprova!")
            return
    except ValueError:
        print("Input non valido! Devi inserire un numero.")
        return
 
    chiave = (nome, marca, modello)
 
    if chiave in strumenti:
        strumenti[chiave] += pezzi
    else:
        strumenti[chiave] = pezzi
    
    salva()
    print("Strumento aggiunto/modificato con successo!")
 
def elimina_strumento():
    nome = input("Inserisci il nome dello strumento da eliminare: ")
    marca = input("Inserisci la marca dello strumento: ")
    modello = input("Inserisci il modello dello strumento: ")
 
    chiave = (nome, marca, modello)
 
    if chiave in strumenti:
        del strumenti[chiave]
        salva()
        print("Strumento eliminato!")
    else:
        print("Strumento non trovato!")
 
def visualizza_disponibilita():
    nome = input("Inserisci il nome dello strumento: ")
    marca = input("Inserisci la marca dello strumento: ")
 
    strumenti_filtrati = {}
    for k, v in strumenti.items():
        if k[0] == nome and k[1] == marca:
            strumenti_filtrati[k] = v
    
    strumenti_ordinati = sorted(strumenti_filtrati.items(), key=lambda x: x[1], reverse=True)
 
    if strumenti_ordinati:
        print(f"Disponibilità di {nome} {marca}:")
        for item in strumenti_ordinati:
            chiave, pezzi = item
            modello = chiave[2]
            print(f"Modello: {modello}, Pezzi disponibili: {pezzi}")
    else:
        print("Nessuno strumento trovato.")
 
def vendi_strumento():
    nome = input("Inserisci il nome dello strumento: ")
    marca = input("Inserisci la marca dello strumento: ")
    modello = input("Inserisci il modello dello strumento: ")
 
    chiave = (nome, marca, modello)
 
    if chiave in strumenti and strumenti[chiave] > 0:
        strumenti[chiave] -= 1
        if strumenti[chiave] == 0:
            del strumenti[chiave]
        salva()
        print("Vendita effettuata con successo!")
    else:
        print("Strumento non disponibile!")
 
def menu():
    carica()
    while True:
        print("1- Inserisci strumento")
        print("2- Visualizza disponibilità di una marca")
        print("3- Elimina strumento")
        print("4- Vendi strumento")
        print("5- Esci")
 
        scelta = input("Scegli un'opzione del menu: ")
        
        if scelta == "1":
            aggiungi_strumento()
        elif scelta == "2":
            visualizza_disponibilita()
        elif scelta == "3":
            elimina_strumento()
        elif scelta == "4":
            vendi_strumento()
        elif scelta == "5":
            print("Uscita dal programma.")
            return
        else:
            print("Scelta non valida, riprova!")
 
menu()