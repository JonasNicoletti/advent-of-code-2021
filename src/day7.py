with open("src/inputs/day7.txt") as f:
    crabs = [int(x) for x in f.read().split(",")]
    min_fuel = 0
    for i in range(max(crabs)):
      temp = sum([sum(range(0, abs(x - i)+1)) for x in crabs])
      if min_fuel == 0:
        min_fuel = temp
      else:
        if temp < min_fuel:
          min_fuel = temp
print(min_fuel)