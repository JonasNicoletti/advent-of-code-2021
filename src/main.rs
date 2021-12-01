mod day1;

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
    1 => day1::main(),
    0 => {
      day1::main();
    }
    _ => println!("Invalid day"),
  }
}
