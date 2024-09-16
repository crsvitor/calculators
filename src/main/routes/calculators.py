from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calculator_routes_blueprint = Blueprint('calculator_routes', __name__)

@calculator_routes_blueprint.route('/calculator/1', methods=['POST'])
def calculator_1():
    calculator = Calculator1()
    response = calculator.calculate(request)

    return jsonify(response), 200