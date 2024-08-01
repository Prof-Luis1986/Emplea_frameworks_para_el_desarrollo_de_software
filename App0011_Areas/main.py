import flet as ft

def main(page: ft.Page):
    page.title = "Cálculo de áreas"
    page.bgcolor = "green"
    
    def route_change(route):
        page.views.clear()

        # Se genera la vista principal
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.AppBar(title=ft.Text("Áreas", color="green"), bgcolor="yellow"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    ft.Image(src="Geo.jpg", width="100%", height="200px"),
                                    ft.Row(
                                        [
                                            ft.Container(
                                                content=ft.ElevatedButton("Ir al cuadrado", on_click=lambda _: page.go("/cuadrado")),
                                                border_radius=10,
                                                margin=5,
                                            ),
                                            ft.Container(
                                                content=ft.ElevatedButton("Ir al círculo", on_click=lambda _: page.go("/circulo")),
                                                border_radius=10,
                                                margin=5,
                                            ),
                                            ft.Container(
                                                content=ft.ElevatedButton("Ir al triángulo", on_click=lambda _: page.go("/triangulo")),
                                                border_radius=10,
                                                margin=5,
                                            ),
                                            ft.Container(
                                                content=ft.ElevatedButton("Ir al rectángulo", on_click=lambda _: page.go("/rectangulo")),
                                                border_radius=10,
                                                margin=5,
                                            ),
                                            ft.Container(
                                                content=ft.ElevatedButton("Ir al trapecio", on_click=lambda _: page.go("/trapecio")),
                                                border_radius=10,
                                                margin=5,
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        spacing=10,
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=page.bgcolor,
                            expand=True,
                        ),
                    ]
                )
            )
        # Se genera la vista de cuadrado
        elif page.route == "/cuadrado":
            txtLado = ft.TextField(label="Ingresa el valor del lado del cuadrado", color="red")
            lblAreaC = ft.Text("Resultado: ", color="red")
            
            def CalcularCuadrado(e):
                try:
                    lado = float(txtLado.value)
                    AreaC = lado * lado
                    lblAreaC.value = f"El área del cuadrado es: {AreaC}"
                    page.update()
                except ValueError:
                    lblAreaC.value = "Por favor, ingresa un número válido."
                    page.update()
            
            page.views.append(
                ft.View(
                    "/cuadrado",
                    [
                        ft.AppBar(title=ft.Text("Área del cuadrado", color="green"), bgcolor="orange"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txtLado,
                                    ft.Container(
                                        content=ft.ElevatedButton("Calcular área", on_click=CalcularCuadrado),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                    lblAreaC,
                                    ft.Container(
                                        content=ft.ElevatedButton("Ir al inicio", on_click=lambda _: page.go("/")),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=page.bgcolor,
                            expand=True,
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Se genera la vista de círculo 
        elif page.route == "/circulo":
            txtRadio = ft.TextField(label="Ingresa el valor del radio del círculo", color="red")
            lblAreaCi = ft.Text("Resultado: ", color="red")
            
            def CalcularCirculo(e):
                try:
                    radio = float(txtRadio.value)
                    AreaCi = 3.1416 * radio * radio
                    lblAreaCi.value = f"El área del círculo es: {AreaCi}"
                    page.update()
                except ValueError:
                    lblAreaCi.value = "Por favor, ingresa un número válido."
                    page.update()
            
            page.views.append(
                ft.View(
                    "/circulo",
                    [
                        ft.AppBar(title=ft.Text("Área del círculo", color="green"), bgcolor="pink"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txtRadio,
                                    ft.Container(
                                        content=ft.ElevatedButton("Calcular área", on_click=CalcularCirculo),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                    lblAreaCi,
                                    ft.Container(
                                        content=ft.ElevatedButton("Ir al inicio", on_click=lambda _: page.go("/")),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=page.bgcolor,
                            expand=True,
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Se genera la vista de triángulo
        elif page.route == "/triangulo":
            txtBase = ft.TextField(label="Ingresa el valor de la base del triángulo", color="blue")
            txtAltura = ft.TextField(label="Ingresa el valor de la altura del triángulo", color="blue")
            lblAreaT = ft.Text("Resultado: ", color="red")
            
            def CalcularTriangulo(e):
                try:
                    base = float(txtBase.value)
                    altura = float(txtAltura.value)
                    AreaT = (base * altura) / 2
                    lblAreaT.value = f"El área del triángulo es: {AreaT}"
                    page.update()
                except ValueError:
                    lblAreaT.value = "Por favor, ingresa un número válido."
                    page.update()
            
            page.views.append(
                ft.View(
                    "/triangulo",
                    [
                        ft.AppBar(title=ft.Text("Área del triángulo", color="yellow"), bgcolor="blue"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txtBase,
                                    txtAltura,
                                    ft.Container(
                                        content=ft.ElevatedButton("Calcular área", on_click=CalcularTriangulo),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                    lblAreaT,
                                    ft.Container(
                                        content=ft.ElevatedButton("Ir al inicio", on_click=lambda _: page.go("/")),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=page.bgcolor,
                            expand=True,
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Se genera la vista de rectángulo
        elif page.route == "/rectangulo":
            txtBaseR = ft.TextField(label="Ingresa el valor de la base del rectángulo", color="blue")
            txtAlturaR = ft.TextField(label="Ingresa el valor de la altura del rectángulo", color="blue")
            lblAreaR = ft.Text("Resultado: ", color="red")
            
            def CalcularRectangulo(e):
                try:
                    baseR = float(txtBaseR.value)
                    alturaR = float(txtAlturaR.value)
                    AreaR = baseR * alturaR
                    lblAreaR.value = f"El área del rectángulo es: {AreaR}"
                    page.update()
                except ValueError:
                    lblAreaR.value = "Por favor, ingresa un número válido."
                    page.update()
            
            page.views.append(
                ft.View(
                    "/rectangulo",
                    [
                        ft.AppBar(title=ft.Text("Área del rectángulo", color="yellow"), bgcolor="purple"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txtBaseR,
                                    txtAlturaR,
                                    ft.Container(
                                        content=ft.ElevatedButton("Calcular área", on_click=CalcularRectangulo),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                    lblAreaR,
                                    ft.Container(
                                        content=ft.ElevatedButton("Ir al inicio", on_click=lambda _: page.go("/")),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=page.bgcolor,
                            expand=True,
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Se genera la vista de trapecio
        elif page.route == "/trapecio":
            txtBase1 = ft.TextField(label="Ingresa el valor de la base mayor del trapecio", color="blue")
            txtBase2 = ft.TextField(label="Ingresa el valor de la base menor del trapecio", color="blue")
            txtAlturaT = ft.TextField(label="Ingresa el valor de la altura del trapecio", color="blue")
            lblAreaTr = ft.Text("Resultado: ", color="red")
            
            def CalcularTrapecio(e):
                try:
                    base1 = float(txtBase1.value)
                    base2 = float(txtBase2.value)
                    alturaT = float(txtAlturaT.value)
                    AreaTr = ((base1 + base2) * alturaT) / 2
                    lblAreaTr.value = f"El área del trapecio es: {AreaTr}"
                    page.update()
                except ValueError:
                    lblAreaTr.value = "Por favor, ingresa un número válido."
                    page.update()
            
            page.views.append(
                ft.View(
                    "/trapecio",
                    [
                        ft.AppBar(title=ft.Text("Área del trapecio", color="yellow"), bgcolor="red"),
                        ft.Container(
                            content=ft.Column(
                                [
                                    txtBase1,
                                    txtBase2,
                                    txtAlturaT,
                                    ft.Container(
                                        content=ft.ElevatedButton("Calcular área", on_click=CalcularTrapecio),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                    lblAreaTr,
                                    ft.Container(
                                        content=ft.ElevatedButton("Ir al inicio", on_click=lambda _: page.go("/")),
                                        border_radius=10,
                                        margin=5,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            bgcolor=page.bgcolor,
                            expand=True,
                        ),
                    ],
                    bgcolor=page.bgcolor
                )
            )    
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main)
#ft.app(target=main,view=ft.WEB_BROWSER)
