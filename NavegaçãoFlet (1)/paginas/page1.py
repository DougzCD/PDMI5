import flet as ft

def Page1View(page: ft.Page):
    return ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Flet app"), bgcolor="#f5b5d6", color="#ffffff"),
            ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=-10,
                gradient=ft.LinearGradient(
                    colors=["0xffffffe8","0xfffeff86"],
                    begin=ft.Alignment(-1,-1),
                    end=ft.Alignment(1,1)
                ),
                content=ft.Container(
                    content=ft.Column(
                    controls=[
                        ft.TextField(hint_text="Login", bgcolor = "#ffffff", border_width = 2, border_color = "#f5b5d6"),
                        ft.TextField(hint_text="Senha", bgcolor = "#ffffff", border_width = 2, border_color = "#f5b5d6"),
                        ft.ElevatedButton(
                            text="Fazer Login", 
                            bgcolor = "#89CFF0", 
                            color = "#ffffff", 
                            on_click=lambda _: page.go("/page3")
                        ),
                        ft.ElevatedButton(
                            text="Registre-se",
                            bgcolor = "#89CFF0",
                            color = "#ffffff",
                            on_click=lambda _: page.go("/page2")
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20
            )
            ),
        ]
    )
                        
                            
                        
            
