import flet as ft 

def main(pagina: ft.Page):
    pagina.add(
        ft.Text(
            spans=[
                ft.TextSpan(
                    'Greetings, planet!',
                    ft.TextStyle(
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        foreground=ft.Paint(
                            gradient=ft.PaintLinearGradient(
                                (0, 20), (150, 20), [ft.colors.BLUE, ft.colors.PINK]
                            )
                        ),
                    ),
                ),
            ],
        )
    )
    
ft.app(main)