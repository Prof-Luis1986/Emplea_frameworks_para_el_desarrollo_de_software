import flet as ft

def main(page: ft.Page):
    # Establecer el tamaño por defecto de la ventana
    page.window_width = 800
    page.window_height = 800

    # Audios
    intro = ft.Audio(
        src="Intro.mp3", volume=1, balance=0
    )
    page.overlay.append(intro)
    
    Nivel1 = ft.Audio(
        src="Primer_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel1)
    
    Nivel2 = ft.Audio(
        src="Segundo_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel2)
    
    Nivel3 = ft.Audio(
        src="Tercer_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel3)
    
    Nivel4 = ft.Audio(
        src="Cuarto_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel4)
    
    Nivel5 = ft.Audio(
        src="Quinto_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel5)
    
    Nivel6 = ft.Audio(
        src="Sexto_Nivel.mp3", volume=1, balance=0 
    )
    page.overlay.append(Nivel6)
    
    Nivel7 = ft.Audio(
        src="Septimo_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel7)
    
    Nivel8 = ft.Audio(
        src="Octavo_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel8)
    
    Nivel9 = ft.Audio(
        src="Noveno_Nivel.mp3", volume=1, balance=0
    )
    page.overlay.append(Nivel9)
   
    # Configuración de la página
    page.title = "El Mictlan"
    page.bgcolor = "#000000"
    page.fgcolor = "#FFFFFF"
    
    # Tamaño uniforme para todas las imágenes
    image_width = 150
    image_height = 150
    
    # Función para detener todos los audios
    def stop_all():
        intro.pause()
        Nivel1.pause()
        Nivel2.pause()
        Nivel3.pause()
        Nivel4.pause()
        Nivel5.pause()
        Nivel6.pause()
        Nivel7.pause()
        Nivel8.pause()
        Nivel9.pause()
        
    def play_intro(e):
        stop_all()
        intro.play()    

    def play_nivel1(e):
        stop_all()
        Nivel1.play()

    def play_nivel2(e):
        stop_all()
        Nivel2.play()

    def play_nivel3(e):
        stop_all()
        Nivel3.play()

    def play_nivel4(e):
        stop_all()
        Nivel4.play()

    def play_nivel5(e):
        stop_all()
        Nivel5.play()

    def play_nivel6(e):
        stop_all()
        Nivel6.play()

    def play_nivel7(e):
        stop_all()
        Nivel7.play()

    def play_nivel8(e):
        stop_all()
        Nivel8.play()

    def play_nivel9(e):
        stop_all()
        Nivel9.play()

    # Creación de componentes de la interfaz
    
    btnIntro = ft.FilledButton(text="Escucha el intro", disabled=False, on_click=play_intro)
    
    btnNivel1 = ft.ElevatedButton(text="Primer Nivel", on_click=play_nivel1)
    img1 = ft.Image(
        src="Primer-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )
   
    btnNivel2 = ft.ElevatedButton(text="Segundo Nivel", on_click=play_nivel2)
    img2 = ft.Image(
        src="Segundo-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )
   
    btnNivel3 = ft.ElevatedButton(text="Tercer Nivel", on_click=play_nivel3)
    img3 = ft.Image(
        src="Tercer-Nivel.png", 
        width=image_width, height=image_height, fit="contain"
    )
    
    btnNivel4 = ft.ElevatedButton(text="Cuarto Nivel", on_click=play_nivel4)
    img4 = ft.Image(
        src="Cuarto-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )
   
    btnNivel5 = ft.ElevatedButton(text="Quinto Nivel", on_click=play_nivel5)
    img5 = ft.Image(
        src="Quinto-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )
    
    btnNivel6 = ft.ElevatedButton(text="Sexto Nivel", on_click=play_nivel6)
    img6 = ft.Image(
        src="Sexto-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )
   
    btnNivel7 = ft.ElevatedButton(text="Séptimo Nivel", on_click=play_nivel7)
    img7 = ft.Image(
        src="Septimo-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )
   
    btnNivel8 = ft.ElevatedButton(text="Octavo Nivel", on_click=play_nivel8)
    img8 = ft.Image(
        src="Octavo-Nivel.png", 
        width=image_width, height=image_height, fit="contain"
    )
   
    btnNivel9 = ft.ElevatedButton(text="Noveno Nivel", on_click=play_nivel9)
    img9 = ft.Image(
        src="Noveno-Nivel.jpeg", 
        width=image_width, height=image_height, fit="contain"
    )

    # Añadir el botón de música a la primera fila
    page.add(
        ft.Row(
            alignment="start",  # Alineación a la izquierda
            controls=[
                btnIntro  # Botón de música alineado a la izquierda
            ]
        )
    )

    # Crear un Column con la propiedad scroll
    scroll_column = ft.Column(
        alignment="center",
        spacing=10,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Row(
                alignment="center",
                spacing=10,
                controls=[
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel1, img1]),
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel2, img2]),
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel3, img3])
                ]
            ),
            ft.Row(
                alignment="center",
                spacing=10,
                controls=[
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel4, img4]),
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel5, img5]),
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel6, img6])
                ]
            ),
            ft.Row(
                alignment="center",
                spacing=10,
                controls=[
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel7, img7]),
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel8, img8]),
                    ft.Column(alignment="center", spacing=10, controls=[btnNivel9, img9])
                ]
            )
        ]
    )
    
    page.add(scroll_column)

ft.app(target=main)

