from flask import Flask
from src.controller.pension_controller import pension_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(pension_bp)  # conectar el controlador
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
