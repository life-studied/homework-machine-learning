#include "hypothesis.h"
int main()
{
	hypothesis system("data.txt");
	for (int i = 0; i < 20; i++)
	{
		std::cout << "x:" << i << "\tvalue:" << system.h(i) << std::endl;
	}
	
}