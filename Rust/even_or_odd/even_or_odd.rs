use std::io;
use std::thread;
use std::time::Duration;

fn main() {
    let mut number = String::new();
    println!("Enter a number:");
    io::stdin().read_line(&mut number).expect("Failed to read line");
    number = number.trim().to_string();
    if number.parse::<i32>().unwrap() % 2 == 0 {
        println!("The number is even.");
        thread::sleep(Duration::from_secs(1));
    }
    else {
        println!("The number is odd.");
        thread::sleep(Duration::from_secs(1));
    }
}