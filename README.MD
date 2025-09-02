# Proyecto de Aula: Calculadora Pensional (Colombia reforma 2024)
La calculadora Pensional es una herramienta que va a permitir estimar el valor de la pensional mensual que un trabajador en Colombia recibirá al momento de jubilarse.
Este cálculo se realiza de acuerdo a las reglas establecidas en la Reforma Pnesional 2024, la cual introdujo un modelo de pilares, que combina el égimen público con los fondos privados.
El propósito de este proyecto es brindar a los usuarios una forma seniclla de simular una pension futura.

### Contexto general de los pilares:
Régimen de Prima Media (Colpensiones):
-El trabajador cotiza semanas y al cumplir la edad y requisitos minimos, recibe una pensión calculada sobre un porcentaje de su salario promedio. Lo cual depende principalmente de:
-Semanas cotizadas 
-Edad
-Salario promedio 
-Tasa de reemplazo definida por la ley
### Régimen de Ahorro Individual con Solidaridad (Privadas):
-El trabajador ahorra en una cuenta individual administradad por un fondo privado (Protección, Porvenir, Colfondos)
-El monto de la pensión depende de:
 -Saldo acumulado
 -Factor de cálculo (relacionado con esperanza de vida, tasas de interés y modalidad de pensión)
 -Edad

### Funcionalidades:
-Estima la pensión en Colpensiones 
-Estima la pensión en fondos privados  
-Permite introducir datos como salario promedio, semanas cotizadas, saldo acumulado y edad.  
-Incluye validaciones de errores para asegurar cálculos correctos.  
-Retorna la pensión mensual proyectada con valores redondeados. 

Entrevista a experto sobre el tema: https://soundcloud.com/mariana-henao-748870407/entrevista_calculadora_pension?si=6600a80691774424b816af3bda636c84&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

# Guía rápida para ejecutar el proyecto

### Requisitos: 

- Python 3.10+. 
- Se recomienda usar entorno virtual (venv).

### 1) Preparación del entorno (una sola vez):

### 1. Clona el repositorio y entra a la carpeta del proyecto
git clone <URL_DEL_REPO>
cd <CARPETA_DEL_REPO>

### 2. (Recomendado) Crea y activa un entorno virtual
python -m venv .venv

-macOS / Linux
source .venv/bin/activate

-Windows (PowerShell)
.\\.venv\\Scripts\\Activate.ps1

-Windows (CMD)
.\.venv\Scripts\activate.bat

### 3. (Si existe) Instala dependencias
pip install -r requirements.txt

### La estructura relevante del proyecto es:
src/
  model/                  # Módulos de negocio
  test/                   # Pruebas unitarias (unittest)
view/
  interfaz-calculadora-pensional.py   (Interfaz de consola)

### 2) Ejecutar las pruebas unitarias

Asegúrate de estar en la raíz del proyecto (donde está la carpeta src/).

Opción Recomendada: ajustar PYTHONPATH y usar discover

Configura PYTHONPATH para que Python vea el paquete src/:

-macOS / Linux
export PYTHONPATH="$(pwd)/src"

-Windows (PowerShell)
$env:PYTHONPATH = "$PWD/src"

-Windows (CMD)
set PYTHONPATH=%cd%\src
### Ahora ejecuta todas las pruebas:
python -m unittest discover -s src/test -p "test*.py" -v
## Ejemplos útiles:

-Un archivo específico
python -m unittest -v src.test.test

-Una clase de pruebas
python -m unittest -v src.test.test.PruebasPension

-Un método de prueba
python -m unittest -v src.test.test.PruebasPension.test_normal_1

### 3) Ejecutar la interfaz de consola:

Desde la raíz del proyecto (con PYTHONPATH configurado como en 2A o con .env de 2B):

python view/interfaz-calculadora-pensional.py

La app te pedirá los datos por consola y mostrará el resultado calculado usando las funciones de src/model/Pension_prueba.py.

Si tu sistema requiere ruta explícita, usa:

python ./view/interfaz-calculadora-pensional.py

### Elaborado por: 
Mariana Heano Echeverri y Maria Fernanda Piedrahita Montoya.
