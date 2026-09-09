
#include <iostream>
//learncpp.com 1.9 -> ... 2.10

// syntax: type identifier { expression };  ====> int sayi {1230};



/* terms to know before reading the following code example:
 Declaration: Tells compiler about an identifier and its associated type information.
 Definition: Implements a function or instantiates a variable. Definitions are also declarations.
 Pure declaration: A declaration that isn’t a definition.
 Initialization: Provides an initial value for a defined object.
 A good SWE must make his code readable both for himself and others. Use whitespaces efficient.

 Cpp reads code up to bottom, you must declare function before calling it in main,
 If want to create function body later, you can use forward declaration.
 For example:
int forward_declared_fn(int ,int);              // no function body yet. (fn parameters does not need to have names)
int main() {
    std::cout << forward_declared_fn(2,3);      // called body-less function in main.
    return 0;
}
int forward_declared_fn(int x, int y) {         // defined the body later. No problem occurs.
    return x * y;
}
 !! If line 20 was never given: (LINKER ERROR)
        The program would compile but wouldn't link. Linker gives error because func body never given.
 !! If line 12 was never given: (COMPILER ERROR)
        The program wouldn't compile because it would not be able to access called function.
*/

/*  Multi file cpp programs: All files get compiled all together.
    Lets say I have an add.cpp and main.cpp in the same folder of files:
    add.cpp -> has two parameters int x and int y, returns their multiplication: return x + y
    main.cpp -> has no add function declaration anywhere in the file, just calls the add(2,3) function.
    What Happens If main.cpp file has no clue what add() is? Since there are no declaration of add() anywhere in main.cpp, wont compile
    How to make sure add.cpp add() function body gets recognized by main.cpp? You simply use a declaration for add():
*/

int add(int x,int y);               //we need this declaration to make sure compiler does not complain.
void non_value_returning_fn()
{
    std::cout << "hi, this function will not return any value where its called.\n";
}

int get_user_input()                    //declared fn header with integer returning type.
{
    std::cout << "enter val:    ";    //fn body
    int userin {};                      //fn body
    std::cin >> userin;                 //fn body//fn body
    return userin;                      //returns input "userin" to where its called
}


int main()
{
    std::cout << "we will call add() fn from add.cpp file:\n";
    std::cout << add(2,3) << "\n";
    non_value_returning_fn();
    std::cout << "returned value doubled:   " << (get_user_input() * 2) << "\n";
    return 0;
}
// NOTE: If you declare the function with the same name inside main.cpp file, linker cant execute. This is called "Naming Collisions"

