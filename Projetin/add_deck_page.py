import flet as ft
from deck_list_page import remove_deck

def add_deck(deck_name, deck_list, deck_status):
    if deck_name.value:
        deck_list.controls.append(
            ft.ListTile(
                title=ft.Text(deck_name.value),
                trailing=ft.IconButton(
                    icon=ft.icons.DELETE,
                    on_click=lambda e: remove_deck(deck_name.value, deck_list)
                ),
                leading=ft.Checkbox(
                    label="Marcar como concluído",
                    value=False,
                    on_change=lambda e: update_deck_status(deck_name.value, deck_list, deck_status)
                ),
                subtitle=ft.Text("Classificação: " + deck_status.value),
            )
        )
        deck_name.value = ""
        deck_list.update()

def update_deck_status(deck_name, deck_list, deck_status):
    for deck in deck_list.controls:
        if deck.title.value == deck_name:
            deck.subtitle = ft.Text("Classificação: " + deck_status.value)
            break
    deck_list.update()

def show_add_deck_screen(page, deck_name, deck_status, deck_list):
    page.controls.clear()
    page.controls.append(
        ft.Column(
            controls=[
                ft.Text("Adicionar Novo Deck", size=25, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Nome do Deck", ref=deck_name),
                ft.Dropdown(
                    options=[
                        ft.DropdownOption(text="Bom"),
                        ft.DropdownOption(text="Médio"),
                        ft.DropdownOption(text="Ruim")
                    ],
                    label="Classificação",
                    ref=deck_status
                ),
                ft.ElevatedButton("Adicionar Deck", on_click=lambda e: add_deck(deck_name, deck_list, deck_status))
            ],
            alignment=ft.alignment.center
        )
    )
    page.update()

