from typing import Dict
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