import flet as ft

# Define your main function to handle a page
def main(pagina: ft.Page):

    pagina.title = "Pagina Teste"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    #Fundo Degrade
    gradient_container = ft.Container(
        width=pagina.window_width,
        height=pagina.window_height,
        gradient=ft.LinearGradient(
            colors=["#33FFF6","#9809A2"],
            begin=ft.Alignment(-1,-1), #top-left
            end=ft.Alignment(1,1) #bottom-right
        )
    )
    
    #Componente Perssonalizado
    title = ft.Text(
        value="Tela Perssonalizada",
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        color="#000000"
    )
    subtitle = ft.Text(
        value="Bem Vindo",
        style=ft.TextThemeStyle.DISPLAY_LARGE,
        color="#000000"
    )
    username = ft.TextField(
        label="Usuário",
        hint_text="Digite seu usuário", 
        width = 200,
        text_size=ft.TextStyle(
            color="#333333"
        )
    )
    password = ft.TextField(
        label="Senha",
        hint_text="Digite sua senha", 
        password=True,
        width = 200,
        text_size=ft.TextStyle(
            color="#333333"
        )
    )
    login_btn = ft.ElevatedButton(
        text="Login",
        on_click=lambda e:print("Click!"),
        bgcolor="#000000",
        color="#FFFFFF"
    )
    
    # Adicionando os componentes à pagina dentro do container com fundo degradê
    gradient_container.content=ft.Container(
        content=ft.Column(
            [
                title,
                subtitle,
                username,
                password,
                login_btn
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        padding=20
    )
    
    pagina.add(gradient_container)
    
    pagina.update()

# Run the application using ft.app, with main as the entry point
ft.app(target=main)
