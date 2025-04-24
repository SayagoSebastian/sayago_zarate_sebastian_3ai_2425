#carico il file e metto i dati in una lista di tuple
def carica():
    datiInput = []
    file = open("input2.txt", "r", encoding="UTF-8")
    for riga in file:
        riga = riga[0:len(riga)-1]
        parti=riga.split("-")
        nome = parti[0]
        razza = parti[1]
        data = parti[2]
        adottato = parti[3].strip()
        datiInput.append((nome, razza, data, adottato))
    file.close()
    return datiInput

def stampaAnimaliNonAdottati(l):
    print("Animali non adottati: ")
    for i, animale in enumerate(l):
        if animale[3] == "N":
            print(f"{i+1} - {animale[0]} {animale[1]} {animale[2]}")

#ordino usando il bubble sort
def bubblesort(l):
    for j in range(0, len(l)-1):
        for i in range(0, len(l)-1):
            if l[i][1].lower()>l[i+1][1].lower():
                l[i], l[i+1] = l[i+1], l[i]
            elif l[i][1].lower()==l[i+1][1].lower():
                if l[i][0].lower()>l[i+1][0].lower():
                    l[i], l[i+1] = l[i+1], l[i]    

#salvo sul file
def salva(l):
    file = open("input2.txt", "w")
    for animale in l:
        riga = animale[0]+"-"+animale[1]+"-"+animale[2]+"-"+animale[3]+"\n"
        file.write(riga)
    file.close()

def adotta(l):
    errore = True
    while errore==True:
        errore = False
        try:
            posizione = int(input("Inserisci l'indice dell'animale da adottare "))
            if posizione < 1 or posizione > len(l):
                print("Posizione non valida")
                errore = True
            elif l[posizione-1][3] == "S":
                print("Animale gia adottato, scegline un altro")
                errore = True
        except:
            print("Formato posizione non valido")
            errore = True
    tupla = (l[posizione-1][0], l[posizione-1][1], l[posizione-1][2], "S")
    l[posizione-1] = tupla

Lista = carica()
stampaAnimaliNonAdottati(Lista)
adotta(Lista)
salva(Lista)

#bubblesort(Lista)
#salva(Lista)
