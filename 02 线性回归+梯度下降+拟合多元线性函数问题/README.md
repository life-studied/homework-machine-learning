# 02 多元函数拟合

​	对于$h(X) = \theta^T * X$，其中$\theta = \begin{bmatrix}\theta_0\\ \theta_1\\ \vdots \\ \theta_n\end{bmatrix}$，$X=\begin{bmatrix}x_0\\ x_1\\ \vdots \\ x_n\end{bmatrix}$，并且$x_0 = 1$；

​	代价函数$J(\theta) = \frac{1}{2m} \sum_{i = 1}^{m}(h_\theta(X_i)-Y_i)^2$。

​	梯度下降法的$\theta_j =\theta_j - \alpha \frac{1}{m} \sum_{i=1}^{m}(h_\theta(X_i)-Y_i)x_j$。

### 优化方法

#### 1.特征缩放

​	可以通过使用特征缩放来使其更快收敛。该方法常用于参数之间的数量级差距较大（2个数量级以上）。

E.g. 

$x_1=size(0-2000 feet^2)$

$x_2 = number of bedrooms (1-5)$

将其进行归一化特征缩放处理，即：

$x_1 = \frac{x_1}{max size}$，$0 \leq x_1 \leq 1$

$x_2 = \frac{x_2}{max bedrooms}$，$0 \leq x_2 \leq 1$

注意：在做出特征缩放的参数处理后，对后续使用该函数时，传入的$x_i$也要进行对应的处理。

#### 2.均值归一化

​	均值归一化是另一种处理特征的方法。其本质就是在减去均值后再特征缩放。

​	其公式为：$x_i = \frac{x_i - \mu_i}{s_i}$，其中$\mu_i$为$x_i$的均值，$s_i$为$x_i$的范围（$max-min$）。

​	例如上面的例子，应该这样处理（假设平均值$x_1 = 1000$，$x_2 = 2$）：

$x_1 = \frac{x_1 - 1000}{max size}$，$-0.5 \leq x_1 \leq 0.5$

$x_2 = \frac{x_2 - 2}{max bedrooms}$，$-0.5 \leq x_2 \leq 0.5$，可能最大的会略大于0.5

#### 3.学习率选择

​	只要学习率足够小，最终梯度下降一定可以收敛到一个值。但是这样可能会导致收敛时间变得格外的长。选择一个合适的学习率，可以通过观察迭代过程中的代价函数曲线测试不同的学习率。（0.0001，0.0003，0.001，0.003，0.01，0.03...）

#### 4.合并参数

​	有时一些参数之间存在关系，可以将这些并不正交的参数进行合并，形成一个新的参数，来创造一个更好的模型。

​	例如，在房屋售价中，房屋长度和宽度是明显有关系的一个影响参数，可以将它们相乘来创造一个新的参数面积来构建更好的模型。

#### 5.非线性参数

​	如果某些参数的影响在直觉上很可能是非线性的，例如$h_\theta(x) =\theta_0+\theta_1 x_1+\theta_2 x_2^2 + \theta_3 x_3^3 $，可以令新的参数$g_0=1$，$g_1 = x_1$，$g_2 = x_2^2$，$g_3 = x_3^3$，使其变为一个线性函数$h_\theta(g) = \theta_0+\theta_1 g_1 + \theta_2 g_2 + \theta_3 g_3$。

​	注意：一般在这种情况下，特征缩放将变得额外重要。	

