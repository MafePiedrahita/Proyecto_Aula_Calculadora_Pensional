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
```
git clone <URL_DEL_REPO>
cd Proyecto_Aula_Calculadora_Pensional-main

```
### 2. (Recomendado) Crea y activa un entorno virtual
### Crear:
```
python -m venv .venv
```
### Activar

-macOS / Linux
```
source .venv/bin/activate
```
-Windows (PowerShell)
```
.\\.venv\\Scripts\\Activate.ps1
```
-Windows (CMD)
```
.\.venv\Scripts\activate.bat
```

### 2) Ejecutar las pruebas unitarias

-Abre una terminal en la carpeta raíz del proyecto (donde ves src/).

-Ejecuta todas las pruebas con este comando:
```
python -m unittest discover -s src/test -p "test*.py" -v
``` 
## Ejemplos útiles:

-Un archivo específico
python -m unittest -v src.test.test

-Una clase de pruebas
python -m unittest -v src.test.test.PruebasPension

-Un método de prueba
python -m unittest -v src.test.test.PruebasPension.test_normal_1

### 3) Ejecutar la interfaz de consola:

Desde la raíz del proyecto (con PYTHONPATH configurado como en 2A o con .env de 2B):
```
python -m src.view.interfaz_calculadora_pensional
```
La app te pedirá los datos por consola y mostrará el resultado calculado usando las funciones de src/model/Pension_prueba.py.

Si tu sistema requiere ruta explícita, usa:

python ./view/interfaz-calculadora-pensional.py

### La estructura relevante del proyecto es:
```
src/
├── app.py                         
├── controller/
│   ├── __init__.py
│   └── pension_controller.py     
├── model/
│   ├── __init__.py
│   ├── conexion_db.py            
│   └── Pension_prueba.py          
├── service/
│   ├── __init__.py
│   └── pension_service.py         
├── view/
│   ├── templates/                 
│   │   ├── index.html
│   │   ├── insertar.html
│   │   ├── buscar.html
│   │   └── crear_tablas.html
│   └── static/                    
└── init_db.py                     

```

### Elaborado por: 
Mariana Heano Echeverri y Maria Fernanda Piedrahita Montoya.

---

## 🧩 Ejecución de la Interfaz Gráfica (Kivy)

### 🔧 Requisitos previos

Antes de ejecutar la interfaz, asegúrate de tener instalado el framework **Kivy**.

Puedes instalar Kivy desde la terminal con el siguiente comando:

```bash
pip install kivy
```

> 💡 Si usas un entorno virtual (recomendado), actívalo antes de instalar Kivy.

---

### ▶️ Ejecución por consola

1. Abre una terminal o consola en la carpeta raíz del proyecto.
2. Dirígete al directorio donde se encuentra la interfaz src/view/gui.
3. Ejecuta el siguiente comando:

```bash
python Interfaz_calculadora_gui.py
```

Esto iniciará la interfaz gráfica de la calculadora pensional utilizando Kivy.
Una ventana se abrirá mostrando la aplicación con su interfaz visual completa.

---

### 💻 Ejecución del ejecutable (.exe)

Si no deseas usar la consola, también puedes ejecutar la aplicación desde el **ejecutable disponible en la sección de “Releases” del repositorio de GitHub**.

1. Ve al apartado **Releases**.
2. Descarga el archivo ejecutable (`.exe`) correspondiente a tu sistema operativo.
3. Una vez descargado, simplemente haz doble clic sobre el archivo para abrir la interfaz.

> ⚠️ No es necesario tener Python ni Kivy instalados para usar el ejecutable, ya que está empaquetado con todas las dependencias.

---

### 👨‍💻 Autores de la interfaz

* **Juan Sebastian Pinilla Giraldo**
* **Pedro Hernandez**

---


# Configuración de la base de datos 

Esta aplicación requiere este creada una tabla llamada aportantes.

## Ejecución como Aplicación Web (Flask)

Esta versión permite usar la Calculadora Pensional como una aplicación web interactiva, desarrollada con Flask bajo el patrón MVC (Modelo - Vista - Controlador).

## Requisitos adicionales
 
Asegúrate de tener Flask y psycopg2 instalados:

```
pip install flask psycopg2
```

## Configuración de la base de datos

La aplicación se conecta automáticamente a una base de datos PostgreSQL.

## Crear las tablas en la base de datos

Para crear las tablas automáticamente:


Asegúrate de que el archivo sql/01_schema.sql existe y contiene el esquema de la tabla aportantes.


## Ejecuta la aplicación y visita:

```
http://127.0.0.1:5000
```

## Ejecutar la aplicación web

1. Abre la terminal en la carpeta raíz del proyecto
2. Ejecuta:

```
python -m src.app
```


