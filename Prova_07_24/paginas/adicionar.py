import flet as ft

def AdicionarView(page: ft.Page):
    return ft.View(
        "/adicionar",
        [
            ft.AppBar(title=ft.Text("Tarefas Magicas"), bgcolor="#f5b5d6", color="#ffffff"),
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
                        ft.TextField(hint_text="Nome da Tarefa", bgcolor = "#ffffff", border_width = 2, border_color = "#f5b5d6"),
                        ft.TextField(hint_text="Descrição da Tarefa", bgcolor = "#ffffff", border_width = 2, border_color = "#f5b5d6"),
                        ft.ElevatedButton(
                            text="Adicionar Tarefa",
                            bgcolor = "#89CFF0",
                            color = "#ffffff",
                            on_click=lambda _: page.go("/")
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
