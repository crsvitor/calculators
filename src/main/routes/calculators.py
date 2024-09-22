from flask import Blueprint, jsonify, request
from src.main.factories.calculator_1_factory import calculator_1_factory
from src.main.factories.calculator_2_factory import calculator_2_factory
from src.main.factories.calculator_3_factory import calculator_3_factory
from src.errors.error_controller import handle_errors

calculator_routes_blueprint = Blueprint('calculator_routes', __name__)

@calculator_routes_blueprint.route('/calculator/1', methods=['POST'])
def calculator_1():
    try:
        calculator = calculator_1_factory()
        response = calculator.calculate(request)

        return jsonify(response), 200

    except Exception as exception:
        error_response = handle_errors(error=exception)
        return jsonify(error_response['body']), error_response['status_code']


@calculator_routes_blueprint.route('/calculator/2', methods=['POST'])
def calculator_2():
    try:
        calculator = calculator_2_factory()
        response = calculator.calculate(request)

        return jsonify(response), 200

    except Exception as exception:
        error_response = handle_errors(error=exception)
        return jsonify(error_response['body']), error_response['status_code']

@calculator_routes_blueprint.route('/calculator/3', methods=['POST'])
def calculator_3():
    try:
        calculator = calculator_3_factory()
        response = calculator.calculate(request)

        return jsonify(response), 200

    except Exception as exception:
        error_response = handle_errors(error=exception)
        return jsonify(error_response['body']), error_response['status_code']
