import flet as ft
import time

# FUNÇÃO PARA A TELA INICIAL
def main_screen(pagina: ft.Page):

    pagina.title = "TELA INICIAL"
    pagina.clean()
    
    gradient_container = ft.Container(
        width=pagina.window_width,
        height=pagina.window_height,
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
    
    pagina.add(gradient_container)
    
    
# FUNÇÃO PARA A TELA SPLASH
def splash_screen(pagina: ft.Page):
    pagina.title="SPLASH SCREEN"
    
    gradient_container = ft.Container(
        width=pagina.window_width,
        height=pagina.window_height,
        gradient=ft.LinearGradient(
            colors=["#33FFF6","#9809A2"],
            begin=ft.Alignment(-1,-1), #top-left
            end=ft.Alignment(1,1) #bottom-right
        )
    )
    
    logo = ft.Image(src="app\pngwing.com.png",
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
    
    pagina.add(gradient_container)
    
    # SIMULA UM TEMPO DE CARREGAMENTO DDE X SEGUNDOS COM ATUALIZAÇÃO DO PROGRESSO
    for i in range(100):
        progress_bar.value = i/100
        pagina.update()
        time.sleep(0.03)
        
    main_screen(pagina)


# FUNÇÃO PRINCIPAL
def main(pagina:ft.Page):
    
    splash_screen(pagina)
    
ft.app(target=main)
