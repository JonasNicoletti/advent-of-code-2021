use std::fs;
use std::vec::Vec;

pub fn solve() -> () {
  part1();
  part2();
}

fn part1() {
  // read file and convert each line to a int32
  let contents = fs::read_to_string("src/inputs/day1.txt").expect("Error reading file");
  let mut total = 0;
  let mut previus = i32::MAX;
  for line in contents.lines() {
    let num = line.parse::<i32>().unwrap();
    if num > previus {
      total += 1;
    }
    previus = num;
  }
  println!("{}", total);
}

fn part2() {
  let contents = fs::read_to_string("src/inputs/day1.txt").expect("Error reading file");
  let mut total = 0;
  let mut previus = i32::MAX;
  let mut current = Vec::new();

  for line in contents.lines() {
    let num = line.parse::<i32>().unwrap();
    if current.iter().count() < 3 {
      current.push(num);
      continue;
    }
    total += is_larger(&current, previus);
    previus = current.iter().sum::<i32>();
    current.remove(0);
    current.push(num);
  }
  // for the last element
  total += is_larger(&current, previus);
  println!("{}", total);
}

fn is_larger(vec: &Vec<i32>, previus: i32) -> i32 {
  let current_sum = vec.iter().sum::<i32>();
  if current_sum > previus {
    return 1;
  }
  return 0;
}
