from flask import Blueprint, render_template, request
from src.service.pension_service import (
    buscar_aportante_por_documento,
    insertar_aportante,
    listar_aportantes,  # opcional, para /lista
)

pension_bp = Blueprint(
    "pension",
    __name__,
    url_prefix="",
    template_folder="../view/templates",
    static_folder="../view/static",
)


# -------- Menú de inicio --------
@pension_bp.route("/")
def index():
    return render_template("index.html")


# -------- Buscar (READ) --------
@pension_bp.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultado = None
    if request.method == "POST":
        documento = request.form.get("documento")
        if documento:
            resultado = buscar_aportante_por_documento(documento)
    return render_template("buscar.html", resultado=resultado)


# -------- Insertar (CREATE) --------
@pension_bp.route("/insertar", methods=["GET", "POST"])
def insertar():
    mensaje = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        documento = request.form.get("documento")
        salario = request.form.get("salario")

        if nombre and documento and salario:
            insertar_aportante(nombre, documento, float(salario))
            mensaje = "Aportante insertado correctamente."

    return render_template("insertar.html", mensaje=mensaje)