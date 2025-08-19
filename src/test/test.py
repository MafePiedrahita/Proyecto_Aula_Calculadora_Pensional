import sys
sys.path.append("src")

import unittest
from model import Pension_prueba 

class PruebasPenion( unittest.TestCase):

    def test_normal_1( self ):
        # Entradas
        sexo = "Hombre"
        edad = 62
        semanas = 1300
        salario_promedio = 3_000_000
        reemplazo = 0.65
        entidad = "Colpensiones"

        #Probar proceso
        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

        #Verificar Salidas
        pension_esperada = 1_950_000

        self.assertAlmostEqual(pension_mensual, pension_esperada, 0)

    def test_extraordinario_1( self ):
        #Entradas
        sexo = "Mujer"
        edad = 57
        semanas = 1000
        salario_promedio = 2_000_000
        reemplazo = 0.65
        entidad = "Colpensiones"

        #Probar Proceso
        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

        #Verificar Salidas
        pension_esperada = 1_300_000

        self.assertAlmostEqual(pension_mensual, pension_esperada, 0)

    def test_ideal_1( self ):
        #Entradas
        sexo = "Hombre"
        edad = 62
        semanas = 1800
        salario_promedio = 4_000_000
        reemplazo = 0.80
        entidad = "Colpensiones"
        
        #Probar Proceso
        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)
        
        #Verificar Salidas
        pension_esperada = 3_200_000

    def test_normal_privada_2( self ):
        #Entradas 
        sexo = "Hombre"
        edad = 62
        semanas = "No aplica"
        salario_promedio = 3_000_000
        saldo_acomulado = 350_000_000
        entidad = "Porvenir"
        factor = 171

        #Proceso de Prueba
        pensional_mensual = Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

        #Verificar Salidas
        pension_esperada = 2_046_793.63

    def test_normal_privada_3( self):
        #Entradas
        sexo = "Mujer"
        edad = 57
        semanas = "No aplica"
        salario_promedio = 2_500_000
        saldo_acomulado = 280_000_000
        entidad = "Porvenir"
        factor = 195

        #Procesos de Prueba
        pension_mensual = Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

        #Verificar Salidas
        pension_esperada = 1_435_897.44

    def test_normal_privada_4( self ):
        #Entradas
        sexo = "Mujer"
        edad = 57
        semana = 2100
        salario_promedio = 6_800_000
        saldo_acomulado = 850_000_000
        entidad = "Porvenir" 
        factor = 125

        #Procesos de Prueba
        pension_mensual = Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

        #Verificar Salidas
        pension_esperada = 6_800_000

    def test_extraordinario_2( self ):
        #Entradas
        sexo = "Mujer"
        edad = 56
        semana = 1600
        salario_promedio = 6_000_000
        saldo_acomulado = 900_000_000
        entidad = "Porvenir" 
        factor = 150

        #Procesos de Prueba
        pension_mensual = Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

        #Verificar Salidas
        pension_esperada = 6_000_000
    
    def test_extraordinario_3( self ):
        #Entradas
        sexo = "Mujer"
        edad = 35
        semana = 500
        salario_promedio = 2_800_000
        saldo_acomulado = 120_000_000
        entidad = "Porvenir" 
        factor = 63

        #Procesos de Prueba
        pension_mensual = Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

        #Verificar Salidas
        pension_esperada = 1_435_897.44
    
    def test_extraordinario_4( self ):
       #Entradas
        sexo = "Hombre"
        edad = 62
        semanas = 2200
        salario_promedio = 30_000_000
        reemplazo = 0.80
        entidad = "Colpensiones"
        
        #Probar Proceso
        pension_mensual = Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)
        
        #Verificar Salidas
        pension_esperada = 24_000_000

    def test_error_1(self):
        #Entradas
        sexo = "Hombre"
        edad = 62
        semanas = 900
        salario_promedio = 2_500_000
        reemplazo = "No aplica"
        entidad = "Colpensiones"

        #Proceso
        with self.assertRaises( Pension_prueba.Error_no_cumple_semanas):
            Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

    def test_error_2(self):
        #Entradas
        sexo = "Hombre"
        edad = 44
        semanas = 1200
        salario_promedio = 2_500_000
        reemplazo = "No aplica"
        entidad = "Colpensiones"

        #Proceso de Prueba
        with self.assertRaises( Pension_prueba.Error_invalidez):
            Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)
    

    def test_extraordinario_5(self):
         #Entradas
        sexo = "Mujer"
        edad = 50
        semana = 950
        salario_promedio = 2_800_000
        saldo_acomulado = 0
        entidad = "Porvenir" 
        factor = 125

        #Procesos de Prueba
        pension_mensual = Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)

        #Verificar Salidas
        pension_esperada = 2_000_000 

    def test_error_3(self):
        #Entradas
        sexo = "Hombre"
        edad = 62
        semanas = 1300
        salario_promedio = 2_500_000
        reemplazo = 0.65
        entidad = "Entidad falsa" 
        
        #Proceso de Prueba
        with self.assertRaises(Pension_prueba.Error_entidad_invalida):
            Pension_prueba.calcular_reemplazo_colpensiones(salario_promedio, reemplazo, semanas, edad, entidad)

    def test_error_4(self):
        # Entradas
        saldo_acomulado = 100_000_000
        factor = 0
        edad = 62
        entidad = "Porvenir"

        # Proceso
        with self.assertRaises(Pension_prueba.Error_factor_invalido):
            Pension_prueba.calcular_pension_privado(saldo_acomulado, factor, edad, entidad)


    



#Bucle Principal
if __name__ == "__main__":
    unittest.main()
