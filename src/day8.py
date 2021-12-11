from collections import defaultdict


def get_translation(signals: [str]) -> dict:
    translation = defaultdict()
    for value in signals:
        if len(value) == 2:
            translation[1] = value
        elif len(value) == 3:
            translation[7] = value
        elif len(value) == 4:
            translation[4] = value
        elif len(value) == 7:
            translation[8] = value
    translation[6] = "".join(sorted([x for x in signals if len(
        x) == 6 and len(set(list(x)) & set(list(translation[1]))) == 1][0]))
    translation[9] = "".join(sorted([x for x in signals if len(
        x) == 6 and len(set(list(x)) & set(list(translation[1]))) == 2][0]))
    translation[5] = "".join(sorted([x for x in signals if len(
        x) == 5 and len(set(list(x)) & set(list(translation[4]))) == 3][0]))
    translation[0] = "".join(sorted([x for x in signals if len(
        x) == 6 and x not in (translation[6], translation[9])][0]))
    translation[3] = "".join(sorted([x for x in signals if len(
        x) == 5 and len(set(list(x)) & set(list(translation[1]))) == 2][0]))
    translation[2] = "".join(sorted([x for x in signals if len(
        x) == 5 and x not in (translation[3], translation[5])][0]))

    return translation


def get_value(output: str, signal: str) -> int:

    signals = signal.strip().split(" ")
    signal = [x for x in signals if set(list(x)) == set(list(output))][0]
    if len(signal) == 2:
        return 1
    elif len(signal) == 3:
        return 7
    elif len(signal) == 4:
        return 4
    elif len(signal) == 7:
        return 8
    elif len(signal) == 6:
        one = set(list([x for x in signals if len(x) == 2][0]))
        if len(set(list(signal)) & one) == 1:
            return 6
        elif len(set(list(signal)) & one) == 2:
            return 9
        return 0
    elif len(signal) == 5:
        four = set(list([x for x in signals if len(x) == 4][0]))
        if len(set(list(signal)) & four) == 2:
            return 2
        one = set(list([x for x in signals if len(x) == 2][0]))
        if len(set(list(signal)) & one) == 2:
            return 3
        return 5


with open("src/inputs/day8.txt") as f:
    lines = f.readlines()
    c = 0
    for line in lines:
        signal, output = line.split("|")
        tmp = ""
        for value in output.strip().split(" "):
            tmp += str(get_value(value, signal))
        print(tmp)
        c += int(tmp)


print(c)
