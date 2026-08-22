/*
use std::ffi::CString;
use std::cmp::Ordering;
use rand::RngExt;
use std::io;
use std::ptr::null_mut;
use std::thread;
use std::time::Duration;
use std::io::repeat;
use rand::random_range;
use rand::rand_core::utils::read_words;
*/


//BASIC STACK MEMORY CHRONOLOGICAL EXECUTION EXAMPLE.
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

// MEMORY MANAGEMENT, OWNERSHIP, HEAP AND STACK PRINCIPALS ***
//resource: tech with tim, eydi gozeneli, core dumped, max taylor, lets get rusty
//UNDERSTANDING OWNERSHIP
//
fn main() {

}

 */
//OWNERSHIP: STACK COPY VS HEAP MOVE AND CLONE
/*
fn main() {
    //stack: copy trait
    let mut x:u8 = 10;
    let y:u8 = x;
    println!("x before changing x:  {x}\ny before changing x:  {y}");
    //output = x:10, y:10
    x = 30;
    dots();
    println!("x after changing x:  {x}\ny after changing x:  {y}");
    //output = x:30, y:10

    //heap: move trait and clone method
    let s1:String = String::from("this is s1");
    let s2:String = s1; //s1 moved inside s2 abandoning previous variable.
    //println!("{s1},{s2}"); //compile error: value used after moved.
    println!("{s2}"); //output = "this is s1"

    //to use both variables at the same time, we can use clone() method
    let s3:String = String::from("this is s3");
    let s4:String = s3.clone(); //creates a new clone of s1 and assigns it to s2.
    println!("{s3},{s4}"); //output: "this is s3, this is s3"
    //note: cloning is a big performance issue while dealing with bigger and more complex data. Must be avoided if possible.
}
 */