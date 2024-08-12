import flet as ft

def Page3View(page: ft.Page):
    return ft.View(
        "/page3",
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
                        ft.Text("Aqui está um placeholder para textos e afins", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                        ft.Text("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Delectus, aliquid sit eius odio at voluptate neque, dolorum minima natus quaerat suscipit laboriosam totam nam porro! Dolor quasi numquam deserunt distinctio molestiae eligendi quisquam at doloribus incidunt voluptatem! Aspernatur, asperiores perferendis. Doloremque, corporis? Eligendi eos voluptatum voluptates ratione. Eaque, modi! Non quos nulla eaque aspernatur neque ipsam aperiam totam? Aut aliquam sint accusantium illum maxime. Facilis voluptatibus optio explicabo eos repellendus ratione fugiat, sunt blanditiis, delectus, minus at qui earum. Blanditiis consequuntur dignissimos voluptatibus provident id! Architecto commodi quis magni obcaecati, expedita, exercitationem eius sint enim nihil, nobis culpa nostrum maiores."),
                        ft.ElevatedButton(
                            text="Voltar", 
                            bgcolor = "#89CFF0", 
                            color = "#ffffff", 
                            on_click=lambda _: page.go("/")
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
                padding=20
            )
            ),
        ]
    )
                        
                            
                        
            
