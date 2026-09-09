#include <stdbool.h>
#include <stdio.h> //input output library
//channel: BroCode 6hr tutorial on C
/*this is how to comment alltogether
    *
    */
/*printing
    *printf("this is how you print\n"); // use \n at the end
    *printf("new line");
    */
/*format specifiers:
* %d(deciaml integer) for integers,
* %f(float) for floats, HOLDS 6 7 DIGITS
* &lf(long float for doubles, HOLDS 15 17 DIGITS. double the size of normal float. Thats why its called a duble.
* %c(character) single characters
*/


int main()
{
    //creating variables

    int my_age = 19; //integer
    bool is_alive = true; //true boolean
    bool does_understand_rust = false; //false boolean
    printf("I'm %d years old.\n Im currently alive(%d)\n. I do understand rust...(%d)\n", my_age, is_alive, does_understand_rust);
    /*rust version:
     *let my_age:u8 = 19;
     *let is_alive:bool = true;
     *let does_understand_rust:bool = false;
     *println!("Im {} years old", my_age);
    */

    float my_gpa = 3.24;
    float weather = -10.4;
    printf("You can change printed digit count by adding .digitcount before lf: %.2f\n",my_gpa);
    printf("My gpa is:  %f and weather here is %f\n",my_gpa, weather);

    double pi = 3.1415926535807;
    printf("Long floats or doubles are longer floats such as: %lf\n",pi);
    printf("You can change printed digit count after dot by adding .digitcount before lf: %.1lf, max: %.15lf \n",pi,pi);

    char a = 'a';
    char h = 'h';
    char m = 'm';
    char e = 'e';
    char t = 't';
    printf("%c%c%c%c%c",a,h,m,e,t); //output = ahmet
    return 0;
}