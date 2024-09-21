from typing import Dict
from pytest import raises
from .calculator_2 import Calculator2

class MockRequest:
    def __init__(self, json: Dict) -> None:
        self.json = json


def test_calculate():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
    })

    calculator_instance = Calculator2()
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

    calculator_instance = Calculator2()

    with raises(Exception) as exception:
        calculator_instance.calculate(mock_request)

    assert str(exception.value) == 'Incorrect body'