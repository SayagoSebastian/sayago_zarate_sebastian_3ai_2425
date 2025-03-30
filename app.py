import flet as ft

def main(page: ft.Page):
    def b_clicked(e):
        t.value = f"Dati inseriti: {nome.value}, {cognome.value}, {classe.value}, {sesso.value}, {anno_nascita.value}, {sport.value}, {console.value}"
        page.update()

    t = ft.Text(text_align=ft.TextAlign.CENTER)
    nome = ft.TextField(label="Nome", text_align=ft.TextAlign.CENTER)
    cognome = ft.TextField(label="Cognome", text_align=ft.TextAlign.CENTER)
    classe = ft.TextField(label="Classe", text_align=ft.TextAlign.CENTER)
    sesso = ft.Dropdown(label="Sesso", options=[ft.dropdown.Option("Maschio"), ft.dropdown.Option("Femmina")])
    anno_nascita = ft.TextField(label="Anno di Nascita", text_align=ft.TextAlign.CENTER)
    sport = ft.Dropdown(label="Sport Preferito", options=[
        ft.dropdown.Option("Calcio ⚽"),
        ft.dropdown.Option("Basket 🏀"),
        ft.dropdown.Option("Ping Pong 🏓"),
        ft.dropdown.Option("Atletica 🏃")
    ])
    console = ft.Dropdown(label="Console Preferita", options=[
        ft.dropdown.Option("PSN"),
        ft.dropdown.Option("Xbox"),
        ft.dropdown.Option("Switch")
    ])
    b = ft.ElevatedButton(text="Submit", on_click=b_clicked)

    page.add(
        ft.Column([
            nome,
            cognome,
            classe,
            sesso,
            anno_nascita,
            sport,
            console,
            b,
            t
        ], alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
