import sys
sys.path.append("src")
from src.model import pension_prueba

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculadorPensional(App):

    def build(self):
        contenedor = BoxLayout(orientation = "vertical")

        etiqueta_edad= Label(text="Edad")
        etiqueta_semanas_cotizadas= Label(text="Semanas cotizadas")
        etiqueta_salario_promedio= Label(text="Salario promedio")
        etiqueta_saldo_acumulado= Label(text="Saldo acumulado")

        contenedor.add_widget(etiqueta_edad)
        self.valor_edad = TextInput()
        contenedor.add_widget(self.valor_edad)

        contenedor.add_widget(etiqueta_semanas_cotizadas)
        self.valor_semanas_cotizadas = TextInput()
        contenedor.add_widget(self.valor_semanas_cotizadas)

        contenedor.add_widget(etiqueta_saldo_acumulado)
        self.valor_saldo_acumulado = TextInput()
        contenedor.add_widget(self.valor_saldo_acumulado)

        contenedor.add_widget(etiqueta_salario_promedio)
        self.valor_salario_promedio = TextInput()   
        contenedor.add_widget(self.valor_salario_promedio)

        boton_calcular = Button(text="Calcular")
        boton_calcular.bind(on_press=self.calcular_pension)
        contenedor.add_widget(boton_calcular)


        self.etiqueta_resultado = Label(text="Resultado")
        contenedor.add_widget(self.etiqueta_resultado)

        return contenedor

    def calcular_pension(self, boton):
        try:
            edad = int(self.valor_edad.text)
            semanas_cotizadas = int(self.valor_semanas_cotizadas.text)
            saldo_acumulado = float(self.valor_saldo_acumulado.text)
            salario_promedio = float(self.valor_salario_promedio.text)

            # Puedes ajustar los valores de reemplazo, entidad y factor según tu lógica
            reemplazo = 0.65  # ejemplo
            entidad = "Colpensiones"  # ejemplo
            factor = 20  # ejemplo para privado

            # Ejemplo usando Colpensiones
            resultado = pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas_cotizadas, edad, entidad)
            self.etiqueta_resultado.text = f"Pensión estimada: {resultado}"
        except Exception as e:
            self.etiqueta_resultado.text = f"Error: {str(e)}"

app = CalculadorPensional()
app.run()
