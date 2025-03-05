import os

# Funzione per leggere il contenuto di un file e restituirlo in minuscolo
def leggi_file(nome_file):
    try:
        with open(nome_file, 'r', encoding='utf-8') as f:
            return f.read().lower()
    except FileNotFoundError:
        print(f"Non è stato possibile trovare il file {nome_file}.")
        return ""

# Funzione per eseguire i conteggi di parolacce, parole e lettere
def analizza_biblioteca():
    try:
        with open('parolacce.txt', 'r', encoding='utf-8') as f:
            lista_parolacce = set(f.read().strip().split('\n'))
    except FileNotFoundError:
        print("Il file 'parolacce.txt' non è stato trovato.")
        return 0, [], {}

    numero_parolacce = 0
    parole_frequenti = {}
    frequenza_lettere = {}


    lista_file = os.listdir(".")
    for file in lista_file:
        if file[-4:] == '.txt':  # Verifica che il file sia un .txt
            contenuto = leggi_file(file)
            if contenuto:
                
                parole = contenuto.split()
                for parola in parole:
                    if parola in lista_parolacce:
                        numero_parolacce += 1

                
                for parola in parole:
                    if parola in parole_frequenti:
                        parole_frequenti[parola] += 1
                    else:
                        parole_frequenti[parola] = 1

                
                for lettera in contenuto:
                    if 'a' <= lettera <= 'z':  
                        if lettera in frequenza_lettere:
                            frequenza_lettere[lettera] += 1
                        else:
                            frequenza_lettere[lettera] = 1

    # Ordina le parole per frequenza e prendi solo le prime 50
    classifica_parole = []
    for parola, conta in parole_frequenti.items():
        classifica_parole.append((parola, conta))

    for i in range(len(classifica_parole)):
        for j in range(i + 1, len(classifica_parole)):
            if classifica_parole[i][1] < classifica_parole[j][1]:
                classifica_parole[i], classifica_parole[j] = classifica_parole[j], classifica_parole[i]

    
    classifica_parole = classifica_parole[:50]

    return numero_parolacce, classifica_parole, frequenza_lettere

# Funzione principale che esegue i conteggi e mostra i risultati
def mostra_risultati():
    numero_parolacce, parole_classifica, lettere_frequenza = analizza_biblioteca()

    print(f"Totale parolacce trovate: {numero_parolacce}")
    print("Classifica delle prime 50 parole più frequenti:")
    for parola, frequenza in parole_classifica:
        print(f"{parola}: {frequenza}")

    print("Frequenza delle lettere dell'alfabeto:")
    for lettera, frequenza in lettere_frequenza.items():
        print(f"{lettera}: {frequenza}")


mostra_risultati()
