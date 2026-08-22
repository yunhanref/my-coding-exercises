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


//STRINGS AND EXAMPLES.
/*
//string types
//&str
//read only, immutable,
//Rust'ta her verinin tek bir sahibi (owner) vardır. Veriyi bir fonksiyona aktardığınızda normalde sahiplik oraya geçer ve eski değişken kullanılamaz hale gelir. & bunu engeller.
fn at_str() {
    let s1: &str = "&str";
    // & kullanmadan (Sahiplik Devredilir / Move):
    // let s2 = s1;
    // println!("{}", s1); // HATA! s1 artık geçersiz.

    // & kullanarak (Ödünç Alma / Borrowing):
    let s2 = &s1;
    println!("s1:   {}", s1); // Çalışır! s1 hâlâ geçerli.
    println!("s2 as &s1:   {}", s2); // Çalışır! s2 sadece s1'in adresini tutuyor.
}
fn main() {
    println!(":&str");
    at_str();
    println!(".String");
    string();
    println!(".to_tring");
    to_string();
    println!("string slices");
    string_slices();
    println!("stack emptied.")
}

//String type
//heap stored data, growable, slower.

fn string() {
    let mut string:String = String::new();
    string.push_str("XXXXXXXX");
    println!("pushed string is: '{string}'.")
}

//quick definition to_string()
//Data Origin: When you call .to_string() on a value (like a string literal &str or a number), Rust allocates new space on the heap.Ownership: It copies or formats the data into that newly allocated heap space, giving you an owned String type that you can change or pass around
fn to_string() {
    let quick_definition:String = "quick_string".to_string();
    println!("{quick_definition}")
}

fn string_slices() {
    println!("string slicing operations");
    let mut string: String = String::from("string to be sliced"); //string indexes start from 0 to n
    let slicer1 = &string[0..string.len()];
    println!("from 0 to end:    {slicer1}");
    let slicer2 = &string[0..10]; //take value referances from index 0 to 10 (excluded)
    println!("from index 0 to 9:  {slicer2}");
    (&mut string).push_str(" are wonderful!");
}
 */