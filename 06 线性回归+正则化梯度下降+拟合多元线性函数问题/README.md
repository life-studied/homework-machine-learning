# 06 正则化+线性回归+拟合多元线性函数问题

​	对于原有的代价函数进行正则化后，新的代价函数为：

​		$J(\theta) = \frac{1}{2m} [\sum_{i = 1}^{m}(h_\theta(x^{(i)})-y^{(i)})^2 + \lambda \sum_{j= 1}^{n}\theta_j^2]$。

​		其中$\lambda$为正则化参数。

​	对该代价函数进行梯度下降，每次迭代后的$\theta_j$：

​		$\theta_j =\theta_j - \alpha [\frac{1}{m} \sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}+\frac{\lambda}{m}\theta_j]$

​		或者

​		$\theta_j =\theta_j(1-\alpha\frac{\lambda}{m}) - \alpha \frac{1}{m} \sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}$

​	注意这个新的式子的前半部分，其中的$1-\alpha\frac{\lambda}{m}$会是一个略小于1的值，因此就相当于在原有的$\theta_j$迭代上，对其先缩放至一个大约是$0.99$的大小，再减去一个相同的偏移值。

