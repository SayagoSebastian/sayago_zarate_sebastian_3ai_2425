case_in_vendita = []


def aggiungi_casa():
    errore = True
    while errore:
        errore = False  

        id = input("Inserisci ID univoco: ")
        if not id.isdigit():
            print("numero intero non valido.")
            errore = True
        else:
            id = int(id)
    while errore:
        errore = False     
        indirizzo = input("Inserisci l'indirizzo della casa: ")
        
        metri_quadri = input("Inserisci i metri quadri: ")
        if not metri_quadri.isdigit():
            print("numero intero non valido.")
            errore = True
        else:
            metri_quadri = int(metri_quadri)
    while errore:
        errore = False 
        prezzo = input("Inserisci il prezzo di vendita: ")
        if not prezzo.replace('.', '', 1).isdigit():
            print("numero intero non valido.")
            errore = True
        else:
            prezzo = float(prezzo)
    while errore:
        errore = False 
        numero_stanze = input("Inserisci il numero di stanze: ")
        if not numero_stanze.isdigit():
            print("numero intero non valido.")
            errore = True
        else:
            numero_stanze = int(numero_stanze)
    while errore:
        errore = False 
        numero_box = input("Inserisci il numero di box (0 se non ci sono): ")
        if not numero_box.isdigit():
            print("numero non valido")
            errore = True
        else:
            numero_box = int(numero_box)

        casa = {
            "id": id,
            "indirizzo": indirizzo,
            "metri_quadri": metri_quadri,
            "prezzo": prezzo,
            "numero_stanze": numero_stanze,
            "numero_box": numero_box
        }
        case_in_vendita.append(casa)
        print("Casa aggiunta con successo!\n")

errore=True
while errore:
    errore=False
    numero_case = input("Quante case vuoi mettere?")
    if numero_case.isdigit():
        numero_case = int(numero_case)
        errore=False
    else:
        print("numero non valido")
        errore=True

for _ in range(numero_case):
    aggiungi_casa()

print("\nElenco delle case in vendita:")
for casa in case_in_vendita:
    print(casa)