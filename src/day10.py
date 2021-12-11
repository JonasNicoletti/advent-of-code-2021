chars = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
error_value = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
missing_value = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
missing_scores = []
with open("src/inputs/day10.txt") as f:
    lines = f.readlines()
    errors = []
    for line in lines:
        syntax = []
        for char in line.strip():
            if char in chars:
                if syntax[-1] == chars[char]:
                    syntax.pop()
                else:
                    errors.append(error_value[char])
                    syntax = []
                    break
            else:
                syntax.append(char)
        if syntax:
            c = 0
            for i, char in enumerate(syntax[::-1]):
                c *= 5
                c += missing_value[char]
            missing_scores.append(c)
    print(sum(errors))
    print(sorted(missing_scores)[len(missing_scores) // 2])
