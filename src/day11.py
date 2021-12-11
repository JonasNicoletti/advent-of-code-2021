flashes = 0
with open("src/inputs/day11.txt") as f:
    octopuses = [list(map(int, list(line.strip()))) for line in f]

adjacents = [(0, 1), (0, -1), (1, 0), (-1, 0),
             (1, 1), (1, -1), (-1, 1), (-1, -1)]

flashes = 0
total_octopuses = len(octopuses)*len(octopuses)


def flash(i, j, octopuses):
    global flashes

    octopuses[i][j] += 1
    if octopuses[i][j] == 10:
        flashes += 1
        for x, y in adjacents:
            try:
                if i+x >= 0 and j+y >= 0:
                    flash(i+x, j+y, octopuses)
            except IndexError:

                pass

    return octopuses


# for day in range(100):
day = 0
while True:
    day += 1
    flashes = 0
    for i, row in enumerate(octopuses):
        for j, octopus in enumerate(row):
            octopuses = flash(i, j, octopuses)

    print(f"Day {day}: {flashes} out of {total_octopuses}")
    octopuses = [[0 if octopus > 9 else octopus for octopus in row]
                 for row in octopuses]

    if flashes == total_octopuses:
        break
