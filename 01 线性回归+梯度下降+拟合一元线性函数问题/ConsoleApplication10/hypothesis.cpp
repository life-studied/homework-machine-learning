#include "hypothesis.h"
#include<iomanip>
double hypothesis::cost(double t0, double t1)
{
    int num = data.size();
    double sum{};
    for (const auto& i : data)
    {
        double one_item = t0 + t1 * i.first - i.second;
        sum += one_item * one_item;
    }
    return sum / 2.0 / num;
}

double hypothesis::theta0_derivative()
{
    int num = data.size();
    double sum{};
    for (const auto& i : data)
    {
        sum += h(i.first) - i.second;
    }
    return sum / num;
}

double hypothesis::theta1_derivative()
{
    int num = data.size();
    double sum{};
    for (const auto& i : data)
    {
        sum += i.first * (h(i.first) - i.second);
    }
    return sum / num;
}

double hypothesis::h(double x)
{
    return theta_0 + theta_1 * x;
}

void hypothesis::gradient()
{
    for(int i = 0;i<20000;i++)
    {
        double temp0 = theta0_derivative();
        double temp1 = theta1_derivative();
        double last_theta0 = theta_0;
        double last_theta1 = theta_1;
        theta_0 -= studyRet * temp0;
        theta_1 -= studyRet * temp1;
        double cost1 = cost(theta_0, theta_1);
        double cost2 = cost(last_theta0, last_theta1);
        std::cout << "new t0 and t1:" << std::setprecision(5) << theta_0 << "\t" << theta_1 << std::endl;
        std::cout << "cost1 and cost2:" << std::setprecision(8) << cost1 << "\t" << cost2 << std::endl;
        
    }
}
