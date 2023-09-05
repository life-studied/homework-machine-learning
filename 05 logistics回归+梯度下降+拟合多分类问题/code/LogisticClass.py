import numpy as np
import matplotlib.pyplot as plt
import sys


sys.path.append('../../thirdparty/python-tools/EasyPaint')

import easy_paint as ep


class LogisticsRegression:
    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list
        # 转换为矩阵
        self.x_matrix = np.matrix(self.x_list)
        self.y_matrix = np.matrix(self.y_list)
        self.theta = [[0]] * len(self.x_list[0])
        self.theta_matrix = np.matrix(self.theta)
        self.alpha = 0.03
        self.cost_list = []
        self.m = len(self.y_list)

    def cost(self):
        ones_vector = np.matrix(np.ones((self.m, 1)))
        return -1.0 / self.m * (self.y_matrix.T * np.log(self.h_matrix()) + (ones_vector - self.y_matrix).T * np.log(
            ones_vector - self.h_matrix()))

    def g_matrix(self):
        return self.x_matrix * self.theta_matrix

    def g(self, x):
        pass

    def h_matrix(self):
        g_m = self.g_matrix()
        h_m = 1.0 / (1.0 + np.exp(-g_m))
        return h_m

    def h(self, x):
        pass

    def gradient_descent(self):
        while True:
            self.theta_matrix = self.theta_matrix - self.alpha * ((self.h_matrix() - self.y_matrix).T * self.x_matrix).T
            self.cost_list.append(self.cost().item())
            if len(self.cost_list) > 1 and np.abs(self.cost_list[-1] - self.cost_list[-2]) < 0.0000001:
                break

    def theta_partial_derivative(self):
        pass

    def paint(self):
        if len(self.x_list) == 2:
            ep.paint_dots_chart(self.x_list, self.y_list)
            ep.paint_line_chart(self.theta_matrix, self.x_start(), self.x_end())
        else:
            print(f"x参数个数为{len(self.x_list)}，超过1个，不予绘制")

    def paint_cost(self):
        x_list = [x for x in range(1, len(self.cost_list) + 1)]
        plt.scatter(x_list, self.cost_list)
        ep.beautify_line_chart(self.x_start(x_list), self.x_end(x_list),
                               self.y_start(self.cost_list), self.y_end(self.cost_list))

    def print_cost(self):
        print(self.cost_list)

    def print_theta(self):
        print(self.theta_matrix)

    @staticmethod
    def x_start(x_list):
        return int(min(x_list))

    @staticmethod
    def x_end(x_list):
        return int(max(x_list))

    @staticmethod
    def y_start(y_list):
        return int(min(y_list))

    @staticmethod
    def y_end(y_list):
        return int(max(y_list))
