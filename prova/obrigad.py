import flet as ft
   
# pagina principal
def main_screen(page: ft.Page):

    page.title = "TELA INICIAL"
    page.clean()
    
    gradient_container = ft.Container(
        width=page.window_width,
        height=page.window_height,
        gradient=ft.LinearGradient(
            colors=["#33FFF6","#9809A2"],
            begin=ft.Alignment(-1,-1), #top-left
            end=ft.Alignment(1,1) #bottom-right
        )
    )
    
    text = ft.Text("Obrigado por usar ao Todos",
                    style=ft.TextThemeStyle.DISPLAY_LARGE)
    
    gradient_container.content=ft.Container(
        content=ft.Column(
            [
                text,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=20
    )
    
    page.add(gradient_container)
    
ft.app(target=main_screen)
