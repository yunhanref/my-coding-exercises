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


//sicaklik hesaplama fahrenheit and celcius
/*
fn main() {
    println!("Hi, welcome to the temperature converter!");
    loop {
        let mut question:String = String::new();
        println!("please enter the operation you want to do: 1/2. fahrenheit to celsius(1) / celsius to fahrenheit(2)\n");
        io::stdin()
            .read_line(&mut question)
            .expect("Failed to read line");
        let question:i16 = question.trim().parse().expect("");
        //simdi sicaklik degerini girsin
        let mut temperature:String = String::new();
        println!("please enter the temperature you want to convert\n");
        io::stdin()
            .read_line(&mut temperature)
            .expect("failed to read line");
        let temperature:i16 = temperature.trim().parse().expect("");
        if question == 1 {
            println!("you choose fahrenheit to celsius.");
            let f_to_c = (temperature - 32) * 5/9;
            println!("{f_to_c}");
            break
        }
        else if question == 2 {
            println!("you choose celsius to fahrenheit.");
            let c_to_f = (temperature * 18/10) + 32;
            println!("{c_to_f}");
            break
        }
        else {
            println!("invalid; continue");
            continue
        }
    }
}
 */