mod day1;
mod day2;
mod day3;

fn main() {
  use clap::{load_yaml, App};

  let yaml = load_yaml!("cli.yml");
  let matches = App::from_yaml(yaml).get_matches();

  let day: i32 = matches
    .value_of("day")
    .unwrap_or("0")
    .parse()
    .expect("Failed to parse day number");

  // match day to a number
  match day {
    1 => day1::solve(),
    2 => day2::solve(),
    3 => day3::solve(),
    0 => {
      day1::solve();
      day2::solve();
      day3::solve();
    }
    _ => println!("Invalid day"),
  }
}
