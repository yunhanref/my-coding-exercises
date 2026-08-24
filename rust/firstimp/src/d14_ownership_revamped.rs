//ownership revamped.
/*
fn main() {
    //RE-USE OF:    STACK STORED VARIABLES
    //if a stack stored value is defiend in another variable, a new stack frame gets created and value gets copied in.
    //Copying is not as inefficient as cloning.
    let x: u8 = 255;
    let y = x;
    println!("x:    {x},  y:   {y}");
    let copied_literal:&str = "this string literal is stack stored, So it can be copeid and borrowed by variables other than its creation variable.";
    let copy_literal:&str = copied_literal;
    println!("copied_literal:   {}\ncopy_literal:    {}",copied_literal, copy_literal);

    //RE-USE OF:    HEAP STORED VARIABLES 1
    //move trait in rust
    let previous_owner: String = String::from("this string will be moved. The first variable cant borrow it");
    let new_owner = previous_owner; //value moved from str to str2 variable. Because they both point to the same heap address, to fix it value is moved.
    println!("new_owner:    {new_owner}");
    //RE-USE OF:    HEAP STORED VARIABLES 1
    //to use previous_owner again later, use .clone() while defining new_owner:
    //NOTE: CLONING GETS MORE EXPENSIVE AND INEFFICIENT AS CLONED VALUE GROWS.
    let cloned_variable:String = String::from("this string will be cloned. Both before and after declared variables can borrow it.");
    let clone_variable:String = cloned_variable.clone();
    println!("cloned_variable:  {}\nclone_variable: {}",cloned_variable,clone_variable); //both can be used thanks to cloning.

    // previous owner cant borrow its moved value again after it gets called by an outer function because the value is moved to the functions parameter variable.
    let string_to_send:String = String::from("this heap-stored string will be sent and assigned to an outer functions parameter, which moves it from its original creation variable");
    takes_ownership(string_to_send);
    //println!("as you can see: {string_to_send} Compiler gives an 'cant borrow moved value' error. Variable scope ended.");
    //to fix: call function as takes_owanership(string_to_send.clone()); !!

    let integer_to_parameter:i8 = 30;
    makes_copy(integer_to_parameter);
    println!("{integer_to_parameter} is still accessable.");


    let move_and_return_string:String = String::from("this string will be moved and then be returned");
    let new:String = moves_and_returns(move_and_return_string);
    println!("{new}");
}


fn takes_ownership(name:String) {
    println!("!!function called, added all values to the stack frame");
    println!("!!the variable created inside main which is: ({name}) is now moved to the parameter variable of this function.");
    println!("!!If you try to print the value after the takes_owanership fucntion call, compiler will complain that it has moved from creation variable and cant borrow it again. ");
    println!("!!to use the variable again, you can clone it.");
    println!("!!function end, stack frame deleted.");
}

fn makes_copy(sayi:i8) {
    println!("this function creates copies of stack stored variables.");
    println!("{sayi}");
    println!("variales used as parameter can be used after the function call because its a stack stored data, so compiler automaticly creates copy.");
}


fn moves_and_returns(move_and_return:String) -> String {
    println!("this functiom takes a variable as its parameter, then returns it where its called.");
    println!("{move_and_return}");
    move_and_return
}
 */