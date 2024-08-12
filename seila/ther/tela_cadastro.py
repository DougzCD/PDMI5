import flet as ft 

def main(pagina:ft.Page):
    pagina.title = 'Tela de Cadastro'
    titulo = ft.Text(value="CADASTRO", style=ft.TextThemeStyle.DISPLAY_LARGE)
    name = ft.TextField(label='Nome',width=200)
    email = ft.TextField(label='Email', width=200)
    username = ft.TextField(label='Usuário',width=200)
    senha = ft.TextField(label= 'Senha',password=True,width=200)
    feedback = ft.Text(value="")
    
    def signup(e):
        if name.value and email.value and username.value and senha.value:
            feedback.value = "Cadastro bem sucedido"
            feedback.color = "green"
        else:
            feedback.value = "Por favor, preencha todos os campos!"
            feedback.color = "red"
            
        pagina.update()
            
    botao_senha = ft.ElevatedButton(text='Cadastrar', on_click=signup)
    
    pagina.add(
        ft.Row([
            ft.Column([
                titulo,
                name,
                email,
                username,
                senha,
                botao_senha,
                feedback
                
            ])
        ], alignment=ft.MainAxisAlignment.CENTER)
    )
ft.app(target=main)