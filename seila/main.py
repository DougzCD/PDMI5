import flet as ft 
from telas.telaCadastro import CadastroScreen
def main(page:ft.page):
    splash_screen = CadastroScreen
    splash_screen.show()
ft.app(target=main)