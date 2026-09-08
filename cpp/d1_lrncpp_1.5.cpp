#include <iostream> // input output

int main()  //identifier = name of the function.
//all cpp programs must haw a main function
//int means the return value data type must be an integer (NOTE: main fn is the only fn that doesnt need a return value. )

{
    //functions have statemens. Statements are instructions that causes the program to make actions
    //standardlibrary::characterout.

    std::cout << "this is a string literal\nyes it is.\n";  //all values that put straight into the source code are called literals. (read-only, immutable)
    std::cout <<  5 << '\n';                                //this is a literal integer
    std::cout << 'a'<< '\n';                                //this is a literal character


    int x;          //defined a variable object of int type named x. Has no initializer!
    int width;      //created object variable named width, data type = integer. Has no initializer
    width = 5;      //assigned 5 to the variable, now width object holds the copied value of 5 in memory.
                        //the program gives an advice: declaration and assignment can be joined, which means you can initialise the variable right away like "int width {5};" or "int width = 5;" in one line.
                            //this is called a copy initialization, the empty width variable gets initialised later.
                                //initialization: variable takes value when created.
                                    //assignment: variable takes value after created.

    //CPP NOTE: MAV VALUE OF INT IS I32, WHICH MEANS IT CAN TAKE VALUES FROM [-2.17BILLION , +2.17BILLION] SPACE.
    int exceeding_int {3000000000};
    std::cout << exceeding_int;       //printed value is 2.17 billion because the current value (3billion) exceeds maximum value.

    //CPP NOTE: UNINITIALISED VARIABLES ARE UNPREDICTABLE, MAKE YOUR CODE PERFECT LIKE RUST.
    int uninit;     //uninitialized var
    float uninit2;  //uninitialized var
    double uninit3; //uninitialized var
    char uninit4;   //uninitialized var
    bool uninit5;   //uninitialized var
    std::cout << uninit << "\n" << uninit2 << "\n" << uninit3 << "\n" << uninit4 << "\n" << uninit5 << "\n";



    std::cout << width << '\n';

    [[maybe_unused]] double pi = 3.14159;   //maybe_unused attribute tells the compiler that its okay if this variable is not used,
    //compiler wont complain about it, will optimize these values out of the program.


    //INPUT: character in: cin operations.
    // << = insertion operator, >> = extraction operator.
    int input;                                                  //created an empty variable for later initialization.
    std::cout << "enter number to print in the console: \n";    //string inserted to cout and printed to the screen.
    std::cin >> input;                                          //cin requests an input from user, then initializes input value to the variable.
    std::cout << "you typed " << input << '\n';                 //result.




    //****BUFFERED CIN AND COUT****
    int in1;                                        //created an empty variable for later initialization.
    int in2;                                        //created an empty variable for later initialization.
    std::cout << "enter" << '\n';                   //string inserted to cout and printed to the screen.
    std::cin >> in1 >> in2;                         //cin requests an input from user, then initializes input value to the variables.
    std::cout << in1 << " ---- " << in2 << '\n';
    /*
    *This program inputs to two variables (this time as separate statements). We’ll run this program twice.
    Run #1: When std::cin >> x; is encountered, the program will wait for input. Enter the value 4. The input 4\n goes into the input buffer, and the value 4 is extracted to variable x.
    When std::cin >> y; is encountered, the program will again wait for input. Enter the value 5. The input 5\n goes into the input buffer, and the value 5 is extracted to variable y. Finally, the program will print You entered 4 and 5.
    There should be nothing surprising about this run.
    Run #2: When std::cin >> x is encountered, the program will wait for input. Enter 4_space_5. The input 4_space_5\n goes into the input buffer, but only the 4 is extracted to variable x (extraction stops at the space!!!).
    When std::cin >> y is encountered, the program will not wait for input. Instead, the 5 that is still in the input buffer is extracted to variable y. The program then prints You entered 4 and 5.
    Note that in run 2, the program didn’t wait for the user to enter additional input when extracting to variable y because there was already prior input in the input buffer that could be used.
    //std::cin is buffered because it allows us to separate the entering of input from the extract of input. We can enter input once and then perform multiple extraction requests on it.
    //must be used with caution by professional developers.
    */
    int bufferinput1;
    int bufferinput2;
    std::cin >> bufferinput1 >> bufferinput2;
    std::cout << bufferinput1 << "  -  " << bufferinput2;
    //instead of pressing enter after the first value -thanks to buffering- you can add a space and type the other value
    //Kullanıcı 35 36 yazıp Enter'a bastığında, girdiler işletim sistemi tarafından std::cin tamponuna aktarılır;
    //ardından >> operatörü sırasıyla ilk sayı 35'i bufferinput1'e, aradaki boşluğu atlayarak ikinci sayı 36'yı ise bufferinput2'ye atar.
    //std::cout << "enter values: " << '\n';
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


