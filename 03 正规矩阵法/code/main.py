import matplotlib.pyplot as plt
import numpy as np


def beautify_line_chart(x_start, x_end, y_start, y_end):
    # 添加标签
    plt.xlabel("x")
    plt.ylabel("f(x)")
    # 设置坐标轴范围
    px_start = x_start - 1
    py_start = y_start - 1
    px_end = x_end + 1
    py_end = y_end + 1
    plt.xlim(px_start, px_end)
    plt.ylim(py_start, py_end)
    # 设置横纵轴刻度
    plt.xticks([i for i in range(px_start, px_end)])
    plt.yticks([i for i in range(py_start, py_end)])
    # 添加网格线
    # plt.grid(True)
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


def paint_dots_chart(x_lists, y_list):
    x_list = [x[1] for x in x_lists]
    plt.scatter(x_list, y_list)


def paint_line_chart(theta_matrix, x_start, x_end):
    x_array = np.linspace(x_start - 1, x_end + 1, 101)
    theta_list = theta_matrix.tolist()
    y_array = [x * theta_list[1][0] + theta_list[0][0] for x in x_array]
    plt.plot(x_array, y_array)


if __name__ == '__main__':
    x_lists, y_lists = load_data_set(r"../data-set/pizza_1_vars.txt")
    theta = calculate_theta(x_lists, y_lists)
    if len(theta) == 2:  # 如果是一次函数，则绘制图像
        # 计算绘制区域的上下限
        x_start = min([x[1] for x in x_lists])
        x_end = max([x[1] for x in x_lists])
        y_start = min([y[0] for y in y_lists])
        y_end = max([y[0] for y in y_lists])

        # 设定图像的尺寸（英尺）
        fig, ax = plt.subplots(figsize=(8, 10))
        # 绘制散点图
        paint_dots_chart(x_lists, y_lists)
        # 绘制直线图
        paint_line_chart(theta, x_start, x_end)
        # 美化并显示
        beautify_line_chart(x_start, x_end, y_start, y_end)
    print(f"theta = \n{theta}")
