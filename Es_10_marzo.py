manga_lista = []
 

def inserisci_manga():
    titolo = input("Titolo del manga: ")
    autore = input("Autore: ")
    casa_editrice = input("Casa editrice: ")
    
    completo = input("Il manga è completo? (s/n): ").strip().lower()
    
    errore = True
    volumi = -1  # Se il manga è incompleto, i volumi restano -1
    if completo == 's':
        while errore:
            errore = False
            try:
                volumi = int(input("Numero di volumi: "))
            except ValueError:
                print("Errore! Inserisci un numero valido.")
                errore = True
 
    manga = {
        "titolo": titolo,
        "autore": autore,
        "casa_editrice": casa_editrice,
        "volumi": volumi,
        "completo": completo == 's'
    }
    
    manga_lista.append(manga)
    print("Manga aggiunto!\n")
 
def ordina_manga(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1):
            if lista[j]["volumi"] < lista[j + 1]["volumi"] or lista[j + 1]["volumi"] == -1:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
 
def mostra_tutti():
    if not manga_lista:
        print("Nessun manga in lista.\n")
        return
    
    ordina_manga(manga_lista)
 
    for manga in manga_lista:
        volumi = "Sconosciuto" if manga["volumi"] == -1 else manga["volumi"]
        print(f"{manga['titolo']} di {manga['autore']} ({manga['casa_editrice']}) - Volumi: {volumi}")
 
def mostra_per_autore():
    autore = input("Inserisci l'autore: ")
    trovati = []
    
    for m in manga_lista:
        if m["autore"].lower() == autore.lower():
            trovati.append(m)
 
    if not trovati:
        print(f"Nessun manga trovato per {autore}.\n")
        return
 
    ordina_manga(trovati)
 
    for manga in trovati:
        volumi = "Sconosciuto" if manga["volumi"] == -1 else manga["volumi"]
        print(f"{manga['titolo']} - Volumi: {volumi}")
 
def mostra_maggiori_di():
    errore = True
    while errore:
        errore = False
        try:
            x = int(input("Numero minimo di volumi: "))
        except ValueError:
            print("Errore! Inserisci un numero valido.\n")
            errore = True
 
    trovati = []
    for m in manga_lista:
        if m["volumi"] > x:
            trovati.append(m)
 
    if not trovati:
        print(f"Nessun manga con più di {x} volumi.\n")
        return
 
    ordina_manga(trovati)
 
    for manga in trovati:
        print(f"{manga['titolo']} - Volumi: {manga['volumi']}")
 
def conta_autore():
    autore = input("Inserisci l'autore: ")
    num_manga = 0
    tot_volumi = 0
 
    for m in manga_lista:
        if m["autore"].lower() == autore.lower():
            num_manga += 1
            if m["volumi"] != -1:
                tot_volumi += m["volumi"]
 
    if num_manga == 0:
        print(f"Nessun manga trovato per {autore}.\n")
        return
 
    print(f"{autore} ha scritto {num_manga} manga con {tot_volumi} volumi in totale.\n")
 
# Menu 
def menu():
    while True:
        print("\n1) Aggiungi un manga")
        print("2) Mostra tutti i manga")
        print("3) Mostra manga di un autore")
        print("4) Mostra manga con più di X volumi")
        print("5) Conta manga e volumi di un autore")
        print("6) Esci")
 
        scelta = input("Scegli un'opzione: ")
        print()
 
        if scelta == "1":
            inserisci_manga()
        elif scelta == "2":
            mostra_tutti()
        elif scelta == "3":
            mostra_per_autore()
        elif scelta == "4":
            mostra_maggiori_di()
        elif scelta == "5":
            conta_autore()
        elif scelta == "6":
            print("Ciao!")
            break
        else:
            print("Scelta non valida!\n")
 

menu()