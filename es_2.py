

def controllo_cane():
    errore=True
    while errore:
        errore=False
        canile=open("input.txt", "r")
        #cani_file=canile.readlines()
        #cani=[]
        cani_visual=canile.read()
        print(cani_visual)
        lista_cani=canile.readlines()
        cani=list(lista_cani)
        adotta_animale=input("Scegli l'animale da adottare: ")
        if adotta_animale not in cani:
            if len(adotta_animale) == 0:
                print("Cane non presente")
            else:
                print("Cane presente")
        canile.close()

def adotta():
    
    #for cane in cani_file:
    #    cani.append(cane)
    #    print(cani)
    #for index in cani:
    #    print(index)
    canile_2=open("input.txt", "r")
    lista_cani_2=canile.readlines()
    cani_2=list(lista_cani_2)
    adotta_animale_=controllo_cane()
    for cane in cani_2:
        cane=cani.index()
        print(cane)
    #adotta=input("Scegli quale animale adottare: ")
    #if adotta not in cani:
    #    print("cane non presente")
    #else:
    canile_2.close()
    menu()

def ordina():
    errore=True
    while errore:
        errore=False
        lettura_file=open("input.txt", "r")
        if not lettura_file:
            print("File vuoto")
        else:
            righe=lettura_file.readlines()
            righe_1=str(righe)
            lettura_uscita=open("output.txt","w")
            lettura_uscita.write(righe_1)
            lettura_file.close()
            lettura_uscita.close()

            


    menu()
    
def visualizza_in():
    lettura_file_in=open("input.txt", "r")
    lettura_input = lettura_file_in.read()
    print(lettura_input)
    lettura_file_in.close()
    menu()

def visualizza_out():
    lettura_file_out=open("output.txt", "r")
    lettura_output= lettura_file_out.read()
    print(lettura_output)
    lettura_file_out.close()
    menu()

def ordina_uguale():
    uguali={

    }
    apertura=open("input.txt", "r")
    righe_2=apertura.readline()
    for cane in righe_2.split("-"):
        if cane == cane:
            uguali[cane] = cane
    print("ho messo i cani con lo stesso nome nel dizionario")
    print(uguali)
    apertura.close()
    menu()

def menu():
    print("1- ordina per razza ")
    print("2- esci")
    print("3- adotta un animale")
    print("4- visualizza input.txt")
    print("5- visualizza output.txt")
    print("6- ordinamento per nome uguale")
    errore=True
    while errore:
        errore=False
    scelta = input("Scegli: ")
    if scelta =="1":
        ordina()
    elif scelta == "2":
        print("sei uscito")
        errore=False
    elif scelta == "3":
        adotta()
    elif scelta == "4":
        visualizza_in()
    elif scelta == "5":
        visualizza_out()
    elif scelta == "6": 
        ordina_uguale()
        
menu()