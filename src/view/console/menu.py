# view/console/menu.py
from datetime import date
from src.model.entities.aportante import Aportante
from src.controller import aportante_controller as ac
from src.service.simulacion_service import estimar_publico, estimar_privado

def run():
    while True:
        print("\n=== Calculadora Pensional (Consola) ===")
        print("1) Insertar Aportante")
        print("2) Buscar Aportante por ID")
        print("3) Actualizar salario de Aportante")
        print("4) Eliminar Aportante")
        print("5) Simular pensión (Público)")
        print("6) Simular pensión (Privado)")
        print("0) Salir")
        op = input("Opción: ").strip()

        try:
            if op == "1":
                ap = Aportante(
                    None,
                    input("Tipo doc (CC/CE/TI/PA): ").strip().upper(),
                    input("Nro doc: ").strip(),
                    input("Nombres: ").strip(),
                    input("Apellidos: ").strip(),
                    date.fromisoformat(input("Fecha nac (YYYY-MM-DD): ").strip()),
                    float(input("Salario promedio: ").strip()),
                    int(input("Semanas cotizadas: ").strip()),
                    int(input("Edad: ").strip())
                )
                ap_id = ac.crear(ap)
                print(f"✔ Aportante creado id={ap_id}")

            elif op == "2":
                ap = ac.buscar_por_id(int(input("ID: ")))
                print(ap if ap else "No existe")

            elif op == "3":
                rows = ac.actualizar_salario(
                    int(input("ID: ")),
                    float(input("Nuevo salario: "))
                )
                print(f"Filas afectadas: {rows}")

            elif op == "4":
                rows = ac.eliminar(int(input("ID: ")))
                print(f"Filas afectadas: {rows}")

            elif op == "5":
                sim_id = estimar_publico(int(input("ID aportante: ")), 0.65)
                print(f"✔ Simulación Público creada id={sim_id}")

            elif op == "6":
                sim_id = estimar_privado(
                    int(input("ID aportante: ")),
                    float(input("Saldo acumulado: ")),
                    240
                )
                print(f"✔ Simulación Privado creada id={sim_id}")

            elif op == "0":
                break
            else:
                print("Opción inválida.")
        except Exception as e:
            print(f"✖ Error: {e}")
