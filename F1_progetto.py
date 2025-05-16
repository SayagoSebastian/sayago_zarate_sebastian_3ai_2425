import flet as ft
def tempo_in_secondi(tempo_str):
    """
    Converte una stringa di tempo nel formato 'mm:ss.ccc' in secondi float.
    Ritorna None se il formato non è valido o se i valori superano i limiti.
    """
    try:
        minuti, resto = tempo_str.split(":")
        secondi, millisecondi = resto.split(".")
        minuti = int(minuti)
        secondi = int(secondi)
        millisecondi = int(millisecondi)
        
        if secondi >= 60 or millisecondi >= 1000:
            return None  # Tempo non valido

        return minuti * 60 + secondi + millisecondi / 1000
    except:
        return None

def main(page: ft.Page):
    page.title = "Benvenuto"
    page.window_min_width = 1000
    page.window_min_height = 700

    bottone_inizia = ft.ElevatedButton("Inizia", width=150, height=50)

    layout_iniziale = ft.Stack([
        ft.Image(
            src="sfondo_primo.jpeg",
            fit=ft.ImageFit.COVER,
            expand=True,
            
        ),
        ft.Container(
            content=ft.Column(
                controls=[bottone_inizia],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            alignment=ft.alignment.center
        )
    ], expand=True)

    page.add(layout_iniziale)

ft.app(target=main)