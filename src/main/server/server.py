from flask import Flask
from src.main.routes.calculators import calculator_routes_blueprint


app = Flask(__name__)
app.register_blueprint(calculator_routes_blueprint)