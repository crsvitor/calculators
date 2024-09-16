from flask import Blueprint, jsonify, request

calculator_routes_blueprint = Blueprint('calculator_routes', __name__)

@calculator_routes_blueprint.route('/calculator/1', methods=['POST'])
def calculator_1():
    print(request)
    return jsonify({'success': True }), 200