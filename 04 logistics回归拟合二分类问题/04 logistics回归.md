# 04 logistics回归

​	假设存在两个函数：$h_\theta(z) = \frac{1}{1+e^{-z}}$，以及$g(x)$，其中，$z = g(x)$。

​	其中，$g(x)$为决策边界的函数，用于将函数平面划分成两个区域，不同区域的函数值分别大于/小于0。

​	由于原有的代价函数会出现多个局部最优点，因此创建新的代价函数$Cost(h_\theta(x^{(i)}),y^{(i)}) = \begin{cases} -log(h_\theta(x)),&y = 1\\-log(1-h_\theta(x)),&y=0 \end{cases} $，即$Cost(h_\theta(x^{(i)}),y^{(i)}) = -y log(h_\theta(x))-(1-y)log(1-h_\theta(x))$

​	**代价函数图示：**

<img src="./assets/image-20230902161616257.png" alt="image-20230902161616257" style="zoom: 50%;" /><img src="./assets/image-20230902161722741.png" alt="image-20230902161722741" style="zoom: 50%;" />

​	分析：

* $h_\theta(x)\rightarrow1,y=1,Cost\rightarrow0$
* $h_\theta(x)\rightarrow0,y=1,Cost\rightarrow\infty$
* $h_\theta(x)\rightarrow0,y=0,Cost\rightarrow0$
* $h_\theta(x)\rightarrow1,y=0,Cost\rightarrow\infty$

综上，$J(\theta)=\frac{1}{m}\sum_{i=1}^{m}Cost(h_\theta(x^{(i)}),y^{(i)})=\frac{1}{m}[\sum_{i=1}^{m}-y^{(i)} log(h_\theta(x^{(i)}))-(1-y^{(i)})log(1-h_\theta(x^{(i)}))]$

## 梯度下降

​	$\theta_j = \theta_j - \alpha\sum_{i=1}^{m}(h_\theta(x^{(i)})-y^{(i)})x_j^{(i)}$

## 矩阵格式计算推导（线性g(x））

$x=\begin{bmatrix}x^{(1)}\\x^{(2)}\\ \vdots \\ x^{(m)}\end{bmatrix}$，其中$x^{(i)}$为样本行向量$\begin{bmatrix}x_1^{(i)}&x_2^{(i)}&\cdots&x_n^{(i)}\end{bmatrix}$。$x_1^{(i)} = 1$。

$y=\begin{bmatrix}y^{(1)}\\y^{(2)}\\ \vdots \\ y^{(m)}\end{bmatrix}$

$\theta = \begin{bmatrix}\theta_1\\\theta_2\\ \vdots \\ \theta_n\end{bmatrix}$

$g(x) = x*\theta = \begin{bmatrix}g(x)^{(1)}\\g(x)^{(2)}\\\vdots\\g(x)^{(m)}\end{bmatrix}$

$h(x) = \frac{1}{1+e^{-g(x)}} = \begin{bmatrix}\frac{1}{1+e^{-g(x)^{(1)}}} \\ \frac{1}{1+e^{-g(x)^{(2)}}} \\ \vdots \\ \frac{1}{1+e^{-g(x)^{(m)}}}\end{bmatrix}$

$Cost(h(x),y) = -\frac{1}{m}[y^T*log(h(x))+(\begin{bmatrix}1\\1\\\vdots\\1\end{bmatrix}-y)^T*log(\begin{bmatrix}1\\1\\\vdots\\1\end{bmatrix}-h(x))]$

梯度下降中每次迭代的新的$\theta_{i+1}=\theta_i - \alpha*((h(x)-y)^T*x)^T$