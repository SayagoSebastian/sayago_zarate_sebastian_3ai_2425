import flet as ft
def main(page: ft.Page):

    classi = [
        {"name": "1ai", "icon_name": ft.Icons.CLOUD_OUTLINED},
        {"name": "2ai", "icon_name": ft.Icons.CLOUD_OUTLINED},
        {"name": "3ai", "icon_name": ft.Icons.CLOUD_OUTLINED},
        {"name": "4ai", "icon_name": ft.Icons.CLOUD_OUTLINED},
        {"name": "5ai", "icon_name": ft.Icons.CLOUD_OUTLINED},
        {"name": "1L", "icon_name": ft.Icons.CLOUD_OUTLINED},
        {"name": "3bi", "icon_name": ft.Icons.CLOUD_OUTLINED},
    ]
    t_nome = ft.Text()
    page.title = "Sondaggio"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    primo_titolo = ft.Text("Prima Parte", size=30)
    primo_testo = ft.Text("Verifica che il nome dell'intervistato non sia già stato utilizzato.", size=10)
    secondo_titolo = ft.Text("Seconda Parte", size=30)
    secondo_testo = ft.Text("Accoda le preferenze nel file sondaggio.txt", size=10)
    testo_box = ft.Text("Sistemi di gioco a disposizione: ")
    secondo_testo_box= ft.Text("Tipologia di gioco preferita: ")
    divisore = ft.Divider(height=9, color="black")
    nome = ft.TextField(label="Nome intervistato", icon=ft.Icons.PEOPLE)
    bottone = ft.FilledButton("Inizia", icon=ft.Icons.SEARCH)

    def controllo_nome(e, nome):
        if len(nome)< 3:
            errore= ft.Text("Nome non valido")
        else:
            page.open()
    def button_clicked(e):
        t.value = f"Da inserire nel file sondaggio.txt: CONSOLE: '{opz_1.value}', '{opz_2.value}', '{opz_3.value}', '{opz_4.value}', '{opz_5.value}', TIPOLOGIA:  '{cg.value}' , CLASSE: '{dd.value}' NOME: '{nome.value}'"
        t_nome = f"Nome: '{nome.value}"
        t_classe = f"Classe: {dd.value}"
        page.update() 
    
    t = ft.Text()
    opz_1 = ft.Checkbox(label= "xbox", value="xbox")
    opz_2 = ft.Checkbox(label= "Psx", value="Psx")
    opz_3 = ft.Checkbox(label="Switch", value= "Switch" )
    opz_4 = ft.Checkbox(label="Pc", value="PC" )
    opz_5 = ft.Checkbox(label="Android/Ios", value="Android/Ios")
    
    def radio_bottone(e):
        t_radio.value= f"Informazione da inserire nel file: {e.control.value}"
        page.update()
    t_radio = ft.Text()
    cg = ft.RadioGroup(
        content= ft.Row(
            [
                ft.Radio(label="Nessuna", value="Nessuna"),
                ft.Radio(label="Sport", value="Sport"),
                ft.Radio(label="Platform", value="Platform"),
                ft.Radio(label="Rpg", value="Rpg"),
                ft.Radio(label="Fps", value="Fps"),
            ]
        ),
        on_change=radio_bottone,
    )
    
    
    def classe_elenco():
        options = []
        for icon in classi:
            options.append(
                ft.DropdownOption(key=icon["name"], leading_icon=icon["icon_name"])
            )
        return options
    t_classe=ft.Text()
    dd = ft.Dropdown(
        editable=True,
        leading_icon=ft.Icons.SEARCH,
        label="Quale anno frequenti?",
        options=classe_elenco(),
    )
    
    
    b_finale = ft.FilledButton(text="Conferma", icon=ft.Icons.ADD_OUTLINED, on_click=button_clicked)
    page.add(
        ft.Column
        ([
            primo_titolo,
            primo_testo,
        ]),
        ft.Row([
            nome, bottone,
        ]),
        ft.Column([
            divisore,
            secondo_titolo,
            secondo_testo,
            testo_box,
            opz_1, opz_2, opz_3, opz_4, opz_5,
            secondo_testo_box,
            cg,
            divisore,
            dd,
            ft.CupertinoSwitch(
                label="Acconsento all'invio delle promozioni pubblicitarie",
                value=True
            ),
        b_finale,
        t
        ]
    )
    )

ft.app(main)