#pragma once
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <utility>
#include "file_manager.h"

class hypothesis
{
private:
	std::string dataFile;
	std::string resFile;
	std::vector<std::pair<double, double>> data;
	double theta_0;
	double theta_1;
	bool isCalculated;
	double studyRet;
public:
	hypothesis(std::string dataFile, std::string resFile = "") : dataFile(dataFile), resFile(resFile), theta_0(0), theta_1(1), isCalculated(false), studyRet(0.001)
	{
		file_manager fm;
		std::stringstream ss(fm.getData(dataFile));
		while (!ss.eof())
		{
			double d1, d2;
			ss >> d1 >> d2;
			data.push_back({ d1,d2 });
		}
		std::cout << "data loading finish..." << std::endl;
		gradient();
		isCalculated = true;
	}
	double h(double x);
private:
	void gradient();
	double cost(double t0, double t1);
	double theta0_derivative();
	double theta1_derivative();
};