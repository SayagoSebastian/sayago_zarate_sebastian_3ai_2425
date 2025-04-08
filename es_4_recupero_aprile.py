immobili = []

def aggiungi_immobile():
    id = int(input("Inserisci l'ID dell'immobile: "))
    citta = input("Inserisci la città dell'immobile: ")
    metri_quadri = int(input("Inserisci i metri quadri dell'immobile: "))
    prezzo = float(input("Inserisci il prezzo dell'immobile: "))
    
    immobile = {"id": id, "citta": citta, "metri_quadri": metri_quadri, "prezzo": prezzo}
    immobili.append(immobile)
    print(f"Immobile con ID {id} aggiunto con successo!\n")

def rimuovi_immobile(id):
    global immobili
    nuovi_immobili = []
    for im in immobili:
        if im["id"] != id:
            nuovi_immobili.append(im)
    immobili = nuovi_immobili

def modifica_immobile(id, nuovi_dati):
    for im in immobili:
        if im["id"] == id:
            if "citta" in nuovi_dati:
                im["citta"] = nuovi_dati["citta"]
            if "metri_quadri" in nuovi_dati:
                im["metri_quadri"] = nuovi_dati["metri_quadri"]
            if "prezzo" in nuovi_dati:
                im["prezzo"] = nuovi_dati["prezzo"]
            break


def visualizza_immobili():
    if immobili:
        for im in immobili:
            print(f"ID: {im['id']}, Città: {im['citta']}, MQ: {im['metri_quadri']}, Prezzo: {im['prezzo']}")
    else:
        print("Nessun immobile presente.\n")

def ordina_immobili():  #ordinmaento imm
    for i in range(len(immobili)):
        for j in range(i + 1, len(immobili)):
            if (immobili[i]["metri_quadri"] > immobili[j]["metri_quadri"]) or \
               (immobili[i]["metri_quadri"] == immobili[j]["metri_quadri"] and immobili[i]["prezzo"] > immobili[j]["prezzo"]):
                
                immobili[i], immobili[j] = immobili[j], immobili[i]


def filtra_per_mq(min_mq): #in base ai metri quadri
    risultati = []
    for imm in immobili:
        if imm["metri_quadri"] > min_mq:
            risultati.append(imm)
    return risultati


def filtra_per_prezzo(minimo_prez, massimo_prez):
    risultati = []
    for imm in immobili:
        if imm["prezzo"] >= minimo_prez and imm["prezzo"] <= massimo_prez:
            risultati.append(imm)
    return risultati


def menu():
    while True:
        print("\nGestione Immobili")
        print("1. Aggiungi immobile")
        print("2. Visualizza immobili")
        print("3. Ordina immobili")
        print("4. Filtra immobili per metri quadri")
        print("5. Filtra immobili per prezzo")
        print("6. Esci")
        
        scelta = input("Scegli un'opzione (1-6): ")
        
        if scelta == '1':
            aggiungi_immobile()
        elif scelta == '2':
            print("\nElenco immobili:")
            visualizza_immobili()
        elif scelta == '3':
            ordina_immobili()
            print("\nImmobili ordinati.")
        elif scelta == '4':
            min_mq = int(input("Inserisci il numero minimo di metri quadri: "))
            risultati = filtra_per_mq(min_mq)
            if risultati:
                print("\nImmobili trovati con più di", min_mq, "metri quadri:")
                for imm in risultati:
                    print(imm)
            else:
                print(f"\nNessun immobile trovato con più di {min_mq} metri quadri.")
        elif scelta == '5':
            minimo_prez = float(input("Inserisci il prezzo minimo: "))
            massimo_prez= float(input("Inserisci il prezzo massimo: "))
            risultati = filtra_per_prezzo(minimo_prez, massimo_prez)
            if risultati:
                print(f"\nImmobili trovati con prezzo tra {minimo_prez} e {massimo_prez}:")
                for imm in risultati:
                    print(imm)
            else:
                print(f"\nNessun immobile trovato con prezzo tra {minimo_prez} e {massimo_prez}.")
        elif scelta == '6':
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")


menu()
