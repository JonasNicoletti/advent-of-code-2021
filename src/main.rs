use std::collections::HashMap;
mod day1;
mod day2;

fn main() {
  use clap::{load_yaml, App};

  let yaml = load_yaml!("cli.yml");
  let matches = App::from_yaml(yaml).get_matches();

  let day = matches.value_of("day").unwrap_or("all");
  let mut days: HashMap<&str, fn() -> ()> =
    HashMap::from([("1", day1::main), ("2", day2::main)]);

  if day == "all" {
    for (day, day_fn) in days {
      println!("Running day {}", day);
      day_fn();
    }
  } else {
    println!("Running day {}", day);
    days.get(day).unwrap_or(unknown_day)();
  }
}
fn unknown_day() {
  println!("Unknown day");
}
