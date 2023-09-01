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
	std::vector<vector<double>> data;
	std::vector<double> y;
	std::vector<double> theta;
	bool isCalculated;
	double studyRet;
	int x_num;
public:
	hypothesis(std::string dataFile, int x_num);
	double h(const vector<double>& x);
private:
	void gradient();
	double cost(const vector<double>& theta);
	double theta_derivative(int i);
};
