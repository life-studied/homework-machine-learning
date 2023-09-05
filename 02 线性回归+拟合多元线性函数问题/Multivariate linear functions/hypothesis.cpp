#include "hypothesis.h"
#include<iomanip>
double hypothesis::cost(const vector<double>& theta)
{
    int num = y.size();
    double sum{};
    for (int i = 0;i<num;i++)
    {
        double one_item = h(data[i]) - y[i];
        sum += one_item * one_item;
    }
    return sum / 2.0 / num;
}

double hypothesis::theta_derivative(int j)
{
    int num = y.size();
    double sum{};
    for (int i = 0; i < num; i++)
    {
        sum += (h(data[i]) - y[i]) * data[i][j];
    }
    return sum / num;
}

hypothesis::hypothesis(std::string dataFile, int x_num) : dataFile(dataFile), resFile(resFile), x_num(x_num), isCalculated(false), studyRet(0.001), theta(vector<double>(x_num + 1, 0))
{
    file_manager fm;
    std::stringstream ss(fm.getData(dataFile));
    int j{};
    while (!ss.eof())
    {
        double x_i{};
        
        data.push_back(vector<double>());
        data[j].reserve(x_num + 1);
        data[j].push_back(1);
        for (int i = 0; i < x_num; i++)
        {
            ss >> x_i;
            data[j].push_back(x_i);
        }
        j++;
        double y_i{};
        ss >> y_i;
        y.push_back(y_i);
    }
    std::cout << "data loading finish..." << std::endl;
    gradient();
    isCalculated = true;
}

double hypothesis::h(const vector<double>& x)
{
    double sum{};
    for (int i = 0; i < theta.size(); i++)
    {
        sum += theta[i] * x[i];
    }
    return sum;
}

void hypothesis::gradient()
{
    for(int i = 0;i<100000;i++)
    {
        vector<double> new_theta_derivative(x_num + 1, 0);
        for (int i = 0; i < theta.size(); i++)
                new_theta_derivative[i] = theta_derivative(i);
        for (int i = 0; i < theta.size(); i++)
            theta[i] -= studyRet * new_theta_derivative[i];
        double new_cost = cost(theta);
        std::cout << "new theta:";
        for (int i = 0; i < theta.size(); i++)
            std::cout << std::setprecision(5) << theta[i] << "\t";
        std::cout << std::endl;
        std::cout << "new cost" << std::setprecision(8) << new_cost << std::endl;
    }
}
