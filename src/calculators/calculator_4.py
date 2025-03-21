from flask import request as FlaskRequest
from typing import Dict, List
from src.errors.error_controller import HttpUnprocessableEntityError


class Calculator_4:
    def calculate(self, request: FlaskRequest):  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        average = self.__calculate_list_media(input_data)
        response = self.__format_response(average)

        return response

    def __validate_body(self, body: Dict) -> float:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Lista de números não fornecida ou mal formatada!")

        input_data = body["numbers"]
        return input_data

    def __calculate_list_media(self, list_numbers: List[float]) -> float:
        first_part = sum(list_numbers)
        second_part = first_part / len(list_numbers)
        return second_part

    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }
