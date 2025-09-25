import sys 
sys.path.append("src")

from model import pension_prueba  


try: 
#leer entradas 
    sexo=str(input("Ingrese su genero: "))
    edad=int(input("Ingrese su edad: "))
    semanas=int(input("Ingrese si tiene semanas cotizadas: "))
    salario_promedio=int(input("Ingrese su salaio promedio: "))
    saldo_acomulado=int(input("Ingrese el saldo acomulado si su entidad es privada: "))

    pension_mensual = pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, semanas, edad)
    print(pension_mensual)

except ValueError as Error:
    print("No puede calcular la pension mensual:" + str(Error))

except ValueError as e:
    ... 

