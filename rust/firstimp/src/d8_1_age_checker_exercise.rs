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


//if else user input age checker:
/*
fn age_checker() {
    loop {
        let mut age:String = String::new(); //opens new empty string.
        io::stdin() //takes user input
            .read_line(&mut age)//dont put ; at the end. Otherwise rust will think the process ends.!!
            .expect("enter number");
        let age:u8 = age.trim().parse().expect("enter age");
        println!("answer. {age}");
    if age >= 18 {
        println!("welcome in");
        break
    }
    else if age < 18 || age > 120  {
        println!("invalid, try again");
        continue
    }
}
}
 */