import flet as ft
from paginas.home_page import show_home_screen
from paginas.deck_list_page import show_deck_list_screen
from paginas.add_deck_page import show_add_deck_screen
from paginas.splash import splash_screen

def main(page: ft.Page):
    page.title = "Aplicativo de Gerenciamento de Decks"
    page.horizontal_alignment = ft.alignment.center
    page.vertical_alignment = ft.alignment.center

    # Referências para os componentes
    deck_name = ft.Ref[ft.TextField]()
    deck_status = ft.Ref[ft.Dropdown]()
    deck_list = ft.Column()

    # Configuração de rotas
    def route_change(route):
        
        if route =="/":
            
            splash_screen(page)
            
        elif route == "/home":
            
            show_home_screen(page)
            
        elif route == "/decks":
            
            show_deck_list_screen(page, deck_list)
            
        elif route == "/add":
            
            show_add_deck_screen(page, deck_name, deck_status, deck_list)
            
    
    page.on_route_change = route_change

    # Configuração do AppBar e BottomAppBar
    page.appbar = ft.AppBar(
        title=ft.Text("Gerenciador de Decks"),
        actions=[
            ft.IconButton(icon=ft.icons.HOME, on_click=lambda e: page.go("/")),
            ft.IconButton(icon=ft.icons.LIST, on_click=lambda e: page.go("/decks")),
            ft.IconButton(icon=ft.icons.ADD, on_click=lambda e: page.go("/add")),
        ]
    )
    
    page.bottom_bar = ft.BottomAppBar(
        content=ft.Container(
            content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.ADD, on_click=lambda e: page.go("/add"))
                ],
                alignment=ft.MainAxisAlignment.END
            ),
            padding=ft.Padding(10,10,10,10),
        )
    )

    # Fundo degradê
    page.bgcolor = ft.LinearGradient(colors=["#33FFF6","#9809A2"])

    # Mostra a tela inicial por padrão
    show_home_screen(page)

ft.app(target=main)
