from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, json: Dict) -> None:
        self.json = json

class MockDriverHandler(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        pass
    
    def variance(self, numbers: List[float]) -> float:
        random_mock_value = 151515
        return random_mock_value

class MockDriverHandlerError(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float:
        pass
    
    def variance(self, numbers: List[float]) -> float:
        random_mock_value = 3
        return random_mock_value

def test_calculate_with_variance_error():
    mock_request = MockRequest({
        "numbers": [1, 2, 3, 4, 5]
    })

    driver = MockDriverHandlerError()
    calculator3 = Calculator3(driver_handler=driver)

    with raises(Exception) as exception:
        calculator3.calculate(mock_request)

    assert str(exception.value) == 'Process failed: Variance is lower than multiplied values'

def test_calculate():
    mock_request = MockRequest({
        "numbers": [1, 1, 1, 1, 100]
    })

    driver = MockDriverHandler()
    calculator3 = Calculator3(driver_handler=driver)

    response = calculator3.calculate(request=mock_request)

    assert response == {'data': {
        'Calculator': 3,
        'value': 151515,
        'Success': True,
        }
    }

def test_calculate_with_numpy_integration():
    mock_request = MockRequest({
        "numbers": [1, 1, 1, 1, 100]
    })

    driver = NumpyHandler()
    calculator3 = Calculator3(driver_handler=driver)

    response = calculator3.calculate(request=mock_request)

    assert response == {'data': {
        'Calculator': 3,
        'value': 1568.16,
        'Success': True,
        }
    }