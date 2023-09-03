from MultipleLogisticClass import MultipleLogisticsRegression

if __name__ == '__main__':
    demo = MultipleLogisticsRegression(r"../data-set/test.txt")
    x = []  # 输入测试样例
    print(demo.h(x))  # 输出对应的分类
