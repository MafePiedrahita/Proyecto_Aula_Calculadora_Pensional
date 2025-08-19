import sys 
sys.path.append("src")

from model import Pension_prueba  


try: 
#leer entradas 
    sexo=str(input("Ingrese su genero: "))
    edad=int(input("Ingrese su edad: "))
    semanas=int(input("Ingrese si tiene semanas cotizadas: "))
    salario_promedio=int(input("Ingrese su salaio promedio: "))
    saldo_acomulado=int(input("Ingrese el saldo acomulado si su entidad es privada: "))

except ValueError as error_valores:
    ...

except ValueError as e:
    ... 

