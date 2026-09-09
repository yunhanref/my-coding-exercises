#include "d4_lrncpp_2_13.h"
#include <iostream>

int wake_up() {
    std::cout << "you woke up.\n";
    return 0;
}
int tidy_bed() {
    int q {};
    std::cout << "tidy up?  \n";
    std::cin >> q;
    if (q == 1)
        std::cout << "you tidied up your bed" << "\n";
    else if (q == 0);
        std::cout << "you didnt tidy up your bed \n";
    return 0;
}


int brush_teeth() {
    int q {};
    std::cout << "brush teeth?  \n";
    std::cin >> q;
    if (q == 1)
        std::cout << "you brushed up your bed" << "\n";
    else if (q == 0);
        std::cout << "you didnt brush up your bed \n";
    return 0;
}


int shower() {
    std::cout << "you took a shower" << "\n";
    return 0;
}


int eat_breakfast() {
    std::cout << "you ate breakfast" << "\n";
    return 0;
}


int dress_up() {
    std::cout << "you dressed up" << "\n";
    return 0;
}


int leave() {
    std::cout << "you left the house" << "\n";
    return 0;
}