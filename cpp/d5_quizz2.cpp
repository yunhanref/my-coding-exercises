#include "d5_quizz2.h"
#include <iostream>
int read_number()
{
    int userin{};
    std::cout << "Enter an integer: \n";
    std::cin >> userin;
    return userin;
}

int write_number(int x)
{
    std::cout << "You entered:  " << x << "\n";
    return 0;
}