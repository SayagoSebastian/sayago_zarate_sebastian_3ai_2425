import os

# Lista globale per memorizzare i libri
libri = []

# Funzione per aggiungere un libro alla collezione
def aggiungi_libro(titolo):
    if titolo in libri:
        print(f"Errore: il libro '{titolo}' è già presente nella collezione.")
    else:
        libri.append(titolo)
        print(f"Il libro '{titolo}' è stato aggiunto alla collezione.")

# Funzione per modificare un titolo
def modifica_libro(vecchio_titolo, nuovo_titolo):
    if vecchio_titolo not in libri:
        print(f"Errore: il libro '{vecchio_titolo}' non è nella collezione.")
    elif nuovo_titolo in libri:
        print(f"Errore: il libro '{nuovo_titolo}' è già presente nella collezione.")
    else:
        indice = libri.index(vecchio_titolo)
        libri[indice] = nuovo_titolo
        print(f"Il libro '{vecchio_titolo}' è stato modificato in '{nuovo_titolo}'.")

# Funzione per eliminare un libro
def elimina_libro(titolo):
    if titolo not in libri:
        print(f"Errore: il libro '{titolo}' non è nella collezione.")
    else:
        libri.remove(titolo)
        print(f"Il libro '{titolo}' è stato rimosso dalla collezione.")

# Funzione per visualizzare tutti i libri ordinati alfabeticamente
def visualizza_libri():
    if not libri:
        print("La collezione è vuota.")
    else:
        libri.sort()
        print("Lista dei libri:")
        for libro in libri:
            print(libro)

# Funzione per cercare un libro
def cerca_libro(titolo):
    if titolo in libri:
        print(f"Il libro '{titolo}' è nella collezione.")
    else:
        print(f"Il libro '{titolo}' non è nella collezione.")

# Funzione per caricare i dati da un file
def carica_dati():
    global libri
    if os.path.exists("collezione_libri.txt"):
        with open("collezione_libri.txt", "r") as file:
            libri = file.read().splitlines()
        print("Dati caricati con successo.")
    else:
        print("Nessun dato da caricare (file non trovato).")

# Funzione per salvare i dati su un file
def salva_dati():
    with open("collezione_libri.txt", "w") as file:
        for libro in libri:
            file.write(libro + "\n")
    print("Dati salvati con successo.")

# Funzione per visualizzare il menu e scegliere l'operazione
def menu():
    errore = True
    while errore:
        errore = False
        print("\nBenvenuto nel software di gestione dei libri!")
        print("1) Aggiungi un nuovo titolo")
        print("2) Modifica un titolo")
        print("3) Elimina un titolo")
        print("4) Visualizza tutti i titoli")
        print("5) Cerca un titolo")
        print("6) Carica i dati da file")
        print("7) Salva i dati su file")
        print("8) Esci")

        scelta = input("Scegli un'operazione (1-8): ")

        if scelta == '1':
            titolo = input("Inserisci il titolo del libro da aggiungere: ")
            aggiungi_libro(titolo)
        elif scelta == '2':
            vecchio_titolo = input("Inserisci il titolo da modificare: ")
            nuovo_titolo = input("Inserisci il nuovo titolo: ")
            modifica_libro(vecchio_titolo, nuovo_titolo)
        elif scelta == '3':
            titolo = input("Inserisci il titolo da eliminare: ")
            elimina_libro(titolo)
        elif scelta == '4':
            visualizza_libri()
        elif scelta == '5':
            titolo = input("Inserisci il titolo da cercare: ")
            cerca_libro(titolo)
        elif scelta == '6':
            carica_dati()
        elif scelta == '7':
            salva_dati()
        elif scelta == '8':
            print("Uscita dal programma...")
            errore = False
        else:
            print("Scelta non valida. Riprova.")
            errore = True

# Avvio del programma
menu()