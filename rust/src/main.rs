//use std::ffi::CString;
//use std::cmp::Ordering;
//use rand::RngExt;
use std::io;
//use rand::rand_core::utils::read_words;
//input output module

/*
fn main() {
    println!("the program has started...");
    println!("running other functions...");
    println!("guess the num between 1-10");
    let secret_number: u32 = rand::rng().random_range(1.=10);
    println!("the secret number is: {}", secret_number);
    // python example == random_number = random.randint(1,10)
    loop {
        let mut guess: String = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
        let guess: u32 = guess.trim().parse().expect("Please type a number!");
        println!("guess: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You guessed correctly!");
                break;
            }
        }
    }
}
*/
/*
fn main() {
    println!("main func started!");
    let mut number = 10;
    //let keyword is for creating new variables.
    //mut keyword makes the number mutable. Which means changeable.
    println!("mutable number before mutation: {number}");
    number = 11; //reassigning the variable by not including let.
    println!("mutable number after mutation: {number}");
}
 */
/*
fn main() {
    println!("day1 of learning rust");
    let mut int: u32  = 32;
    println!("var1 before mutation:  {int}");
    int = 33;
    println!("var1 before mutation:  {int}");
    const PI_NUM: f32 = 3.141592653589793;
    println!("pi:  {PI_NUM}");
    let mut nega: i32 = -32;
    println!("{nega}");
    nega = -33;
    println!("{nega}");
}
*/
/*
fn main() {
    println!("BINARY");
    let var1: i8 = -32;
    let var: u8 = 3;
    println!("{:b}", var1); //output =  11100000
    println!("{var1}"); //output = -32
    println!("{}",var1); //output = -32
    println!("{:#032b}",var1); //output = 0b00000000000000000000000011100000
    println!("{:#b}",var1); //output = 0b11100000
    println!("{var:#010b}"); //you can type it like this as well.

    println!("HEXADECIMAL");
    println!("{:#X}", var1); //output = 0xE0

    println!("DECIMAL");
    println!("{:#e}",var1);  //output = -3.2e1 ==== -3.2 x 10 = -32
}
*/
/*
fn main() {
    let mut var1: u8 = 19;
    let var2 = 42;
    let var3:u8= 255;
    var1 += var2;
    println!("var1 + var2 is {0},\nvar2  is {1},\nvar2({1}) is smaller than var3({2})", var1,var2,var3);
    //***important: you can use the variables indexes to showcase them.
    //OUTPUT:
    //var1 + var2 is 61,
    // var2  is 42,
    // var2(42) is smaller than var3(255)
}
*/
 */
/*
fn main() {
    let bool1:bool = false;
    let bool2:bool = false;
    println!("bool1({0}) is false.\nbool2({1}) is true.",bool1,bool2);
}
 */
/*
fn main() {
    let char1:char = '🐐';
    let char2:char = '🦀';
    println!("{1} is smaller than {0}",char1,char2); //🦀 is smaller than 🐐
}
 */
/*
fn main() {
    let float:f32 = 2.71;
    let from_float_to_int:u8 = float as u8;
    println!("we turned {0} to u8: {1}", float, from_float_to_int); //we turned 2.71 to u8: 2
}
 */
/*
fn main() {
    println!("arraylara gectik");
    let array: [u8;5] = [1,2,3,4,5]; //5 adet 8bit yer acti.
    println!("first value: {0}\nlast value: {1} ",array[0],array[4]);
    let char_array:[char;3] = ['a', 'b', 'c']; //3 adet char acti.
    println!("{1} is bigger than {0}",char_array[1],char_array[2]);
}
 */
/*
fn main() {
    println!("starting over");
    let mut unsigned:u8 = 255; //takes values [0,255]
    println!("u8 before: {}", unsigned);
    unsigned = 0;
    println!("u8 after: {}", unsigned);
    let mut signed:i8 = -128; //takes values [-128,127]
    println!("i8 before: {}", signed);
    signed = 127;
    println!("i8 after: {}", signed);


    //datatypes:
    let _int:u8 = 31;
    let mut float:f32 = 3.31;
    println!("f32: {}", float);
    let float_to_int:u8 = float as u8;
    println!("new var created from float by making it f32 to u8: {}", float_to_int);
    const EULER:f32 = 2.71;
    let bool:bool = true;
    let char1:char = 'a';
    let char2:char = '神';
    let char_array: [char;4] = ['e', 'r', 'e', 'n'];
    let _int_array:[i8;3] = [1,2,3];
    let _flt_array:[f32;4] = [1.11,1.22,1.33,1.44];
    println!("all values: \n{1}\n{0}",bool,char1);
    println!("{}",char_array[1]);
    let _xarray = [2];    //if you dont specify data type of an array, rust will try and name it itself.
    //by default its i32 which takes unneccesary spaces. to make it more efficient we should specify it as u8
    println!("{EULER}");

    if float > EULER {
        println!("{float} > {EULER}"); //T
    }
    else {
        println!("{char2}");
    }
    float = 2.31;
    if float > EULER {
        println!("{float} > {EULER}"); //F
    }
    else if float == EULER {
        println!("float equal euler")
    }
    else {
        println!("float({float}) < EULER({EULER})")
    }

}
 */
/*
fn main() {
    println!("day two of learning rust babyyyy");
    let tuple = (1,-3.99,true,"string",'a',[1,2,3],(1,true));
    println!("{}",tuple.6.1); //i couldnt write it in the {} idk why.
    // tuple destructuring:
    let (a,b,c,d,e,_f,_g) = tuple;
    println!("a = {}, b = {}, c = {}, d = {}, e = {}",a,b,c,d,e);
}
 */

//STACK MEMORY MANAGEMENT EXAMPLE.
/*
fn main() {
    let x:u8 = 1;
    println!("main() and x added to stack, foo() called.");
    foo();
    println!("{x}");
    println!("If you see this last, That means this is the last message of main()");
}
fn foo() {
    let y:u8 = 2;
    println!("foo() and y added to stack, bar() called.");
    bar();
}
fn bar(){
    let z:u8 = 3;
    println!("bar() and z added to stack, nothing is called.");
    println!("the stack is complete. Now deletion is on the way.")
}
 */

//string exercises (will return...)
fn main() {
    println!("input?    ");
    let mut question:String = String::new();
    io::stdin()
        .read_line(&mut question)
        .expect("Failed to read line");
    println!("you typed:     {question}");
}