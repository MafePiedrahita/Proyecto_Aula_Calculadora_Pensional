from flask import Flask
from src.controller.pension_controller import pension_bp
from src.init_db import apply_schema

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "super-secret-key"

    # Registrar los blueprints (controladores)
    app.register_blueprint(pension_bp)

    # Ruta para crear tablas en la base de datos
    @app.route("/init-db")
    def init_db_route():
        apply_schema()  # usa sql/01_schema.sql
        return "✔ Tablas creadas correctamente en la base de datos."

    return app


# ---------- EJECUCIÓN ----------
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)



