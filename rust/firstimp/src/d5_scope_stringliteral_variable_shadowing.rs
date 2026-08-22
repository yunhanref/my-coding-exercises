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


//scope,raw string literal, variable shadowing.
/*
fn main() {
    fn scope() {
        println!("created variable a in outer scope");
        let a:u8 = 10;
        {
            println!("created sub scope inside main scope.");
            let b:u8 = 33;
            println!("both a({a}), and b({b}) can be accessed in the inner scope");
            println!("but when we try to call b outside of its creation scope, rust wont be able to find it");
            println!("because after the inner scope curly brackets, all the inner values will be dropped automaticly, resulting in outer caller to not finding it");
        }
    }

    fn raw_string_literatal() {
        println!(r##"this is a raw string that shows how to put tirnak inside a string: \"#merahba\" ..."##);
    }
    println!("call calling scope()");
    scope();
    println!("call raw_string_literatal()");
    raw_string_literate();
    println!("call variable_shadowing()");
    variable_shadowing();
    println!("main ended and will be deleted on the stack after this");

    fn variable_shadowing() {
        let val:u8 = 10;
        {
            println!("var before inner var shadowing: {val}");
            let val:&str = "shadow"; //changed an outer value.
            println!("after inner var shadowing: {val}"); //prints changed value
        }
        println!("experiment {val}"); //prints original value
    }
}
/*