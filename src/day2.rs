use std::fs;

pub fn solve() -> () {
  part1();
  part2();
}


fn part1() {
  let content = fs::read_to_string("src/inputs/day2.txt").expect("Error reading file");
  let mut horizontal = 0;
  let mut depth = 0;
  content.lines().for_each(|line| {
    // split the line into command and number
    let (command, unit) = parse_input(line);

    // calculate the result
    match command {
      "forward" => horizontal += unit,
      "down" => depth += unit,
      "up" => depth -= unit,
      _ => panic!("Unknown command"),
    };
  });
  println!("{}", horizontal * depth);
}

fn part2() {
  let content = fs::read_to_string("src/inputs/day2.txt").expect("Error reading file");
  let mut horizontal = 0;
  let mut depth = 0;
  let mut aim = 0;
  content.lines().for_each(|line| {
    // split the line into command and unit
    let (command, unit) = parse_input(line);
    // calculate the result
    match command {
      "forward" => {
        horizontal += unit;
        depth += unit*aim;
      }
      "down" => aim += unit,
      "up" => aim -= unit,
      _ => panic!("Unknown command"),
    };
  });
  println!("{}", horizontal * depth);
}

fn parse_input(input: &str) -> (&str, i32) {
  let mut split = input.split_whitespace();
  let command = split.next().unwrap();
  let unit = split.next().unwrap().parse::<i32>().unwrap();
  return (command, unit);
}