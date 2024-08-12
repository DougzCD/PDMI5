import flet as ft
import time

def VizualizarView(page: ft.Page):
    
    logo = ft.Image(src="recursos\pngwing.com.png", width=500,height=500)
    text = ft.Text("Carregando...", style=ft.TextThemeStyle.DISPLAY_LARGE, color="blue")
    progress_bar = ft.ProgressBar(width=200)
    
    view = ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Tarefas Magicas"), bgcolor="#f5b5d6", color="#ffffff"),
            ft.Container(
                width=page.window_width,
                height=page.window_height,
                margin=-10,
                gradient=ft.LinearGradient(
                    colors=["#33FFF6","#9809A2"],
                    begin=ft.Alignment(-1,-1),
                    end=ft.Alignment(1,1)
                ),
                content=ft.Container(
                    content=ft.Column(
                    [
                        logo,
                        text,
                        progress_bar
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20
            )
            ),
 
        ]
    )
    for i in range(100):
        progress_bar.value = i/100
        page.update()
        time.sleep(0.03)
        
    page.go("/adicionar")
    
    return view
