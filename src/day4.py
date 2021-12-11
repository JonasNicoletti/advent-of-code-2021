boards = []

with open("src/inputs/day4.txt") as f:
    lines = f.readlines()
    numbers = lines[0].split(",")
    board = []
    for line in lines[2:]:
        line = line.split()
        if len(line) == 0:
            boards.append(board)
            board = []
        else:
            board.append([(x, False) for x in line])
    boards.append(board)

def check_win(board):
    # check in any row or columns if there is a win
    # get row where all true
    return any([row for row in board if all([x[1] for x in row])]) or any([col for col in zip(*board) if all([x[1] for x in col])])

def evaluate(boards, numbers):
    winning_boards = set()
    for num in numbers:
        for i, board in enumerate(boards):
            for j, row in enumerate(board):
                for k, col in enumerate(row):
                    if col[0] == num:
                        boards[i][j][k] = (col[0],  col[0] == num)
            if check_win(board):
              winning_boards.add(i)
              print(winning_boards)
              if len(winning_boards) == len(boards):
                return int(num) * sum([sum([int(x[0]) for x in row  if not x[1]]) for row in board])


print(evaluate(boards, numbers))
