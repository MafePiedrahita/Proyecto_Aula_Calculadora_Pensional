from datetime import date
from typing import Optional

from src.model.entities.aportante import Aportante
from src.controller import aportante_controller as ac
from src.service.simulacion_service import estimar_publico, estimar_privado


def _leer_int(msg: str, minimo: Optional[int] = None) -> int:
    while True:
        try:
            v = int(input(msg).strip())
            if minimo is not None and v < minimo:
                print(f"✖ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("✖ Ingresa un número entero válido.")


def _leer_float(msg: str, minimo: Optional[float] = None) -> float:
    while True:
        try:
            v = float(input(msg).strip())
            if minimo is not None and v < minimo:
                print(f"✖ Debe ser ≥ {minimo}")
                continue
            return v
        except ValueError:
            print("✖ Ingresa un número válido (usa punto como decimal).")


def _leer_fecha_iso(msg: str) -> date:
    while True:
        try:
            return date.fromisoformat(input(msg).strip())
        except ValueError:
            print("✖ Formato inválido. Usa YYYY-MM-DD (ej: 1990-05-01).")


def _pausa():
    input("\nPresiona ENTER para continuar...")


def _mostrar_aportante(ap: Aportante | None):
    if not ap:
        print("No encontrado.")
        return
    print("\n--- Aportante ---")
    print(f"ID:            {ap.aportante_id}")
    print(f"Tipo doc:      {ap.tipo_doc}")
    print(f"Nro doc:       {ap.nro_doc}")
    print(f"Nombres:       {ap.nombres}")
    print(f"Apellidos:     {ap.apellidos}")
    print(f"Fecha nac:     {ap.fecha_nac}")
    print(f"Salario prom:  {ap.salario_prom}")
    print(f"Semanas cot:   {ap.semanas_cot}")
    print(f"Edad:          {ap.edad}")


def _crear_aportante():
    print("\n=== Crear aportante ===")
    tipo = input("Tipo doc (CC/CE/TI/PA): ").strip().upper()
    nro = input("Nro doc: ").strip()
    nombres = input("Nombres: ").strip()
    apellidos = input("Apellidos: ").strip()
    fecha_nac = _leer_fecha_iso("Fecha nac (YYYY-MM-DD): ")
    salario = _leer_float("Salario promedio: ", minimo=0.0)
    semanas = _leer_int("Semanas cotizadas: ", minimo=0)
    edad = _leer_int("Edad: ", minimo=0)

    ap = Aportante(None, tipo, nro, nombres, apellidos, fecha_nac, salario, semanas, edad)
    ap_id = ac.crear(ap)
    print(f"✔ Aportante creado con id={ap_id}")


def _buscar_por_id():
    print("\n=== Buscar aportante por ID ===")
    ap_id = _leer_int("ID: ", minimo=1)
    _mostrar_aportante(ac.buscar_por_id(ap_id))


def _buscar_por_nro_doc():
    print("\n=== Buscar aportante por nro_doc ===")
    nro = input("Nro doc: ").strip()
    ap = ac.buscar_por_nro_doc(nro) if hasattr(ac, "buscar_por_nro_doc") else None
    if ap is None:
        # fallback: si no implementaste buscar_por_nro_doc en el controller,
        # se trae por una consulta directa (opcional). Recomendado implementarlo en el controller.
        print("Esta opción requiere implementar 'buscar_por_nro_doc' en aportante_controller.")
    _mostrar_aportante(ap)


def _actualizar_salario():
    print("\n=== Actualizar salario promedio ===")
    ap_id = _leer_int("ID aportante: ", minimo=1)
    nuevo = _leer_float("Nuevo salario: ", minimo=0.0)
    filas = ac.actualizar_salario(ap_id, nuevo)
    if filas == 1:
        print("✔ Salario actualizado.")
    else:
        print("✖ No se actualizó (¿ID inexistente?).")


def _eliminar_aportante():
    print("\n=== Eliminar aportante ===")
    ap_id = _leer_int("ID: ", minimo=1)
    conf = input("¿Seguro? (S/N): ").strip().upper()
    if conf == "S":
        filas = ac.eliminar(ap_id)
        if filas == 1:
            print("✔ Eliminado.")
        else:
            print("✖ No se eliminó (¿ID inexistente?).")
    else:
        print("Operación cancelada.")


def _simular_publico():
    print("\n=== Simular pensión (Público / RPM) ===")
    ap_id = _leer_int("ID aportante: ", minimo=1)
    tasa = _leer_float("Tasa de reemplazo (ej 0.65): ", minimo=0.0)
    sim_id = estimar_publico(ap_id, tasa)
    print(f"✔ Simulación creada (Público). ID simulación: {sim_id}")


def _simular_privado():
    print("\n=== Simular pensión (Privado / RAIS) ===")
    ap_id = _leer_int("ID aportante: ", minimo=1)
    saldo = _leer_float("Saldo acumulado: ", minimo=0.0)
    factor = _leer_float("Factor renta (p.ej 240): ", minimo=1.0)
    sim_id = estimar_privado(ap_id, saldo, factor)
    print(f"✔ Simulación creada (Privado). ID simulación: {sim_id}")


def run():
    while True:
        print("\n==============================")
        print("  Calculadora Pensional (CLI) ")
        print("==============================")
        print("1) Crear aportante")
        print("2) Buscar aportante por ID")
        print("3) Actualizar salario")
        print("4) Eliminar aportante")
        print("5) Simular pensión (Público/RPM)")
        print("6) Simular pensión (Privado/RAIS)")
        # Extras opcionales:
        # print("7) Buscar aportante por nro_doc")
        print("0) Salir")
        op = input("Opción: ").strip()

        try:
            if op == "1":
                _crear_aportante(); _pausa()
            elif op == "2":
                _buscar_por_id(); _pausa()
            elif op == "3":
                _actualizar_salario(); _pausa()
            elif op == "4":
                _eliminar_aportante(); _pausa()
            elif op == "5":
                _simular_publico(); _pausa()
            elif op == "6":
                _simular_privado(); _pausa()
            elif op == "7":
                _buscar_por_nro_doc(); _pausa()
            elif op == "0":
                print("Hasta pronto 👋")
                break
            else:
                print("✖ Opción inválida.")
        except Exception as e:
            print(f"✖ Error: {e}")
            _pausa()
