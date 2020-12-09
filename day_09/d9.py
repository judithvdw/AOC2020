from itertools import combinations


def has_sum_in_preamble(preamble, num) -> bool:
    sums = combinations(preamble, 2)
    for sum in sums:
        if sum[0] + sum[1] == num:
            return True
    return False


def find_num(xmas: list, preamb_len) -> int:
    for i in range(preamb_len, len(xmas)):
        preamble = xmas[i - preamb_len:i]
        num = xmas[i]
        if not has_sum_in_preamble(preamble, num):
            return num
    return -1


def find_continuous_streak(xmas, num):
    sum_list = []
    i = 0
    while sum(sum_list) != num:
        if sum(sum_list) < num:
            sum_list.append(xmas[i])
            i += 1
        elif sum(sum_list) > num:
            sum_list.pop(0)
    return min(sum_list) + max(sum_list)


if __name__ == '__main__':
    with open("9.txt") as f:
        xmas = [int(i) for i in f.readlines()]

    PREAMBLE_LENGTH = 25

    part_1 = find_num(xmas, PREAMBLE_LENGTH)
    print("part 1:", part_1)
    print("part 2:", find_continuous_streak(xmas, part_1))
