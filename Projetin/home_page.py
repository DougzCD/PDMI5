import flet as ft

def show_home_screen(page):
    
    page.title="SPLASH SCREEN"
    
    page.controls.clear()
    page.controls.append(
        ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text("Bem-vindo ao aplicativo de decks!", size=30, weight=ft.FontWeight.BOLD),
                    alignment=ft.alignment.center,
                    padding=ft.Padding(20,20,20,20),
                    bgcolor=ft.colors.LIGHT_BLUE
                    width=page.window_width,
                    height=page.window_height,
                    gradient=ft.LinearGradient(
                       colors=["#33FFF6","#9809A2"],
                       begin=ft.Alignment(-1,-1), #top-left
                       end=ft.Alignment(1,1) #bottom-right
                    )
                ),
                ft.Image(src="path_to_logo.png", width=150, height=150, fit=ft.ImageFit.CONTAIN),
                ft.Text("Este aplicativo ajuda você a gerenciar seus decks de forma eficiente."),
            ],
            alignment=ft.alignment.center
        )
    )
    page.update()
