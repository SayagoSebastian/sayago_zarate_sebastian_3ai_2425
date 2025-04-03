import os
 
NOME_FILE = "dati.txt"
 
def crea_record():
    dato = input("Inserisci il testo da salvare: ")
    file = open(NOME_FILE, "a")
    file.write(dato + "\n")
    file.close()
    print("Dati salvati con successo!\n")
 
def leggi_record():
    if os.path.exists(NOME_FILE):
        file = open(NOME_FILE, "r")
        print("--- Contenuto del file ---")
        print(file.read())
        file.close()
    else:
        print("Il file non esiste ancora.\n")
 
def aggiorna_record():
    if not os.path.exists(NOME_FILE):
        print("Il file non esiste. Crea prima un record!\n")
        return
    
    file = open(NOME_FILE, "r")
    righe = file.readlines()
    file.close()
    
    leggi_record()
    indice = int(input("Inserisci il numero della riga da modificare (0-based index): "))
    if 0 <= indice < len(righe):
        nuovo_dato = input("Inserisci il nuovo testo: ")
        righe[indice] = nuovo_dato + "\n"
        file = open(NOME_FILE, "w")
        file.writelines(righe)
        file.close()
        print("Dati aggiornati con successo!\n")
    else:
        print("Indice non valido!\n")
 
def elimina_record():
    if not os.path.exists(NOME_FILE):
        print("Il file non esiste. Nulla da eliminare!\n")
        return
    
    file = open(NOME_FILE, "r")
    righe = file.readlines()
    file.close()
    
    leggi_record()
    indice = int(input("Inserisci il numero della riga da eliminare (0-based index): "))
    if 0 <= indice < len(righe):
        del righe[indice]
        file = open(NOME_FILE, "w")
        file.writelines(righe)
        file.close()
        print("Dati eliminati con successo!\n")
    else:
        print("Indice non valido!\n")
 
def menu():
    while True:
        print("\n--- CRUD con File in Python ---")
        print("1. Crea Record")
        print("2. Leggi Record")
        print("3. Aggiorna Record")
        print("4. Elimina Record")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")
        if scelta == "1":
            crea_record()
        elif scelta == "2":
            leggi_record()
        elif scelta == "3":
            aggiorna_record()
        elif scelta == "4":
            elimina_record()
        elif scelta == "5":
            print("Uscita...\n")
            break
        else:
            print("Scelta non valida! Riprova.\n")
 
menu()