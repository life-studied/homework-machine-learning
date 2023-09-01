# homework-machine-learning
​	吴恩达网课机器学习课后作业

## 01 线性拟合

​	对$y = \theta_0 + \theta_1 * x$线性函数进行拟合，数据在pizza.txt中。

### 步骤

* 读取数据，存入数组
* 循环（终止条件：步数/代价函数几乎不变）
  * 根据代价函数$J(\theta_0,\theta_1) = \frac{1}{2m}\sum_{i=1}^{m}(h(x_i)-y_i)^2$
    * 求两个偏导和：$temp_0$和$temp_1$
    * $temp_0 = \frac{1}{m} \sum_{i = 1}^{m}(h(x_i) - y_i)$
    * $temp_1 = \frac{1}{m} \sum_{i = 1}^{m} (h(x_i)-y_i)*x_i$
  * 更新值：
    * $\theta_0 = \theta_0 - \alpha * temp_0$
    * $\theta_1 = \theta_1 - \alpha * temp_1$



