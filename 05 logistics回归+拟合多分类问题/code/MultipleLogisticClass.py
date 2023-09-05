import sys

from LogisticClass import LogisticsRegression

sys.path.append('../../thirdparty/python-tools/ExtractNumbers')
import extract_num as exn


class MultipleLogisticsRegression:
    def __init__(self, file_path):
        self.x_list, self.y_list = exn.read_xy_data_set_file(file_path)
        self.sample_dict = {}  # 创建一个样本字典，键为y值，值为x行向量样本的list
        for x, y in zip(self.x_list, self.y_list):
            if y in self.sample_dict:
                self.sample_dict[y].append(x)
            else:
                self.sample_dict[y] = [x]
        # 划分样本至k个二分类
        self.logistic_regression_s = []
        self.y_key = []
        for key in self.sample_dict.keys():
            x_list = self.sample_dict[key]
            x_list.extend([item for item in self.x_list if item not in self.sample_dict[key]])
            y_list = [1] * len(self.sample_dict[key]) + [0] * (len(self.x_list) - len(self.sample_dict[key]))
            self.logistic_regression_s.append(LogisticsRegression(x_list, y_list))
            self.y_key.append(key)

    def h(self, x):
        max_p = 0  # 最大概率
        y = 0  # 对应的分类
        for i, key in zip(self.logistic_regression_s, self.y_key):  # 遍历h(x)，找出最大的概率
            now_p = i.h(x)
            if now_p > max_p:
                y = key
                max_p = now_p
        return y  # 返回对应的分类
