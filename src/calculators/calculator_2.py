from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json

        input_data = self.__validate_body(body)
        calculation_result = self.__process_data(input_data)
        response = self.__format_response(calculation_result)

        return response

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise Exception("Incorrect body")
        
        input_data = body['numbers']
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(number * 11) ** 0.95 for number in input_data]
        result = self.__driver_handler.standard_derivation(first_process_result)

        return 1/result

    def __format_response(self, calculation_result: float) -> Dict:
        return {
            'data': {
                'calculator': 2,
                'result': round(calculation_result, 2)
            }
        }