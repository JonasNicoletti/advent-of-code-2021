with open("src/inputs/day9.txt") as f:
    # read input as matrix of ints
    input_matrix = [list(map(int, list(line.strip()))) for line in f]
    # find adjant for each element
    low_points = []
    for i, row in enumerate(input_matrix):
        for j, elem in enumerate(row):
            is_low_point = True
            # check up
            if i > 0:
                is_low_point = is_low_point and input_matrix[i-1][j] > elem
            # check down
            if i < len(input_matrix)-1:
                is_low_point = is_low_point and input_matrix[i+1][j] > elem
            # check left
            if j > 0:
                is_low_point = is_low_point and input_matrix[i][j-1] > elem
            # check right
            if j < len(input_matrix[i])-1:
                is_low_point = is_low_point and input_matrix[i][j+1] > elem
            if is_low_point:
                low_points.append((i,j))

    print(sum([input_matrix[i][j]+1 for (i,j) in low_points]))

    # find basins
    def find_adjacents(i, j, input_matrix, basins):
        adjacents = []
        if i > 0:
            if input_matrix[i-1][j] < 9 and (i-1, j) not in basins:
                adjacents.append((i-1, j))

        if i < len(input_matrix)-1:
            if input_matrix[i+1][j] < 9  and (i+1, j) not in basins:
                 adjacents.append((i+1, j))

        if j > 0:
            if input_matrix[i][j-1] < 9  and (i, j-1) not in basins:
                adjacents.append((i, j-1))

        if j < len(input_matrix[i])-1:
            if input_matrix[i][j+1] < 9  and (i, j+1) not in basins:
                adjacents.append((i, j+1))

        return adjacents
    basins = []
    for (i,j) in low_points:
        basin = [(i,j)]
        is_run = True
        while is_run:
            tmp = []
            for (i,j) in basin:
                tmp += find_adjacents(i, j, input_matrix, basin)
                print(tmp)
            if len(tmp) == 0:
                is_run = False
            else:
                basin += tmp
        print(basin)
        basins.append(len(set(basin)))
top3 = sorted(basins)[-3:]
print(top3[0]*top3[1]*top3[2])

