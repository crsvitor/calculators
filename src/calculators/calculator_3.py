from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.driver_handler_interface import DriverHandlerInterface
from src.errors.http_errors import HttpUnprocessableEntityError, HttpBadRequest

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json

        input_data = self.__validate_body(body)
        variance_value = self.__variance(input_data)
        multiplied_value = self.__multiplication(input_data)

        self.__verify_result(variance=variance_value, multiplication=multiplied_value)

        formatted_value = self.__format_response(variance=variance_value)
        return formatted_value

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Incorrect body")
        
        input_data = body['numbers']
        return input_data
    
    def __variance(self, numbers: List[float]) -> float:
        variance = self.__driver_handler.variance(numbers=numbers)
        return variance
    
    def __multiplication(self, numbers: List[float]) -> float:
        multiplied_values = 1
        for number in numbers: multiplied_values *= number
        return multiplied_values
    
    def __verify_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequest('Process failed: Variance is lower than multiplied values')
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "Success": True,
            }
        }

