import matplotlib.pyplot as plt
import numpy as np


def beautify_line_chart():
    # 添加标签
    plt.xlabel("x")
    plt.ylabel("f(x)")
    # 设置坐标轴范围
    plt.xlim(-2, 30)
    plt.ylim(-2, 30)
    # 设置横纵轴刻度
    plt.xticks([i for i in range(0, 30)])
    plt.yticks([i for i in range(0, 30)])
    # 添加网格线
    plt.grid(True)
    # 横纵轴统一标尺
    plt.gca().set_aspect('equal', adjustable='box')
    # 显示图形
    plt.show()


def load_data_set(file_path):
    data_list = []
    y_list = []
    i = 0
    with open(file_path, 'r') as f:
        for line in f.readlines():
            line = line.rstrip()
            line_data = [int(data) for data in line.split()]
            data_list.append([1])
            y_list.append([])
            data_list[i].extend(line_data[:-1])
            y_list[i].append(line_data[-1])
            i = i + 1
    return data_list, y_list


def calculate_theta(x_lists, y_lists):
    x_matrix = np.matrix(x_lists)
    y_matrix = np.matrix(y_lists)
    return (x_matrix.T * x_matrix).I * x_matrix.T * y_matrix


def paint_dots_chart(ax, x_lists, y_lists):
    ax.plot(x_lists, y_lists)
    beautify_line_chart()


def paint_line_chart(ax, theta_list):
    x_array = np.linspace(-2, 2, 101)
    y_array = [x * theta_list[1] + theta_list[0] for x in x_array]
    ax.plot(x_array, y_array)
    beautify_line_chart()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    x_lists, y_lists = load_data_set(r"../data-set/pizza_3_vars.txt")
    theta = calculate_theta(x_lists, y_lists)
    # if len(theta) == 2:  # 如果是一次函数，则绘制图像
    #     fig, ax = plt.subplots(figsize=(4, 4))
    #     paint_dots_chart(ax, x_lists, y_lists)
    #     paint_line_chart(ax, theta)
    print(f"theta = \n{theta}")
