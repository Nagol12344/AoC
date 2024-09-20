use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let number = 0;
    let biggestnumber= 0;
    // File hosts.txt must exist in the current path
    if let Ok(lines) = read_lines("./test_data.txt") {
        for line in lines.flatten() {
            let line_int = line.parse::<i32>().unwrap();
            
        }
    }
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
