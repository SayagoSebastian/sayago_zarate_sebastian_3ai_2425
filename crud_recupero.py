immobili={
    }


def aggiungi():
    errore=True
    while errore:
        errore=False
        id_immobile=int(input("Inserisci l'id dell'immobile: "))
        if id_immobile <= 0:
            print("Id non corretto")
            errore=True
        else:
            print("Id corretto")
            id_immobile=int(id_immobile)
            indirizzo=input("Inserisci l'indirizzo: ")
            if len(indirizzo) == 0:
                print("Indirizzo non corretto")
                errore=True
            else:
                print("Indirizzo corretto")
                mq=int(input("Inserisci i mq:  max(250)"))
                if mq <= 0 or mq > 250:
                    print("Mq non validi")
                    errore=True
                else:
                    print("Mq validi")
                    prezzo=int(input("inserisci il prezzo: "))
                    if prezzo <=0:
                        print("Prezzo non valido")
                        errore=True
                    else:
                        print("Prezzo corretto")
                        n_stanze=int(input("Inserisci il numero di stanze: "))
                        if n_stanze <= 0 : 
                            print("N-stanze non valido")
                            errore=True
                        else:
                            print("N-stanze valido")
                            n_box=int(input("Inserisci il numero di box: "))
                            if n_box <0 :
                                print("N-box non valido")
                                errore=True
                            else:
                                print("N-box valido")
                                immobile={
                                    "id": id_immobile,
                                    "indirizzo": indirizzo,
                                    "mq": mq,
                                    "prezzo": prezzo,
                                    "stanze": n_stanze,
                                    "box": n_box
                                } 
                                immobili[id_immobile] = immobile
    menu()
      
def modifica():

    print("Immobili disponibili", list(immobili.keys()))
    errore=True
    while errore:
        errore=False
        id_modifica = int(input("Scrivi l'ID dell'immobile da modificare: "))
        if id_modifica not in immobili:
            print("Immobile non presente")
        else:
            immobile = immobili[id_modifica]
            indirizzo_mod=input("Inserisci l'indirizzo nuovo: ")
            if len(indirizzo_mod)==0:
                print("Indirizzo non valido")
                errore=True
            else:
                print("Indirizzo valido")
                immobile["indirizzo"]= indirizzo_mod
                mq_modifica=int(input("Inserisci i mq: "))
                if mq_modifica<=0:
                    print("Mq non validi")
                    errore=True
                else:
                    immobile["mq"]= mq_modifica
                    prezzo_modifica=int(input("Inserisci il prezzo: "))
                    if prezzo_modifica <=0:
                        print("Prezzo non valido")
                        errore=True
                    else:
                        print("Prezzo valido")
                        immobile['prezzo'] = int(prezzo_modifica)
                        n_stanze_mod=int(input("Inserisci il numero delle stanze: "))
                        if n_stanze_mod<=0:
                            print("N-stanze non valido")
                            errore=True
                        else:
                            print("n-stanze valido")
                            immobile['stanze'] = int(n_stanze_mod)                            
                            box_mod=int(input("Inserisci numero box: "))
                            if box_mod < 0:
                                print("N-box non valido")
                                errore=True
                            else:
                                print("n-box valido")
                                immobile['box'] = int(box_mod)
    menu()

def elimina():
    for id_, immobile in immobili.items():
            print(f" id_immobile: {id_}")
            print(f" indirizzo: {immobile['indirizzo']}")
            print(f" mq: {immobile['mq']} m²")
            print(f" prezzo: {immobile['prezzo']} €")
            print(f" stanze: {immobile['stanze']}")
            print(f" box: {immobile['box']}")
            print("-" * 20)
    elimina_immobile=int(input("inserisci l'id dell'immobile da eliminare: "))
    if elimina_immobile not in immobili:
        print("Immobile non presente")
    else:
        del immobili[elimina_immobile]
        print("immobile eliminato")
    menu()
def visualizza():
    if not immobili:
        print("Nessun immobile presente!")
    else:
        print("Immobili a DALMINE: ")
        for id_, immobile in immobili.items():
            print(f" id_immobile: {id_}")
            print(f" Indirizzo: {immobile['indirizzo']}")
            print(f" Mq: {immobile['mq']} m²")
            print(f" Prezzo: {immobile['prezzo']} €")
            print(f" Stanze: {immobile['stanze']}")
            print(f" Box auto: {immobile['box']}")
            print("-" * 20)
    menu()

def visualizza_mq():
    errore=True
    while errore:
        errore=False
        mq_scelti=int(input("inserisci il minimo di mq: "))
        if mq_scelti <= 0:
            print("Mq non validi")
            errore=True
        else:
            immobili_maggiori=[]
            for id_, immobile in immobili.items():
                if immobile["mq"]>= mq_scelti:
                    immobili_maggiori.append((id_,immobile))
            for i in range(len(immobili_maggiori)):
                scambio = False 
                for j in range(i + 1, len(immobili_maggiori)):
                    if immobili_maggiori[i][1]["mq"] > immobili_maggiori[j][1]["mq"]:
                        immobili_maggiori[i], immobili_maggiori[j] = immobili_maggiori[j], immobili_maggiori[i]
                        scambio = True
                if not scambio:
                    print("già in ordine")

            for id_, immobile in immobili_maggiori:
                print(f"id_immobile: {id_}")
                print(f"indirizzo: {immobile['indirizzo']}")
                print(f"mq: {immobile['mq']} m²")
                print(f"prezzo: {immobile['prezzo']} €")
                print(f"stanze: {immobile['stanze']}")
                print(f"box: {immobile['box']}")
                print("-" * 20)
    
    menu()
def visualizza_prezzo():
    prezzo_scelta=int(input("Inserisci il prezzo minimo dell'immobile: "))
    if prezzo_scelta<0:
        print("Prezzo non valido") 
    else:
        immobili_maggiori_prezzo=[]
        for id_, immobile in immobili.items():
            if immobile["prezzo"]>= prezzo_scelta:
                immobili_maggiori_prezzo.append((id_, immobile))

        print(immobili_maggiori_prezzo)

    menu()

def menu():
    print("Menu:")
    print("1- aggiungi immobile ")
    print("2- modifica immobile ")
    print("3- elimina immobile ")
    print("4- visualizza immobili ")
    print("5- visualliza in base ai mq ")
    print("6- visualizza in base al prezzo ")
    errore=True
    while errore:
        errore=False
        scelta= input("Scegli un'opzione del menu: ")
        if scelta == "1": 
            aggiungi()
        elif scelta == "2":
            modifica()
        elif scelta == "3":
            elimina()
        elif scelta == "4":
            visualizza()
        elif scelta == "5":
            visualizza_mq()
        elif scelta == "6":
            visualizza_prezzo
        

menu()