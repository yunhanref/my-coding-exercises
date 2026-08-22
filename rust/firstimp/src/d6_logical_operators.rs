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


//Logical Operators,
/*
//AND(x && y): returns true if both are true
//OR(x || y): returns false only if both are false
//NOT(!(value_to_change)): changes the boolean value of the variable given as parameter.
fn and_gate() {
    println!("and gate started");
    let a: u8 = 31;
    let true_bool: bool = true;
    let and_operation = a > 10 && true_bool; // true && false === true
    println!("a>10 && true_bool:    {and_operation}");
}

fn or_gate() {
    println!("or gate started");
    let b: i8 = -127;
    let false_bool: bool = false;
    if b < 0 || false_bool { // true || false === true
        println!("true");
    } else {
        println!("false");
    }
}

fn not_operator() {
    println!("not operator example");
    let a: u8 = 31;
    let b: i8 = -127;
    println!("converted:    {},{}", !(a > 10), !(b > 0)); // !(true), !(false) === false, true
}

fn main() {
    println!("and gate");
    and_gate();

    println!("or gate");
    or_gate();

    println!("not operator");
    not_operator();

    println!("end");
}
*/
//bit operators(FUH THIS SHI BRU)