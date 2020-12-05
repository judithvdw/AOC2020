from typing import List, Tuple


def get_info(boarding_pass: str):
    fb = boarding_pass[:7].replace("F", "0").replace("B", "1")
    lr = boarding_pass[7:].replace("L", "0").replace("R", "1")
    row = int(fb, 2)
    column = int(lr, 2)
    seat_id = row * 8 + column
    return row, column, seat_id


def parse_input(blob: list):
    airplane_info = []
    for boarding_pass in blob:
        airplane_info.append(get_info(boarding_pass.strip()))
    return airplane_info


def get_missing_nr(seats: List[Tuple[int, int, int]]):
    nrs = [row[2] for row in seats]
    possible_nrs = [a for a in range(min(nrs), max(nrs))]
    return list((set(possible_nrs) - set(nrs)))[0]


if __name__ == '__main__':
    with open("5.txt") as f:
        blob = f.readlines()

    seats = parse_input(blob)
    print("Part 1:", max(map(lambda x: x[2], seats)))
    print("Part 2:", get_missing_nr(seats))
