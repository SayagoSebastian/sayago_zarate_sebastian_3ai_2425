def disegna_albero(n):
    if n < 3 or n % 2 == 0:
        print("Il numero deve essere un intero dispari maggiore o uguale a 3.")
        return
    
   
    for i in range(1, n + 1, 2):
        print(" " * ((n - i) // 2) + "*" * i)
    
   
    largh = n // 3 + (n // 3 % 2 == 0)  
    alt = n // 3
    spazio = (n - largh) // 2
    for x in range(alt):
        print(" " * spazio + "*" * largh)

n = int(input("Inserisci un numero dispari maggiore o uguale a 3: "))
disegna_albero(n)