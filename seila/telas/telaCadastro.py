import flet as ft

class BaseScreen:
    



class CadastroScreen(BaseScreen):
    def __init__(self, page: ft.page):
        super().__init__(page)
        self.db = Database()
        
    def on_register_click(self, e):
        username = self.username_field.value
        email = self.email_field.value
        password = self.passwordl_field.value
        
    def show(self)