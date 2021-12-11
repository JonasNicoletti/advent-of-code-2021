from collections import defaultdict

with open("src/inputs/day6.txt") as f:
    inputs = f.read().split(",")
    # inputs to ints
    inputs = [int(x) for x in inputs]
    lanternfishes = defaultdict(int)
    for i in inputs:
        lanternfishes[i] += 1
    days = 256
    for day in range(1, days+1):
        new_fishes = lanternfishes[0]
        for i in range(1, 9):
            lanternfishes[i-1] = lanternfishes[i]

        lanternfishes[8] = new_fishes
        lanternfishes[6] += new_fishes

    # sum all values of lanternfishes
    print(f"{sum(lanternfishes.values())}")
