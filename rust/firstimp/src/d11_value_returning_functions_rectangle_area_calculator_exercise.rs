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



//functions that return value back where they are called.
/*
fn main() {
    println!("answers questions down below to calculate the area:\n");
    rectangle();
}

fn rectangle () -> u16{ // we specify a return type. Will return u16.
        //define parameters
    let mut width:String = String::new();
    let mut height:String = String::new();
    println!("enter width:  ");
    io::stdin()
        .read_line(&mut width)
        .expect("Failed to read line");
    let width:u16 = width.trim().parse().expect("Not a number");
    println!("width: {width}");
    println!("enter height:  ");
    io::stdin()
        .read_line(&mut height)
        .expect("Failed to read line");
    let height:u16 = height.trim().parse().expect("Not a number");
    println!("height: {height}");
    //define area value.
    let area = width * height;
    //print just in case
    println!("area is:{area}\n");
    //return
    area
}
 */