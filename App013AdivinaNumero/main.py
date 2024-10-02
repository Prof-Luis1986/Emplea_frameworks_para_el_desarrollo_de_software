import flet as ft
import random

# Función para manejar la adivinanza del usuario
def verificar_adivinanza(e, page):
    adivinanza_usuario = int(entrada_numero.value)
    
    if adivinanza_usuario == numero_secreto:
        texto_resultado.value = "¡Correcto! Adivinaste el número."
        boton_adivinar.disabled = True
        page.add(ft.Audio(src="Victoria.mp3", autoplay=True))  # Sonido de acierto
    elif adivinanza_usuario < numero_secreto:
        texto_resultado.value = "El número es mayor. Intenta nuevamente."
        page.add(ft.Audio(src="Boing.mp3", autoplay=True))  # Sonido de error
    else:
        texto_resultado.value = "El número es menor. Intenta nuevamente."
        page.add(ft.Audio(src="Boing.mp3", autoplay=True))  # Sonido de error

    entrada_numero.value = ""  # Limpiar el campo de entrada
    page.update()

# Función principal para inicializar la aplicación
def main(page: ft.Page):
    global numero_secreto, entrada_numero, texto_resultado, boton_adivinar

    page.title = "Juego: Adivina el número"

    # Generar un número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    # Crear los elementos de la interfaz
    titulo = ft.Text("Adivina el número entre 1 y 100", size=20, color="white")
    entrada_numero = ft.TextField(label="Tu adivinanza", width=150)
    boton_adivinar = ft.ElevatedButton("Adivinar", on_click=lambda e: verificar_adivinanza(e, page))
    texto_resultado = ft.Text("", color="white")

    # Crear el contenedor principal con fondo negro
    contenedor_principal = ft.Container(
        content=ft.Column(
            controls=[
                titulo,
                entrada_numero,
                boton_adivinar,
                texto_resultado,
                ft.Image(
                    src="https://i.ibb.co/Gxgryg9/laser.gif",
                    fit=ft.ImageFit.COVER,
                    width=300,  # Ajusta el tamaño según lo necesites
                    height=150,  # Ajusta el tamaño según lo necesites
                )
            ],
            alignment="center",  # Centrar controles verticalmente
            horizontal_alignment="center",  # Centrar controles horizontalmente
            spacing=20,  # Espacio entre controles
        ),
        bgcolor=ft.colors.BLACK,  # Fondo negro
        width=page.window.width,
        height=page.window.height,
        padding=20  # Espacio interno para evitar que los controles lleguen a los bordes
    )

    # Añadir el contenedor principal a la página
    page.add(contenedor_principal)

# Iniciar la aplicación de Flet
ft.app(target=main)
