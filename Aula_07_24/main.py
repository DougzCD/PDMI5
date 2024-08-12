import flet as ft
from paginas.page1 import Page1View
from paginas.page2 import Page2View
from paginas.page3 import Page3View

def main(page: ft.Page):
    def route_change(route):
        
        page.views.clear(),
        
        if page.route == "/":
            
            page.views.append(Page1View(page))
            
        elif page.route == "/page2":
            
            page.views.append(Page2View(page))
            
        elif page.route == "/page3":
            
            page.views.append(Page3View(page))
            
        
        page.update()
        

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
