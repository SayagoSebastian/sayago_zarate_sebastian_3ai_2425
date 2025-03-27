import os 
import datetime


pacchetti=[
    {"nome": "parigi", 
    "prezzo": 500,
     "inizio": "3/05/2025", 
     "fine": "10/05/2025", 
     "posti": 10},

    {'nome':'londra', 
    'prezzo':520, 
    'inizio':'11/05/2025', 
    'fine':'16/05/2025', 
    'posti':2},

    {'nome':'barcellona', 
    'prezzo':380, 
    'inizio':'13/06/2025', 
    'fine':'15/06/2025', 
    'posti':12},

    {'nome':'amsterdam', 
    'prezzo':650, 
    'inizio':'14/04/2025', 
    'fine':'19/04/2025', 
    'posti':5},

    {'nome':'amsterdam', 
    'prezzo':600, 
    'inizio':'25/05/2025', 
    'fine':'1/06/2025', 
    'posti':8}

]

def aggiungi():
    errore=True
    while errore:
        errore=False
        print(pacchetti)
        destinazione=input("Inserisci la destinazione ")
        if len(destinazione)<=0:
            print("Destinazione non valida")
            errore=True
        else:
            print("destinazione valida")
    errore=True
    while errore:
        errore=False
        prezzo_1=float(input("Inserisci il prezzo "))
        if prezzo > 0:
            print("Prezzo non può essere negativo")
            errore=True
        else:
            print("Prezzo accetabile")
            prezzo=float(prezzo_1)
        errore=True
        while errore:
            errore=False
            inizio=input("Inserisci la data di inizio: (DD/MM/YYYY) ")
            if inizio < datetime.now():
                print("data non corretta")
                errore=True
            else:
                print("data  corretta")
        errore=True
        while errore:
            errore=False       
            fine=input("Inserisci la data della fine: (DD/MM/YYYY) ")
            if fine < datetime.now():
                print("data non corretta")
                errore=True
            else:
                print("data non corretta")  
        errore=True 
        while errore:
            errore=False    
            posti_1=int(input("Inserisci i posti disponibili: "))
            if posti > 0:
                print("Posti corretti ")
                posti=int(posti_1)
            else:
                print("Posti non validi")
                errore=True
        
        pacchetto_nuovo={
            "nome": {destinazione},
            "prezzo": {prezzo_1},
            "inizio": {inizio},
            "fine": {fine},
            "posti": {posti_1}
        }
        pacchetto_nuovo=list()
        pacchetti.append(pacchetto_nuovo)
        
    menu()

def visualizza():
    print(pacchetti)

    menu()

def modifica():
    errore=True
    while errore:
        errore=False
        scegli_nome=input("Inserisci il nome della destinazione: ")
        if scegli_nome not in pacchetti:
            print("Destinazione non presente")
            errore=True
        else:
            print("destinazione presente")
    while errore:
        errore=False
        scegli_prezzo=input("Cosa vuoi modificare? (prezzo)")
        if scegli_prezzo == "prezzo":
            cambia_prezzo=float(input("Scegli il prezzo nuovo: "))
            if cambia_prezzo > 0:
                print("prezzo valido")
                for i in pacchetti:
                    if nome == scegli_nome:
                        if prezzo == scegli_prezzo:
                            pacchetti[scegli_nome][scegli_prezzo] = cambia_prezzo
        else:
            print("Errore. riprova")
            errore=True
    menu()
        
                    

def visualizza_2():
    errore=True
    while errore:
        errore=False
        pacchetti=dict()
        scelta_nome=input("Scegli il nome della destinazione: ")
        if len(scelta_nome)<=0:
            print("nome non valido")
            errore=True
        else:
            for i in pacchetti:
                if scelta_nome == i[nome]:
                    print("destinazione presente")
                else:
                    print("Destinazione non presente")
    
    menu()


def menu():
    print("1- aggiungi offerta di viaggio ")
    print("2- visualliza l'elenco dei pacchetti disponibili ")
    print("3- modifica il prezzo di un pacchetto ")
    print("4- visualliza l'elenco dei pacchetti data una destinazione")
    print("5- esci")

    errore=True
    while errore:
        errore=False
        scelta=input("Scegli un'opzione del menu: ")
        if scelta == "1":
            aggiungi()
        elif scelta == "2":
            visualizza()
        elif scelta == "3":
            modifica()
        elif scelta == "4":
            visualizza_2()
        elif scelta == "5":
            errore=False
        else:
            print("scelta non valida")
            errore=True
menu()