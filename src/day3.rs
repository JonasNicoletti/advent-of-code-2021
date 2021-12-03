use std::fs;

pub fn solve() -> () {
  part1();
  part2();
}

fn part1() {
  let content = fs::read_to_string("src/inputs/day3.txt").expect("Error reading file");
  let lines: Vec<_> = content.lines().collect();
  let mut gamma = String::new();
  let mut epsilon = String::new();

  for i in 0..lines[0].len() {
    let most_common = find_most_common(&lines, i);
    if most_common == '0' {
      gamma.push_str("0");
      epsilon.push_str("1");
    } else {
      gamma.push_str("1");
      epsilon.push_str("0");
    }
  }

  let gamma: u32 = u32::from_str_radix(&gamma, 2).unwrap();
  let epsilon: u32 = u32::from_str_radix(&epsilon, 2).unwrap();

  println!("Part 1: {}", gamma * epsilon);
}

fn part2() {
  let content = fs::read_to_string("src/inputs/day3.txt").expect("Error reading file");

  let lines: Vec<_> = content.lines().collect();

  fn equality(a: char, b: char) -> bool {
    return a == b;
  }

  fn desequality(a: char, b: char) -> bool {
    return a != b;
  }

  let oxygen_generator_rating = evalute_rating_by(lines.to_vec(), &equality);
  let c02_scrubber_rating = evalute_rating_by(lines.to_vec(), &desequality);

  println!("Part 2: {}", oxygen_generator_rating * c02_scrubber_rating);
}

fn evalute_rating_by<F>(mut lines: Vec<&str>, mut filter: F) -> u32
where
  F: FnMut(char, char) -> bool,
{
  for i in 0..lines[0].len() {
    let most_common = find_most_common(&lines, i);

    lines = lines
      .into_iter()
      .filter(|line| filter(line.chars().nth(i).unwrap(), most_common))
      .collect();

    if lines.len() == 1 {
      return u32::from_str_radix(&lines[0], 2).unwrap();
    }
  }
  return 0;
}

fn find_most_common(lines: &Vec<&str>, i: usize) -> char {
  let mut count_ones = 0;
  for line in lines {
    if line.chars().nth(i).unwrap() == '1' {
      count_ones += 1;
    }
  }

  let count_zeros = lines.len() - count_ones;

  if count_zeros > count_ones {
    return '0';
  } else {
    return '1';
  }
}
