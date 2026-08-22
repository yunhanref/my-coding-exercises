
//use std::ffi::CString;
//use std::cmp::Ordering;
//use rand::RngExt;
//use std::io;
//use std::ptr::null_mut;
use std::thread;
use std::time::Duration;
//use std::io::repeat;
//use rand::random_range;
//use rand::rand_core::utils::read_words;



//dots

pub fn dots() {
    thread::sleep(Duration::from_millis(500));
    println!(".");
    thread::sleep(Duration::from_millis(500));
    println!("..");
    thread::sleep(Duration::from_millis(500));
    println!("...");
}
