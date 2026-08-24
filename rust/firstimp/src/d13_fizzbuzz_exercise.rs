fn main() {
    println!("main executed");
    my_fizzbuzz_revamped();
    println!("main terminated");
}


/*
Disadvantages of my code/What I learned:
rust panics if other data type is entered. To solve this, use error handling with Ok and Err.
instead of long  if-else statements, match method is a better suit.

fn my_fizzbuzz() {
    println!("problem fizzbuzz: if divisible by 3 print fizz, if divisible by 5 print buzz, if divisible by both, print fizzbuzz!");
    loop {
        let mut question:String = String::new();
        println!("number:   ");
        io::stdin()
            .read_line(&mut question)
            .expect("unable to readline");
        let answer:u32 = question.trim().parse().expect("answer");
        if answer % 3 == 0 && answer % 5 == 0 {
            println!("fizzbuzz");
            continue
        }
        else if answer % 3 == 0 && answer % 5 != 0 {
            println!("fizz");
            continue
        }
        else if answer % 3 != 0 && answer % 5 == 0 {
            println!("buzz");
            continue
        }
        else {
            println!("cant divide with 3 or 5. Program terminated.");
            break
        }
    }
}
*/
/*
fn gemini_fizzbuzz() {

    println!("FizzBuzz Oyunu: 3'e bölünürse Fizz, 5'e bölünürse Buzz, her ikisine de bölünürse FizzBuzz!");

    loop {
        let mut question = String::new();
        println!("\nBir sayı girin:");

        io::stdin()
            .read_line(&mut question)
            .expect("Satır okunamadı");

        // Sayı parse edilemezse programı çökertmek yerine güvenli şekilde sonlandırırız
        let answer: u32 = match question.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("Geçersiz girdi. Program tekrar baslatiliyor...");
                continue;
            }
        };

        // Kalanları (mod) bir demet (tuple) olarak match ile kontrol ediyoruz
        match (answer % 3, answer % 5) {
            (0, 0) => println!("fizzbuzz"),
            (0, _) => println!("fizz"),
            (_, 0) => println!("buzz"),
            _ => {
                println!("3 veya 5 ile bölünemiyor. Program sonlandırıldı.");
                break;
            }
        }
    }
}
 */
//ACHIEVE
fn my_fizzbuzz_revamped() {
    loop {
        let mut question:String = String::new();
        println!("enter number");
        io::stdin()
            .read_line(&mut question)
            .expect("unable to readline");
        let answer:i32 = match question.trim().parse() {
            Ok(num) => num,
            Err(_) => {
                println!("input must be i32, retry:");
                continue
            }
        };
        match (answer % 3, answer % 5) {
            (0,0) => println!("fizzbuzz"),
            (0,_) => println!("fizz"),
            (_,0) => println!("buzz"),
            _ => {
                println!("non divisable 3 nor 5.    ");
                break
            }
        }
    }
}