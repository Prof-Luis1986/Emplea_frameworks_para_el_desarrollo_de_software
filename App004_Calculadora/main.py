import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"
  

def  calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1-num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"
   
    

def calc_mult(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1*num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"
    

def calc_div(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1/num2
        lblResultado.value=f"Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error Ingresa valores correctos"





def main(page:ft.Page):

    
    #Configuración basica de la ventana 
    page.title="Calculadora"
    page.bgcolor="#0CCB72"


    #Creación de componentes de la interfaz
    txtNum1=ft.TextField(label="Ingresa el primer numero", color="red")
    txtNum2=ft.TextField(label="Ingresa el segundo numero", color="red")
    lblResultado=ft.Text("Resultado: ",color="red")
    


    # Funciones de manejo de eventos
    def on_calc_suma(e):
        calc_suma(txtNum1, txtNum2, lblResultado)
        page.update()

    def on_calc_resta(e):
        calc_resta(txtNum1, txtNum2, lblResultado)
        page.update()

    def on_calc_mult(e):
        calc_mult(txtNum1, txtNum2, lblResultado)
        page.update()

    def on_calc_div(e):
        calc_div(txtNum1, txtNum2, lblResultado)
        page.update()

    def limpiar(e):
        txtNum1.value = ""
        txtNum2.value = ""
        lblResultado.value = "Resultado: "
        page.update()


    #Se crean los botones de la aplicación
    btnSuma=ft.ElevatedButton(text="+",on_click=on_calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=on_calc_resta)
    btnMult=ft.ElevatedButton(text="X",on_click=on_calc_mult)
    btnDiv=ft.ElevatedButton(text="/",on_click=on_calc_div)
    btnLimpiar=ft.ElevatedButton(text="Borrar",on_click=limpiar)






    #Agregar los elementos a pages
    page.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1,
                txtNum2
            ],alignment="center")
        ]),
        ft.Row(controls=[lblResultado],alignment="center"),
        ft.Row(controls=[
            btnSuma,
            btnResta,
            btnMult,
            btnDiv,
            btnLimpiar
        ],alignment="center")
    )

ft.app(target=main)