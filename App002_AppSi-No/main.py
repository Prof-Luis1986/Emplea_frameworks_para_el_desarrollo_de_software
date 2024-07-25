import flet as ft

def main(page: ft.Page):
    page.title = "¿Me perdonas?"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    label = ft.Text(
        "¿Me perdonas?", 
        style=ft.TextStyle(size=40, weight="bold")
    )
    image = ft.Image(src="triste.png", width=200, height=200)
    
    button_yes = ft.ElevatedButton(text="Sí", color=ft.colors.GREEN, width=100, height=50)
    button_no = ft.ElevatedButton(text="No", color=ft.colors.RED, width=100, height=50)

    def no_click(e):
        button_yes.width += 20
        button_yes.height += 10
        page.update()
    
    def yes_click(e):
        image.src = "Feliz.png"
        page.update()

    button_no.on_click = no_click
    button_yes.on_click = yes_click

    page.add(
        ft.Column(
            [
                label,
                image,
                ft.Row(
                    [button_yes, button_no],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

ft.app(target=main)
