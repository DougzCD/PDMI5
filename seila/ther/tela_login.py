import flet as ft 

def main(pagina:ft.Page):
    pagina.title = "Tela de LOGIN"
    titulo = ft.Text(value='Login', style = ft.TextThemeStyle.DISPLAY_LARGE)
    username = ft.TextField(label= 'Usuário', hint_text='Digite seu usuário', width=200)
    senha = ft.TextField(label='Senha', hint_text='Digite sua senha', password=True, width=200)
    feedback = ft.Text(value='')
    
    def login(e):
        if username.value=="Ther" and senha.value=="1234":
           feedback.value= 'Login bem sucedido'
           feedback.color= 'green'
        
        else:
             feedback.value = "Por favor, preencha todos os campos!"
             feedback.color = "red"
    
        pagina.update()
        
    login_senha = ft.ElevatedButton(text='Login', on_click=login)
    
    pagina.add(
        ft.Row([
            ft.Column([
                titulo,
                username,
                senha,
                login_senha,
                feedback
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)
    )
    
ft.app(target=main)
