#include <iostream>
//#include "d4_lrncpp_2_13.h"
#include "d5_quizz2.h"

/* d5_quizz1.
int write_answer(int x)
{
    std::cout << "entered number:   " << x << "\n";
    return 0;
}
int read_number()
{
    int userin{};
    std::cout << "enter integer:    \n";
    std::cin >> userin;
    return userin;
}
*/
int main()
{
    /*
    std::cout <<  "start" << "\n";
    wake_up();
    tidy_bed();
    brush_teeth();
    shower();
    eat_breakfast();
    dress_up();
    leave();
    std::cout << "end";
    */

    /* QUIZZ1
    A function named “readNumber” should be used to get (and return) a single integer from the user.
    A function named “writeAnswer” should be used to output the answer. This function should take a single parameter and have no return value.
    A main() function should be used to glue the above functions together.
    int answer{};
    write_answer(read_number());
    */

    /* QUIZZ2
    Modify the program you wrote in exercise #1 so that readNumber() and writeAnswer() live in a separate file called “io.cpp”.
    Use a forward declaration to access them from main().
    If you’re having problems, make sure “io.cpp” is properly added to your project so it gets compiled.
    write_number(read_number());
    return 0;
    */

    /* QUIZZ3
     *Modify the program you wrote in #quizz2
     *so that it uses a header file (named io.h) to access the functions instead of using forward declarations directly in your code (.cpp) files.
     *Make sure your header file uses header guards.
     SOLUTION IS DONE ABOVE.
    */

    
}

