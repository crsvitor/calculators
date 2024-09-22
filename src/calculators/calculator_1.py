from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_errors import HttpUnprocessableEntityError

class Calculator1:
    def calculate(self, request: FlaskRequest): # type: ignore
        body = request.json

        input_data = self.__validate_body(body)
        splitted_number = input_data / 3

        first_process_result = self.__first_process(splitted_number)
        second_process_result = self.__second_process(splitted_number)
        third_process_result = self.__third_process(splitted_number)

        calculation_result = first_process_result + second_process_result + third_process_result
        response = self.__format_response(calculation_result)
        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("Incorrect body")
        
        input_data = body['number']
        return input_data
    
    def __first_process(self, first_number: float) -> float:
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = second_number ** 2.121
        second_part = (first_part / 5) + 1
        return second_part

    def __third_process(self, third_number: float) -> float:
        return third_number
    
    def __format_response(self, calculation_result: float) -> Dict:
        return {
            'data': {
                'calculator': 1,
                'result': round(calculation_result, 2)
            }
        }