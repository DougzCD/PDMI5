import flet as ft
import time

# FUNÇÃO PARA A TELA INICIAL
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
    
    text = ft.Text("Bem-vindo ao Wizard Showdown",
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
    
    
# FUNÇÃO PARA A TELA SPLASH
def splash_screen(page: ft.Page):
    page.title="SPLASH SCREEN"
    
    gradient_container = ft.Container(
        width=page.window_width,
        height=page.window_height,
        gradient=ft.LinearGradient(
            colors=["#33FFF6","#9809A2"],
            begin=ft.Alignment(-1,-1), #top-left
            end=ft.Alignment(1,1) #bottom-right
        )
    )
    
    logo = ft.Image(src="maginho.png",
                    width=500,height=500)
    text = ft.Text("Carregando...",
                   style=ft.TextThemeStyle.DISPLAY_LARGE,
                   color="blue")
    progress_bar = ft.ProgressBar(width=200)
    
    gradient_container.content=ft.Container(
        content=ft.Column(
            [
                logo,
                text,
                progress_bar
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=20
    )
    
    page.add(gradient_container)
    
    # SIMULA UM TEMPO DE CARREGAMENTO DDE X SEGUNDOS COM ATUALIZAÇÃO DO PROGRESSO
    for i in range(100):
        progress_bar.value = i/100
        page.update()
        time.sleep(0.03)
        
    main_screen(page)


# FUNÇÃO PRINCIPAL
def main(page:ft.Page):
    
    splash_screen(page)
    
ft.app(target=main)
