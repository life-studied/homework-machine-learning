from LogisticClass import LogisticsRegression

if __name__ == '__main__':
    demo = LogisticsRegression(r"../data-set/test.txt")
    demo.gradient_descent()
    demo.print_cost()
    demo.print_theta()
