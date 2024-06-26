import flet as ft

# Define your main function to handle a page
def main(pagina: ft.Page):

    pagina.title = "Pagina Teste"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Funçoes da Pagina
    
    def btn_click(e):
        #if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            pagina.update
        #else:
            name = txt_name.value
            pagina.clean()
            pagina.add(ft.Text(f"Hello, {name}!"))

    def checkbox_changed(e):
        output_text.value = f"You have learned how to ski {todo_check.value}."
        pagina.update()
        
    def button_clicked(e):
        output_text.value = f"Dropdown value is: {color_dropdown.value}"
        pagina.update()
    
    # Elementos da Pagina
    
    t = ft.Text(value="Ola!", color="red")
    btn = ft.ElevatedButton("Click me!", on_click=btn_click)
    txt_name = ft.TextField(label="Your name")
    output_text = ft.Text()
    todo_check = ft.Checkbox(label="ToDo: learn how to ski", value=False, on_change=checkbox_changed)         
    submit_btn = ft.ElevatedButton(text="Submit", on_click= button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options = [
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    pagina.add(t, btn, txt_name, todo_check, output_text, color_dropdown, submit_btn)
    
    pagina.update()

# Run the application using ft.app, with main as the entry point
ft.app(target=main)
