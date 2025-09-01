import unittest
from model import Pension_prueba


class PruebasPension(unittest.TestCase):

    # ------- Colpensiones -------

    def test_normal_1(self):
        edad = 62
        semanas = 1300
        salario_promedio = 3_000_000
        reemplazo = 0.65
        entidad = "Colpensiones"

        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(
            salario_promedio, reemplazo, semanas, edad, entidad
        )

        pension_esperada = 1_950_000
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    def test_extraordinario_1(self):
        edad = 57
        semanas = 1000
        salario_promedio = 2_000_000
        reemplazo = 0.65
        entidad = "Colpensiones"

        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(
            salario_promedio, reemplazo, semanas, edad, entidad
        )

        pension_esperada = 1_300_000
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    def test_ideal_1(self):
        edad = 62
        semanas = 1800
        salario_promedio = 4_000_000
        reemplazo = 0.80
        entidad = "Colpensiones"

        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(
            salario_promedio, reemplazo, semanas, edad, entidad
        )

        pension_esperada = 3_200_000
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    def test_extraordinario_4(self):
        edad = 62
        semanas = 2200
        salario_promedio = 30_000_000
        reemplazo = 0.80
        entidad = "Colpensiones"

        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(
            salario_promedio, reemplazo, semanas, edad, entidad
        )

        pension_esperada = 24_000_000
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    # ------- Privado -------

    def test_normal_privada_2(self):
        edad = 62
        saldo_acumulado = 350_000_000
        entidad = "Porvenir"
        factor = 171

        pension_mensual = Pension_prueba.calcular_pension_privado(
            saldo_acumulado, factor, edad, entidad
        )

        pension_esperada = 2_046_783.63  # 350,000,000 / 171
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=2)

    def test_normal_privada_3(self):
        edad = 57
        saldo_acumulado = 280_000_000
        entidad = "Porvenir"
        factor = 195

        pension_mensual = Pension_prueba.calcular_pension_privado(
            saldo_acumulado, factor, edad, entidad
        )

        pension_esperada = 1_435_897.44  # 280,000,000 / 195
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=2)

    def test_normal_privada_4(self):
        edad = 57
        saldo_acumulado = 850_000_000
        entidad = "Porvenir"
        factor = 125

        pension_mensual = Pension_prueba.calcular_pension_privado(
            saldo_acumulado, factor, edad, entidad
        )

        pension_esperada = 6_800_000.00  # 850,000,000 / 125
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    def test_extraordinario_2(self):
        edad = 56
        saldo_acumulado = 900_000_000
        entidad = "Porvenir"
        factor = 150

        pension_mensual = Pension_prueba.calcular_pension_privado(
            saldo_acumulado, factor, edad, entidad
        )

        pension_esperada = 6_000_000.00  # 900,000,000 / 150
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    def test_extraordinario_3(self):
        edad = 35
        saldo_acumulado = 120_000_000
        entidad = "Porvenir"
        factor = 63

        pension_mensual = Pension_prueba.calcular_pension_privado(
            saldo_acumulado, factor, edad, entidad
        )

        pension_esperada = 1_904_761.90  # 120,000,000 / 63
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=2)

    def test_extraordinario_5(self):
        edad = 50
        saldo_acumulado = 0
        entidad = "Porvenir"
        factor = 125

        pension_mensual = Pension_prueba.calcular_pension_privado(
            saldo_acumulado, factor, edad, entidad
        )

        pension_esperada = 0.0
        self.assertAlmostEqual(pension_mensual, pension_esperada, places=0)

    # ------- Errores esperados -------

    def test_error_1(self):
        edad = 62
        semanas = 900
        salario_promedio = 2_500_000
        reemplazo = "No aplica"
        entidad = "Colpensiones"

        with self.assertRaises(Pension_prueba.Error_no_cumple_semanas):
            Pension_prueba.calcular_reemplazo_colpensiones(
                salario_promedio, reemplazo, semanas, edad, entidad
            )

    def test_error_2(self):
        edad = 44
        semanas = 1200
        salario_promedio = 2_500_000
        reemplazo = "No aplica"
        entidad = "Colpensiones"

        with self.assertRaises(Pension_prueba.Error_invalidez):
            Pension_prueba.calcular_reemplazo_colpensiones(
                salario_promedio, reemplazo, semanas, edad, entidad
            )

    def test_error_3(self):
        edad = 62
        semanas = 1300
        salario_promedio = 2_500_000
        reemplazo = 0.65
        entidad = "Entidad falsa"

        with self.assertRaises(Pension_prueba.Error_entidad_invalida):
            Pension_prueba.calcular_reemplazo_colpensiones(
                salario_promedio, reemplazo, semanas, edad, entidad
            )

    def test_error_4(self):
        saldo_acumulado = 100_000_000
        factor = 0
        edad = 62
        entidad = "Porvenir"

        with self.assertRaises(Pension_prueba.Error_factor_invalido):
            Pension_prueba.calcular_pension_privado(
                saldo_acumulado, factor, edad, entidad
            )


if __name__ == "__main__":
    unittest.main()
