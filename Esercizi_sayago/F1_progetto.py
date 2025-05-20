import flet as ft

def pagina_seconda(page: ft.Page):
    # Prima rimuoviamo tutti i controlli visibili
    page.controls.clear()

    # Contenuto della seconda pagina
    pagina_seconda = ft.Column([
        ft.Text("Sei nella seconda pagina!", size=30, color=ft.Colors.WHITE),
        ft.ElevatedButton("Torna indietro", on_click=lambda e: main(page))
    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    page.add(pagina_seconda)
    page.update()

def main(page: ft.Page):
    page.title = "Benvenuto"
    page.window_min_width = 1000
    page.window_min_height = 700

    def on_inizia_click(e):
        pagina_seconda(page)

    bottone_inizia = ft.ElevatedButton("Inizia", width=150, height=50, on_click=on_inizia_click)

    layout_iniziale = ft.Stack([
        ft.Image(
            src="sfondo_primo.jpeg",
            fit=ft.ImageFit.COVER,
        ),
        ft.Container(
            content=ft.Column(
                controls=[bottone_inizia],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            alignment=ft.alignment.center
        )
    ])


    # --- Seconda schermata ---
    nome_input = ft.Dropdown(
        label="Scegli Pilota",
        options=[ft.dropdown.Option(p) for p in piloti_f1_2025],
        width=300
    )

    tempo_input = ft.TextField(
        label="Tempo (minuto:secondi.decimi)",
        hint_text="es: 1:14.345",
        width=300
    )

    errore_text = ft.Text("", color=ft.Colors.RED)
    output = ft.Column(scroll=ft.ScrollMode.AUTO)
    stat_output = ft.Column()

    def aggiorna_classifica():
        output.controls.clear()
        for i, p in enumerate(classifica):
            output.controls.append(
                ft.Row([
                    ft.Text(f"{i+1}.", width=30, color=ft.Colors.WHITE),
                    ft.Text(p["nome"], width=200, color=ft.Colors.YELLOW),
                    ft.Text(p["tempo"], width=100, color=ft.Colors.CYAN),
                    ft.ElevatedButton("Modifica", on_click=lambda e, pilota=p: modifica_click(pilota))
                ])
            )
        page.update()
    # Rimuoviamo tutti i controlli prima di aggiungere (utile se torni indietro)
    page.controls.clear()
    page.add(layout_iniziale)
    page.update()

ft.app(target=main)
