import flet as ft

def calcular_suma(txt_num1, txt_num2, txt_resultado):
    try:
        num1 = float(txt_num1.value.strip())
        num2 = float(txt_num2.value.strip())
        resultado = num1 + num2
        txt_resultado.value = f"Resultado: {resultado}"
    except ValueError:
        txt_resultado.value = "Error: Ingresa valores correctos"

def main(page: ft.Page):
    # Configuración básica de la ventana
    page.title = "Suma2Numeros"
    page.bgcolor = "yellow"  # Cambia el color de fondo de la ventana

    # Creación de componentes de la interfaz
    txt_num1 = ft.TextField(label="Ingresa el primer número", color="green")
    txt_num2 = ft.TextField(label="Ingresa el segundo número", color="green")
    txt_resultado = ft.Text("Resultado: ", color="green")
    
    # Función para manejar el clic en el botón Calcular
    def on_calcular_click(e):
        calcular_suma(txt_num1, txt_num2, txt_resultado)
        page.update()  # Actualizar la página después de calcular

    # Función para limpiar los campos
    def limpiar(e):
        txt_num1.value = ""
        txt_num2.value = ""
        txt_resultado.value = "Resultado: "
        page.update()  # Actualizar la página después de limpiar

    # Creación de botones
    btn_calcular = ft.ElevatedButton(text="Calcular", on_click=on_calcular_click)
    btn_limpiar = ft.ElevatedButton(text="Borrar", on_click=limpiar)

    # Agregar los componentes a la página usando Column y Row
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[txt_num1, txt_num2], alignment="center"),  # Centrar horizontalmente los TextField
            ft.Row(controls=[txt_resultado], alignment="center"),  # Centrar horizontalmente el txt_resultado
            ft.Row(controls=[btn_calcular, btn_limpiar], alignment="center")  # Centrar horizontalmente los botones
        ])
    )

# Aplicación en el escritorio
ft.app(target=main)
#Aplicación en el navegador
#ft.app(target=main,view=ft.WEB_BROWSER)