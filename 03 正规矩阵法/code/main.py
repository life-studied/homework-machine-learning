import matplotlib.pyplot as plt
import numpy as np
import sys

sys.path.append("../../thirdparty/python-tools/ExtractNumbers")
sys.path.append("../../thirdparty/python-tools/EasyPaint")
import extract_num as exn
import easy_paint as ep


def calculate_theta(x_lists, y_lists):
    x_matrix = np.matrix(x_lists)
    y_matrix = np.matrix(y_lists)
    return (x_matrix.T * x_matrix).I * x_matrix.T * y_matrix


if __name__ == '__main__':
    x_lists, y_lists = exn.read_xy_data_set_file(r"../data-set/pizza_1_vars.txt")
    theta = calculate_theta(x_lists, y_lists)
    if len(theta) == 2:  # 如果是一次函数，则绘制图像
        # 计算绘制区域的上下限
        x_start = int(min([x[1] for x in x_lists]))
        x_end = int(max([x[1] for x in x_lists]))
        y_start = int(min([y[0] for y in y_lists]))
        y_end = int(max([y[0] for y in y_lists]))

        # 设定图像的尺寸（英尺）
        fig, ax = plt.subplots(figsize=(8, 10))
        # 绘制散点图
        ep.paint_dots_chart(x_lists, y_lists)
        # 绘制直线图
        ep.paint_line_chart(theta, x_start, x_end)
        # 美化并显示
        ep.beautify_line_chart(x_start, x_end, y_start, y_end)
    print(f"theta = \n{theta}")
