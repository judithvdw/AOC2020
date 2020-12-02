def parse_input(codes: list) -> list:
    cleaned = []
    for code in codes:
        code = [x.strip() for x in code.split(' ')]
        cleaned.append(code[0].split('-') + [code[1][0]] + [code[2]])
    return cleaned


def is_valid_part_1(code: list) -> bool:
    min_letters = int(code[0])
    max_letters = int(code[1])
    letter = code[2]
    pwd = code[3]
    nums = pwd.count(letter)

    return min_letters <= nums <= max_letters


def is_valid_part_2(code: list) -> bool:
    pos_1 = int(code[0]) - 1
    pos_2 = int(code[1]) - 1
    letter = code[2]
    pwd = list(code[3])

    return (pwd[pos_1] == letter) ^ (pwd[pos_2] == letter)


if __name__ == '__main__':
    with open("2.txt") as f:
        x = f.readlines()

    valid_1 = 0
    valid_2 = 0
    for code in parse_input(x):
        valid_1 += is_valid_part_1(code)
        valid_2 += is_valid_part_2(code)

    print("part 1: ", valid_1)
    print("Part 2: ", valid_2)
