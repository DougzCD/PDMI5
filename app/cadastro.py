import flet as ft
import time

# FUNÇÃO PARA A TELA INICIAL
def main_screen(pagina: ft.Page):

    pagina.title = "TELA INICIAL"
    pagina.clean()
    text = ft.Text("Bem-vindo ao Wizard Showdown",
                    style=ft.TextThemeStyle.DISPLAY_LARGE)
    pagina.add(text)
    
# FUNÇÃO PARA A TELA SPLASH
def splash_screen(pagina: ft.Page):
    pagina.title="SPLASH SCREEN"
    logo = ft.Image(src="https://e7.pngegg.com/pngimages/446/995/png-clipart-pixel-dungeon-pixel-art-boss-others-miscellaneous-game.png",
                    width=500,height=500)
    text = ft.Text("Carregando...",
                   style=ft.TextThemeStyle.DISPLAY_LARGE,
                   color="blue")
    progress_bar = ft.ProgressBar(width=200)
    pagina.add(logo, text, progress_bar)
    
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
