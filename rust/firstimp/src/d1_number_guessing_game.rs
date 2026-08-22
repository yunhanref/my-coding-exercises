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