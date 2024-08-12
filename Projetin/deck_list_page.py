import flet as ft

def remove_deck(deck_name, deck_list):
    for deck in deck_list.controls:
        if deck.title.value == deck_name:
            deck_list.controls.remove(deck)
            break
    deck_list.update()

def show_deck_list_screen(page, deck_list):
    page.controls.clear()
    page.controls.append(
        ft.Column(
            controls=[
                ft.Text("Lista de Decks", size=25, weight=ft.FontWeight.BOLD),
                deck_list,
            ],
            alignment=ft.alignment.center
        )
    )
    page.update()
