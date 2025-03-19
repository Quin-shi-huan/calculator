import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    def __init__(self):
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        py_std = self.__np.std(numbers)
        return float(py_std)

    def variance(self, numbers: List[float]) -> float:
        py_var = self.__np.var(numbers)
        return float(py_var)
