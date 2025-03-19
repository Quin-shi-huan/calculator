from typing import Dict
from src.calculators.calculator_4 import Calculator_4


class MockRequest:
    def __init__(self, body: Dict):
        self.json = body


def test_calculate_media():
    mock_request = MockRequest({"numbers": [5, 5, 5, 5, 5]})
    calculator_4 = Calculator_4()

    response = calculator_4.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {
                "data": {
                    "Calculator": 4,
                    "result": 5
                }
            }
