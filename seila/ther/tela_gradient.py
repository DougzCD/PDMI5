import flet as ft 

def main(pagina:ft.Page):
    pagina.title = 'Tela de LOGIN'
    
    gradiente_container = ft.Container(
        width=pagina.window_width,
        height=pagina.window_height,
        gradient=ft.LinearGradient(
            colors=['#33FFF6', 'pink', 'orange', 'white'],
            begin=ft.Alignment(-1,-1), #top-left
            end=ft.Alignment(1,1) #bottom-rigth
        )
    )
    
    titulo = ft.Text(
        value='TELA PERSONALIZADA',
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        color='white')
    subtitulo = ft.Text(
        value='Bem-vindo à aplicação com fundo degradê',
        style=ft.TextThemeStyle.TITLE_MEDIUM,
        color='white')
    
    username = ft.TextField(
        label='Usuário',
        hint_text='Digite seu usuário',
        width=200,
        text_style=ft.TextStyle(color="#333333")
        )
    senha = ft.TextField(
        label='Senha',
        hint_text='Digite sua senha',
        password=True,
        width=200,
        text_style=ft.TextStyle(color='#333333')
        )
    feedback = ft.Text(value='')
    
    def login(e):
        if username.value=="Ther" and senha.value=="1234":
           feedback.value= 'Login bem sucedido'
           feedback.color= 'green'
        else:
            feedback.value = "Por favor, preencha todos os campos!"
            feedback.color = "red"
    
        pagina.update()
    
    login_botao = ft.ElevatedButton(text='Login', on_click=login)
    
    gradiente_container.content = ft.Container(
        content=ft.Column(
            [
                titulo,
                subtitulo,
                username,
                senha,
                login_botao,
                feedback
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
         ),
         padding=20

    )

    pagina.add(gradiente_container)
    
ft.app(target=main)
