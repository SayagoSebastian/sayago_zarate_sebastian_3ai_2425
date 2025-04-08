nomi=[]
classi=[]
diz={

}



def nomi_classi():
    errore=True
    while errore:
        errore=False
        tot_numeri_nomi_classi=int(input("Quanti nomi e cognomi vuoi inserire?"))
        for i in range(0,tot_numeri_nomi_classi):
            nome=input("Scrivi il nome dell'alunno: ")
            if nome == "":
                print("Errore, nome non valido")
                errore=True
            else:
                print("Nome valido")
                nomi.append(nome)
    errore=True
    while errore:
        errore=False  
        for i in range(0,tot_numeri_nomi_classi):
            classe=input("Scrivi la classe dell'alunno: ")
            if classe == "":
                print("Errore, cognome non valido")
                errore=True
            else:
                print("Classe valida")
                classi.append(classe)


    #for i in len(nomi):
    diz[nomi[0]]= [classi[-1]]
    diz[nomi[1]]= [classi[-2]]
    diz[nomi[2]]= [classi[-3]]


    

    print(nomi)
    print(classi)
    print(diz)

nomi_classi()
                



