/* Re-visit of multifile cpp projects (see: d2_lrncpp_2.10.cpp)
        As you can remember, we created an add.cpp that has the fn "add" that returns a+b)
        When we want to use a fn inside main.cpp that is defined in another cpp file, we simply forward declare the add function.
        The reason we forward declare the add function is because the first file to get executed is main.cpp.
            What happens if we DON'T forward declare the function?
                If there were no forward declaration in the main, compiler throws an error because it doesnt know what to do with an undefined function that is in main used.
            What happens if we DO forward declare the add function?
                Compilation of main.cpp and add.cpp starts
                add.cpp compiles with no problem
                main.cpp starts compiling, Compiler sees the forward declared add function and says ok this will be handled later.
                Then the linker sees theres a forward declared function. Searches the add functin all over the compiled and assembled object files
                If Linker is able to find add function defined somewhere the process continues without errors.
                If Linker is NOT able to find add function defined anywhere, linker throws an error because it doesnt know what to do with an undefined function that is used.

        As previously mentioned, manually adding forward declarations for every function you want to use that lives in another file can get tedious quickly.
        To solve this problem, Header files were created:


}
*/

//learncpp.com 2.11 - Heder files
/*
    What is a header file?
        Conventionally, header files are used to propagate a bunch of related forward declarations into a code file.
        Header files allow us to put declarations in one place and then import them wherever we need them.
        Header extensions are .h / .hpp

        Easier way to understand why header files exists is looking at the one we know so far, iostream.
            <iostream> is a header file in the standard library that contains input and output functions. Exact header file is <stdio.h>

    A header file consists of two parts:
        header guard: yet to learn "learncpp.com 2.12"
        header content (function forward declarations, identifiers etc.)

#include "math_operations.h"
#include <iostream>
int main()
{
    std::cout << "start" << "\n";
    std::cout << addition(2,3) << "\n";
    std::cout << subtraction(2,3) << "\n";
    std::cout << division(5.0,1.0) << "\n";
    std::cout << multiplication(2,3) << "\n";
    std::cout << "end"  << "\n";

    return 0;
*/

//learncpp.com 2.12 Header Guards:
/* I CANT BE ASKED TO FIX THIS RN
 * When a header file is included inside another header file, and both are used in main.cpp,
there will at least be 2 identical header content such as 2 identical functions. This will throw a compiler error
For Example:
    ---header1.h---                         // Created header1.h
        int add(int x, int y);              // Declared contents of header1.h

    ---header2.h---                         // Created  header2.h
        #include "header1.h"                // included header1.h as header2.h file content.

    ---header1.cpp---
        #include "header1.h"
        int add(int x, int y) {return x+y;}


    //  Before Preprocessing Stage:
    ---main.cpp---
    #include "header1.h"                    // Contents of header1.h will get copy pasted.
    #include "header2.h"                    // Contents of header2.h will get copy pasted.
    int main() {add(5,7); return 0;}        // Main function calls function add().

    // After Preprocessing Stage:
    ---main.cpp---
    int add(int x, int y);                  // Pasted contents of header1.h
    int add(int x, int y);                  // Pasted contents of header2.h
    int main() {add(5,7); return0;}         // Main calls the function add with arguments 5 and 7.

    // Compiling Stage:
    Because there are 2
*/
// #pragma once
// NO NEED FOR HEADER GUARDS FOR NOW BECAUSE WE WILL NOT DEFINE FUNCTIONS INSIDE HEADERS.


// learncpp.com lesson 2.13: How to design your first programs
//check d4_lrncpp_2_13.cpp and d4_lrncpp_2_13.h files. and main func ofc.

