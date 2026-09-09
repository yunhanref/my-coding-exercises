#include "math_operations.h"
#include <iostream>
//learncpp.com 2.10 - Preprocessor Directives
/*
 9 CPP ISO PHASES OF TRANSLATION/BUILDING (FROM SOURCE CODE TO EXECUTABLE FILE.)
1) PREPROCESSING of the source code: (4 PHASES)
    1.1) What is a preprocessor directive?
        Directives are guide to the compiler that says run this first before anything else
        Directives are defined with hash tag. Such as #include, #pragma, #define, #ifndef, #ifdef etc.
    1.2) What is preprocessing stage?
        Preprocessing stage is where the following actions are done to set the source code ready for compiling:
        Perform specific actions towards the instructions of preprocessor directives.
        Example 1: "#define PI 3.14" directive tells the compiler to find and change anything named PI to 3.14
        Example 2: "#include <iostream>" directive tells the compiler to copy and paste all the contents of <iostream> library to the source code.
        Removing comments from the source code. (We can assume that comment operators are preprocessors.)
    1.3) After preprocessing, file extensions changes from .cpp to .i which stands for intermediate.

2) COMPILING the preprocessed source code to .s files. (gcc,clang etc.)
    2.1) Compiler takes the intermediate source code with .i extension and makes following actions:
        Compiler checks for errors, if there is an error, compiler will complain and execution will stop and end there.
        If the error check passes successfully, the code gets turned into ASM assembly code with the extension .s which stands for source.
        After that, the .s file gets sent to ASSEMBLER

3) ASSEMBLER
    3.1) Turns assembly code to object code (.s files into .o/.obj files.) / (assembly to binary)
    3.2) After that, the binary object files gets sent to linker for further building

4) linking object files to an executable.
    Links the functions etc. Outputs final .exe file.
*/
/* preprocessor directives:
#include <header_file.h>
    Copies and pastes all of the contents of header_file.h into the source code.

#define
    Used for defining macros.
    A macro is a rule that defines how input text is converted into replacement output text.
    Has two ways of usage.
        1) OBJECT-LIKE MACRO SUBSTITUTION:              #define IDENTIFIER substitution_text
            For example #define PI 3.14
            This states that anything named PI in the source code will be seen as 3.14.
        2) OBJECT LIKE MACRO WITHOUT SUBSTITUTION TEXT:    #define IDENTIFIER
            Unlike object-like macros with substitution text, macros of this form are generally considered acceptable to use.
            To understand the general use of this concept, we must know what a CONDITIONAL PREPROCESSOR DIRECTIVE is:

#ifdef {...} endif
    Used for CONDITIONAL COMPILATION where we specify which code will be compiled or not under specific conditions.
    If defined then perform {...}
    For example:
        #include <iostream>
        #define PRINT_JOE           // Defined a PRINT_JOE directive (NOTE: Ifdef or ifndef condition IDENTIFIERs doesnt need values.)
        int main()
        {
        #ifdef PRINT_JOE            // If PRINT_JOE directive is defined in the code, then perform(compile) actions below until endif:
            std::cout << "Joe\n";   // will be compiled since PRINT_JOE is defined
        #endif                      // Ending of the specific conditionally compiled code.
            return 0;
        }

#ifndef {...} endif
    Same as above. Only difference is performs(compiles) if IDENTIFIER is not defined.
    For example:
        #include <iostream>
        #define EREN
        int main()
        {
        ifndef NAZLI                        // If identifier NAZLI is not defined, perform(compile) actions below until endif:
            std::cout << NAZLI << "\n";     // Since NAZLI is not defined anywhere, the code between ifndef-endif will not get compiled.
        endif                               // Ending of the specific conditionally compiled code.
        }

#if 0 {...} endif
    Code between these will never be compiled no matter what.
#if 1 {...} endif
    Code between these will be compiled normally.
*/