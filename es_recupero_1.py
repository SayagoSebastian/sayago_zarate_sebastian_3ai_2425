#carico il file e metto i dati in una lista di tuple
def carica():
    datiInput = []
    file = open("input.txt", "r", encoding="UTF-8")
    for riga in file:
        riga = riga[0:len(riga)-1]
        parti=riga.split("-")
        nome = parti[0]
        razza = parti[1]
        data = parti[2]
        datiInput.append((nome, razza, data))
    file.close()
    return datiInput
    


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
    file = open("ouput.txt", "w")
    for animale in l:
        riga = animale[0]+"-"+animale[1]+"-"+animale[2]+"\n"
        file.write(riga)
    file.close()

Lista = carica()
bubblesort(Lista)
salva(Lista)
