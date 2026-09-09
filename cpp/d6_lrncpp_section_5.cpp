#include <iostream>

/* NOTES: 5.1 Constant variables
      A constant is a value that can not be changed. Constants have 2 types:
        1) Named Constants = Constants that have an identifier
        2) Literal Constants = Constants that have no identifier (Remember rust, string literals etc &str)

    Named Constants types:
        1)  Constant Variables: Unchangeable variables such as const int PI = 3.14
        2)  Object-Like Macros With Substitution Text: #define PI 3.14
        3)  Enumarated Macros: (We'll over later)

    Compiletime Constants       vs      Runtime Constants
    A compile-time constant is a constant whose value is known at compile-time. Examples include:
        Literals.
        Constant objects whose initializers are compile-time constants.
    A runtime constant is a constant whose value is determined in a runtime context. Examples include:
        Constant function parameters.
        Constant objects whose initializers are non-constants or runtime constants.
*/

/* CODES: Constants Exercise
#define ANOTHER_CONSTANT 12345
void constant_vals()
{
    std::cout << "debugging lesson practice\n";
    std::cout << "void started\n";
    const double PI {3.1415926};                // COMPILETIME CONSTANT
    const double G {9.81};                      // COMPILETIME CONSTANT
    std::cout << PI << "\n " << G << "\n" <<  ANOTHER_CONSTANT << "\n";
}
*/

/* CODES: Inputs can be made constants later:
int get_age()
{
    int age{};
    std::cout << "enter age:    \n";
    std::cin >> age;
    std::cout << "your age is:  " << age << "\n";
    std::cout << "now age will be const:    \n";
    const int CONST_INT {age};                  //RUNTIME CONSTANT
    return CONST_INT;
}
*/

/* CODES: Personal Char Input and If/Else Statements Exercise
int get_char(int x)
{
    std::cout << "get_char started.\n";
    if (x == 31)
        std::cout << "easter egg found\n";
    char userin{};
    std::cout << "y/n ?\n";
    std::cin >> userin;
    if (userin == 'y')
        std::cout << "you entered y\n";
    else if (userin == 'n')
        std::cout << "you entered n\n";
    else
        std::cout << "dumb\n";
    return userin;
}
*/

/*  NOTES: 5.2 Literals
    BEFORE READING: SAME AS RUST HEAP AND STACK STORED VARIABLES. LITERALS ARE STACK STORED, DIRECTLY SOURCE CODE WRITTEN VALUES.
    Literals are values that gets written directly to source code. For example:
        int ive {5}                     // 5 is an integer literal
        bool boolean_value {true}       // true is a bool literal
        std::cout << "Hello";           // "Hello" is a C-style string literal

    String Literals:
    C-style String Literals are const objects that are created at the start of the program and are guaranteed to exist for the entirety of the program.
    Every text we printed to the console by using std::cout is a C-type string literal. These type of strings are also called "null terminated strings"
    All C-type string literals have a "null terminator (\0)" at the end.
    Null terminators (\0) job is to indicate that the string has ended.
    example ===> std::cout << "merhaba"; this string literal consists of characters: 'm' + 'e' + 'r' + 'h' + 'a' + 'b' + 'a' + '\0'
*/

/*  NOTES: 5.4 As-If Rule
    Optimisation: Making code cleaner, better, efficient and faster.
    Profiler: A program that measures how long does a function run. Used to see performance.
    Optimizer: An automatic program that looks for ways to improve the code.
    NOTE: Modern cpp compilers are optimized compilers. That means your code gets rewritten where it needed to be.
    NOTE: Optimization is cumulative.

    *** The As-If Rule:
        In C++, compilers are given a lot of leeway to optimize programs.
        The as-if rule says that the compiler can modify a program however it likes in order to produce more optimized code,
        so long as those modifications do not affect a program’s “observable behavior”.
    For Example:
        int x{5+6}; ===> When compiler sees this, it sees no harm in changing  5+6 to directly 11. Because result of 5+6 never changes
        This is called CONSTANT FOLDING. This is an optimization technique where the compiler replaces expressions that have literal operands with the result of the expression.

    *** Compiletime Evaluation:
        Modern C++ compilers allows making calculations in the source code in COMPILETIME rather than making calculations in RUNTIME
        This action is called COMPILETIME EVALUATION. Provides performance boost, more straight-forward code, smaller and faster executable.

    *** CONSTANT PROPOGATION:
        int x{5};           // Created memory address for x that has value 5.
        std::cout << x;     // To cout x, it needs to be fetched from memory to see what it is.
        As you can see this program needs to access RAM 2 times. The modern compilers try to reduce the amount of memory access by using CONSTANT PROPOGATION
        Solution: Instead of having reaching for x in cout, the value of x (which is 5) is replaced with x.
        std::cout << x; ===> std::cout << 5;
        NOTE: THIS CAN ONLY BE DONE TO LITERALS/CONSTANTS. OTHERWISE UNDEFINED BEHAVIOUR WILL OCCUR.
        NOTE: CONST VARIABLES ARE EASIER TO OPTIMIZE THAN NON CONST LITERALS LIKE ABOVE. BECAUSE THEY CAN BE CHANGED LATER IN THE CODE.
    *** DEAD CODE ELIMINATION:
        When there are unused initialised code blocks inside source code, the compiler will find no problem deleting them completely.
    *** COMPILETIME CONSTANTS VS RUNTIME CONSTANTS
        Compiletime Constants: A compile-time constant is a constant whose value is known at compile-time. Examples include:
            Literals.
            Constant objects whose initializers are compile-time constants.\
        Example: const int x{5}; //compiler knows what it is in compiletime.

        Runtime Constants: A runtime constant is a constant whose value is determined in a runtime context. Examples include:
            Constant function parameters.
            Constant objects whose initializers are non-constants or runtime constants.
        Example: const int y{get_input()}; //compiler doesnt know what the returning input is so it is a runtime const.

*/

/* NOTES: 5.5 Constant expressions
 * COMPILETIME PROGRAMMING:
        The use of language features that result in compile-time evaluation is called compile-time programming
        Compiletime programming is used for these main reasons:
            1) Predictability: Prevents undefined behaviour by making computations in compiletime.
            2) Versatility: A calculation made in compiletime guarantees the calculation of that value in all compilers and devices.
            3) Performance and Quality: : Compiletime evaluation makes program smaller and faster.
            
*/


int constants()
{
    std::cout << 1e3<< "\n";
    std::cout << "merhaba";
}



