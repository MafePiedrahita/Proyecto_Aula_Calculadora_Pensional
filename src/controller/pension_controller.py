from flask import Blueprint, render_template, request
from src.service.pension_service import calcular_pension

pension_bp = Blueprint('pension', __name__)

@pension_bp.route('/')
def index():
    return render_template('index.html')

@pension_bp.route('/calcular', methods=['POST'])
def calcular():
    salario = float(request.form['salario'])
    semanas = int(request.form['semanas'])
    edad = int(request.form['edad'])
    regimen = request.form['regimen']
    
    resultado = calcular_pension(salario, semanas, edad, regimen)
    return render_template('index.html', resultado=resultado)
