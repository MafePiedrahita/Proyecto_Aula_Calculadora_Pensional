def calcular_pension(salario, semanas, edad, regimen):
    if regimen == "colpensiones":
        # fórmula ejemplo básica
        if semanas < 1300:
            return "No cumple con las semanas mínimas 1300"
        pension = salario * 0.65
    else:
        # fondos privados
        pension = salario * 0.55

    return round(pension, 2)
