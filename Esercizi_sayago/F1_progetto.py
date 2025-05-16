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
    # Impostazioni della pagina
    page.title = "Qualifiche F1"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLACK
    page.window_min_width = 1000
    page.window_min_height = 700

    

