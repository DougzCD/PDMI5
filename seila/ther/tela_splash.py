import flet as ft 
import time

#função da tela principal
def main_screen(pagina:ft.Page):
    pagina.title = 'TELA INICIAL'
    pagina.clean()
    texto = ft.Text("Bem vindo ao aplicativo", style=ft.TextThemeStyle.DISPLAY_LARGE)
    pagina.add(texto)
    
    
def splash_screen(pagina:ft.Page):
        pagina.title = 'TELA SPLASH'
        logo = ft.Image(src="https://www.petz.com.br/blog/wp-content/uploads/2019/07/vida-de-gato.jpg", width = 500, height = 500)
        texto = ft.Text("carregando...", style=ft.TextThemeStyle. DISPLAY_LARGE, color="green")
        progress_bar = ft.ProgressBar(width=100)
        pagina.add(logo,texto,progress_bar)
        
        for i in range(100):
          progress_bar.value = i/100
          pagina.update()
          time.sleep(0.05)
        
        main_screen(pagina)
        
#função principal
def main(pagina:ft.Page):
        
        splash_screen(pagina)
        
ft.app(target=main)
