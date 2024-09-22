from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, json: Dict) -> None:
        self.json = json

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        random_mock_value = 3
        return random_mock_value
    
    def variance(self, numbers: List[float]) -> float:
        pass

def test_calculate():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
    })

    driver = MockDriverHandler()
    calculator_instance = Calculator2(driver_handler=driver)
    calculated_response = calculator_instance.calculate(mock_request)

    assert 'data' in calculated_response
    assert 'calculator' in calculated_response['data']
    assert 'result' in calculated_response['data']

    assert calculated_response['data']['calculator'] == 2
    assert calculated_response['data']['result'] == 0.33

def test_calculate_with_numpy_integration():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
    })

    driver = NumpyHandler()
    calculator_instance = Calculator2(driver_handler=driver)
    calculated_response = calculator_instance.calculate(mock_request)

    assert 'data' in calculated_response
    assert 'calculator' in calculated_response['data']
    assert 'result' in calculated_response['data']

    assert calculated_response['data']['calculator'] == 2
    assert calculated_response['data']['result'] == 0.08

def test_calculate_with_body_error():
    mock_request = MockRequest({
        "something": []
    })

    driver = NumpyHandler()
    calculator_instance = Calculator2(driver_handler=driver)

    with raises(Exception) as exception:
        calculator_instance.calculate(mock_request)

    assert str(exception.value) == 'Incorrect body'