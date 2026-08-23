#include <iostream> // Giriş ve çıkış işlemleri için
int main() //identifier = name of the function.
//al cpp programs must hae a main function
//int means the return value data type must be an integer
{   //functions have statemens. Statements are instructions that causes the program to make actions
    //standardlibrary::characterout.
    std::cout << "this is a string literal\nyes it is.\n"; //all values that put straight into the source code are called literals. (read-only, immutable)
    std::cout <<  5 << '\n'; //this is a literal integer
    std::cout << 'a'<< '\n'; //this is a literal character


    int x; //defined a variable object of int type thats name is x. Has no initializer!
    int width; //created object variable named width, data type = integer. Has no initializer
    width = 5; //assigned 5 to the variable, now width object holds the copied value of 5 in memory.
    //the program gives an advice: declaration and assignment can be joined, which means you can just say "int width = 5;" in one line.
    //this is called a copy initialization
    //initialization: variable takes value when created.
    //assignment: variable takes value after created.
    std::cout << width << '\n';

    [[maybe_unused]] double pi = 3.14159; //maybe_unused attribute tells the compiler that its okay if this variable is not used, compiler wont complain about it, will optimize these values out of the program.


    //INPUT: character in: cin operations.
    int input;
    std::cout << "enter number to print in the console: \n";
    std::cin >> input;
    std::cout << "you typed " << input << '\n';


    int in1;
    int in2;
    std::cout << "enter" << '\n';
    std::cin >> in1 >> in2;
    std::cout << in1 << " ---- " << in2 << '\n';
    //****BUFFERED CIN AND COUT****
    /*
    *This program inputs to two variables (this time as separate statements). We’ll run this program twice.
    Run #1: When std::cin >> x; is encountered, the program will wait for input. Enter the value 4. The input 4\n goes into the input buffer, and the value 4 is extracted to variable x.
    When std::cin >> y; is encountered, the program will again wait for input. Enter the value 5. The input 5\n goes into the input buffer, and the value 5 is extracted to variable y. Finally, the program will print You entered 4 and 5.
    There should be nothing surprising about this run.
    Run #2: When std::cin >> x is encountered, the program will wait for input. Enter 4 5. The input 4 5\n goes into the input buffer, but only the 4 is extracted to variable x (extraction stops at the space).
    When std::cin >> y is encountered, the program will not wait for input. Instead, the 5 that is still in the input buffer is extracted to variable y. The program then prints You entered 4 and 5.
    Note that in run 2, the program didn’t wait for the user to enter additional input when extracting to variable y because there was already prior input in the input buffer that could be used.
     */
    //std::cin is buffered because it allows us to separate the entering of input from the extract of input. We can enter input once and then perform multiple extraction requests on it.
    // << = insertion operator, >> = extraction operator
    int bufferinput1;
    int bufferinput2;
    std::cout << "enter values: " << '\n';
    std::cin >> bufferinput1 >> bufferinput2;
    std::cout << bufferinput1 << "  -  " << bufferinput2;

    return 0; //func returns 0 to the operating system
}

/*what happens when you run the cpp file?
 * First, the source code gets compiled to object files with a Compiler. Object files contain binary code
 * Second, object files are linked together with a Linker. Linker controls the binary, checks if libraries are used, connects libraries and creates final executable file.
 * Lastly, executable file is run and program complete.
 */
//Memory in cpp: An object is used to store a value in memory (RAM, or CPU registers). A variable is an object that has a name (identifier).
//in cpp, we dont specify the memory address we want to use, we assign, compiler finds.
//VARIABLES: variables are definitions.
//At runtime (when the program is loaded into memory and run), each object is given an actual storage location (such as RAM, or a CPU register) that it can use to store values. The process of reserving storage for an object’s use is called allocation. Once allocation has occurred, the object has been created and can be used.
