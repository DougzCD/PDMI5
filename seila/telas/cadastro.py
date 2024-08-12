import flet as ft

# Define your main function to handle a page
def main(pagina: ft.Page):

    pagina.title = "Pagina Teste"
    pagina.vertical_alignment = ft.CrossAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    gradient_container = ft.Container(
        width=pagina.window_width,
        height=pagina.window_height,
        gradient=ft.LinearGradient(
            colors=["#33FFF6","#9809A2"],
            begin=ft.Alignment(-1,-1), #top-left
            end=ft.Alignment(1,1) #bottom-right
        )
    )
    
    # Funçoes da Pagina
    
    def btn_click(e):
        if name.value and email.value and username.value and password.value:
            feedback.value="Cadastro bem sucedido"
            feedback.color="green"
            #pagina.update
        else:
            feedback.value="Por favor preencha todos os campos"
            feedback.color="red"
        pagina.update
         
    # Elementos da Pagina
    
    name = ft.TextField(label="name", width =200)
    email = ft.TextField(label="E-Mail", width =200)
    username = ft.TextField(label="username", width =200)
    password = ft.TextField(label="password",password=True , width =200)
    feedback = ft.Text(value="")
    
    login_btn = ft.ElevatedButton("cadastrar", on_click=btn_click)
    
    gradient_container.content=ft.Container(
        content=ft.Column(
            [
                name,
                email,
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
