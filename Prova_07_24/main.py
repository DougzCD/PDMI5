import flet as ft
from paginas.visualizar import VizualizarView
from paginas.adicionar import AdicionarView
from paginas.remover import RemoverView

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(VizualizarView(page))
        elif page.route == "/adicionar":
            page.views.append(AdicionarView(page))
        elif page.route == "/remover":
            page.views.append(RemoverView(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
