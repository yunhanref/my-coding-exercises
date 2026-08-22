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


//loop exercise. OUTER LOOPS AND OK,ERR methods.
//Ok() contains the success value
//Err() contains the failure value
/*
fn main() {
    'outer: loop { // 1. Label the outer loop
        println!("please enter your age");
        let mut age:String = String::new();
        io::stdin()
            .read_line(&mut age)
            .expect("failed to read line");

        let mut age: i8 = match age.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        let mut year: u16 = 2026;

        if age < 18 {
            println!("you are not old enough ({age}), time will pass now.");
            loop {
                age += 1;
                year += 1;
                println!("you are {age} years old now. Year is: {year}");
                dots();
                if age == 18 {
                    println!("congrats you are now old enough {age}, {year}.");
                    break 'outer; // 2. Break the outer loop directly
                }
            }
        } else {
            println!("you are old enough {age}-{year}");
            break;
        }
    }
}
*/

//while loop
/*
fn main() {
    let mut a:f32 = 1.0;
    while a<2.0 {
        println!("{a:.3}");
        a +=0.1;
        dots()
    }
}
 */

//for loop
/*
fn main() {
    let list = [1,2,3,4,5];
    for i in list {
        println!("{i}");
    }
    for i in 1..=10 {
        println!("{i}");
    }
}
 */