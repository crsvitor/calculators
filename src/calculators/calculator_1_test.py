from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={ 'number': 10 })
    calculator_instance = Calculator1()

    calculated_response = calculator_instance.calculate(request=mock_request)

    assert 'data' in calculated_response
    assert 'calculator' in calculated_response['data']
    assert 'result' in calculated_response['data']

    assert calculated_response['data']['calculator'] == 1
    assert calculated_response['data']['result'] == 22.67

def test_calculate_with_body_error():
    mock_request = MockRequest(body={
        'something': 10
    })

    calculator_instance = Calculator1()

    with raises(Exception) as exception:
        calculator_instance.calculate(mock_request)

    assert str(exception.value) == 'Incorrect body'
