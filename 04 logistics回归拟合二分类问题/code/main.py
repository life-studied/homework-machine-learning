import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('../../thirdparty/python-tools/ExtractNumbers')
import extract_num as exn


class LogisticsRegression:
    def __init__(self, filename):
        pass

    def cost(self):
        pass

    def h(self, x):
        pass

    def theta_partial_derivative(self):
        pass


if __name__ == '__main__':
    print(exn.read_xy_data_set_str("../data-set/"))
