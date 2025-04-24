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

            


    
    
def visualizza_in():
    print("-"*30)
    print("VISUALIZZO INPUT.TXT")
    lettura_file_in=open("input.txt", "r")
    lettura_input = lettura_file_in.read()
    print(lettura_input)
    lettura_file_in.close()
    

def visualizza_out():
    print("-"*30)
    print("VISUALIZZO OUTPUT.TXT")
    lettura_file_out=open("output.txt", "r")
    lettura_output= lettura_file_out.read()
    print(lettura_output)
    lettura_file_out.close()
    

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
    
ordina()
visualizza_in()
visualizza_out()
ordina_uguale()