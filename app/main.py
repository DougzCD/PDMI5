import flet as ft

# Define your main function to handle a page
def main(pagina: ft.Page):

    pagina.title = "Pagina Teste"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    
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
    
    btn_logar = ft.ElevatedButton("cadastrar", on_click=btn_click)

    pagina.add(name, email, username, password, feedback, btn_logar)
    
    pagina.update()

# Run the application using ft.app, with main as the entry point
ft.app(target=main)
