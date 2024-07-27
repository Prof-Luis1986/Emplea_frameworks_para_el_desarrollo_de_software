import flet as ft
from flet import AppBar, ElevatedButton, View

def main(page: ft.Page):
    page.title = "La historia de la Informática"
    page.bgcolor = "#61A707"
    page.window_width = 600
    page.window_height = 800
    
    image_width_Portada = 800
    image_height_Portada = 400
    
    img_height = 100
    img_width = 100
    
    # Audios Padres de la informática
    intro = ft.Audio(src="Intro.mp3", volume=1, balance=0)
    page.overlay.append(intro)
    
    Pascal = ft.Audio(src="Pascal.mp3", volume=1, balance=0)
    page.overlay.append(Pascal)
    
    Leibniz = ft.Audio(src="Leibniz.mp3", volume=1, balance=0)
    page.overlay.append(Leibniz)
    
    Babbage = ft.Audio(src="Babbage.mp3", volume=1, balance=0)
    page.overlay.append(Babbage)
    
    Lovelace = ft.Audio(src="Lovelace.mp3", volume=1, balance=0) 
    page.overlay.append(Lovelace)
    
    Hollerith = ft.Audio(src="Hollerith.mp3", volume=1, balance=0)
    page.overlay.append(Hollerith)
    
    Turing = ft.Audio(src="Turing.mp3", volume=1, balance=0)
    page.overlay.append(Turing)
    
    Neumann = ft.Audio(src="Neumann.mp3", volume=1, balance=0)
    page.overlay.append(Neumann)
    
    Shannon = ft.Audio(src="Shannon.mp3", volume=1, balance=0)
    page.overlay.append(Shannon)
    
    Hopper = ft.Audio(src="Hopper.mp3", volume=1, balance=0)   
    page.overlay.append(Hopper)
    
    McCarthy = ft.Audio(src="McCarthy.mp3", volume=1, balance=0)
    page.overlay.append(McCarthy)
    
    Berners = ft.Audio(src="Berners.mp3", volume=1, balance=0)
    page.overlay.append(Berners)
    
    Ritchie = ft.Audio(src="Ritchie.mp3", volume=1, balance=0)
    page.overlay.append(Ritchie)
    
    Thompson = ft.Audio(src="Thompson.mp3", volume=1, balance=0)
    page.overlay.append(Thompson)
    
    def StopAll():
        intro.pause()
        Pascal.pause()
        Leibniz.pause()
        Babbage.pause()
        Lovelace.pause()
        Hollerith.pause()
        Turing.pause()
        Neumann.pause()
        Shannon.pause()
        Hopper.pause()
        McCarthy.pause()
        Berners.pause()
        Ritchie.pause()
        Thompson.pause()
    
    def play_intro(e):
        StopAll()
        intro.play()
        
    def play_pascal(e):
        StopAll()
        Pascal.play()
        
    def play_leibniz(e):
        StopAll()
        Leibniz.play()
        
    def play_babbage(e):
        StopAll()
        Babbage.play()
        
    def play_lovelace(e):    
        StopAll()
        Lovelace.play()
        
    def play_hollerith(e):
        StopAll()
        Hollerith.play()
        
    def play_turing(e):
        StopAll()
        Turing.play()
    
    def play_neumann(e):
        StopAll()
        Neumann.play()
        
    def play_shannon(e):
        StopAll()
        Shannon.play()
    
    def play_hopper(e):
        StopAll()
        Hopper.play()
    
    def play_mccarthy(e):
        StopAll()
        McCarthy.play()
    
    def play_berners(e):
        StopAll()
        Berners.play()
    
    def play_ritchie(e):
        StopAll()
        Ritchie.play()
        
    def play_thompson(e):
        StopAll()
        Thompson.play()
    
    # Botones Padres de la informática con imágenes
    btn1 = ElevatedButton(content=ft.Image(src="Pascal.jpeg", width=img_width, height=img_height), on_click=play_pascal)
    btn2 = ElevatedButton(content=ft.Image(src="Leibniz.png", width=img_width, height=img_height), on_click=play_leibniz)
    btn3 = ElevatedButton(content=ft.Image(src="babbage.png", width=img_width, height=img_height), on_click=play_babbage)
    btn4 = ElevatedButton(content=ft.Image(src="Lovelace.png", width=img_width, height=img_height), on_click=play_lovelace)
    btn5 = ElevatedButton(content=ft.Image(src="Hollerith.png", width=img_width, height=img_height), on_click=play_hollerith)
    btn6 = ElevatedButton(content=ft.Image(src="Turing.jpeg", width=img_width, height=img_height), on_click=play_turing)
    btn7 = ElevatedButton(content=ft.Image(src="Neumann.jpeg", width=img_width, height=img_height), on_click=play_neumann)
    btn8 = ElevatedButton(content=ft.Image(src="Shannon.png", width=img_width, height=img_height), on_click=play_shannon)
    btn9 = ElevatedButton(content=ft.Image(src="Hopper.png", width=img_width, height=img_height), on_click=play_hopper)
    btn10 = ElevatedButton(content=ft.Image(src="McCarthy.jpeg", width=img_width, height=img_height), on_click=play_mccarthy)
    btn11 = ElevatedButton(content=ft.Image(src="Berners.jpeg", width=img_width, height=img_height), on_click=play_berners)
    btn12 = ElevatedButton(content=ft.Image(src="Ritchie.png", width=img_width, height=img_height), on_click=play_ritchie)
    btn13 = ElevatedButton(content=ft.Image(src="Thompson.jpeg", width=img_width, height=img_height), on_click=play_thompson)
    
    # Manejo del cambio de ruta
    def route_change(route):
        # Limpia las vistas anteriores
        page.views.clear()
        
        # Vista de portada
        if page.route == '/':
            page.views.append(
                View(
                    "/",
                    controls=[
                        AppBar(
                            title=ft.Text("La historia de la Informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: [StopAll(), page.go('/padres')]
                                    ),
                                    ft.Image(
                                        src="Portada.png",
                                        width=image_width_Portada,
                                        height=image_height_Portada,
                                        fit="cover"
                                    ),
                                    ElevatedButton(
                                        "Escucha el intro",
                                        on_click=play_intro
                                    ),
                                    
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ],
                    bgcolor=page.bgcolor
                )
            )
        # Vista de los padres de la informática
        elif page.route == '/padres':
            page.views.append(
                View(
                    "/padres",
                    controls=[
                        AppBar(
                            title=ft.Text("Los padres de la informática"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                            btn1, btn2, btn3
                                        ]
                                    ),
                                    ft.Row(
                                      alignment="center",
                                      controls=[
                                        btn4, btn5, btn6
                                      ]  
                                    ),
                                    ft.Row(
                                       alignment="center",
                                        controls=[
                                          btn7, btn8, btn9
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn10, btn11, btn12
                                        ] 
                                    ),
                                    ft.Row(
                                        alignment="center",
                                        controls=[
                                          btn13
                                        ] 
                                    ),
                                     ElevatedButton(
                                        'La evolución de los lenguajes de programación',
                                        on_click=lambda _: page.go('/lenguajes')
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
        # Vista de la evolución de los lenguajes de programación
        elif page.route == '/lenguajes':
            page.views.append(
                View(
                    "/lenguajes",
                    controls=[
                        AppBar(
                            title=ft.Text("La evolución de los lenguajes de programación"),
                            bgcolor="gray"
                        ),
                        ft.Container(
                            ft.Column(
                                controls=[
                                    ElevatedButton(
                                        'Volver al inicio',
                                        on_click=lambda _: page.go('/')
                                    ),
                                    ElevatedButton(
                                        'Los padres de la informática',
                                        on_click=lambda _: page.go('/padres')
                                    ),
                                    # Aquí puedes agregar el contenido específico para la sección de lenguajes de programación
                                ],
                                alignment=ft.MainAxisAlignment.START
                            ),
                            bgcolor=page.bgcolor,
                            expand=True
                        )
                    ]
                )
            )
            
        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
