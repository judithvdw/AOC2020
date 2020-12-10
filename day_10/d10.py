from collections import Counter
from itertools import groupby
from typing import List


def differences(adapters):
    adapters_in_order = sorted(adapters)

    diffs = [adapters_in_order[0]]
    for i in range(len(adapters_in_order) - 1):
        diffs.append(adapters_in_order[i + 1] - adapters_in_order[i])

    diffs.append(3)
    return diffs


def calc_combinations(diffs: List[int]) -> int:
    total = 1
    diffs = [str(i) for i in diffs[:-1]]
    groups = [''.join(g) for _, g in groupby(diffs)]
    for group in groups:
        if group[0] == '1':
            if len(group) == 1:
                continue
            elif len(group) == 2:
                total *= 2
            elif len(group) == 3:
                total *= 4
            elif len(group) == 4:
                total *= 7
            else:
                print("Go do maths or something")
    return total


if __name__ == '__main__':
    with open('10.txt') as f:
        adapters = [int(i) for i in f.readlines()]

    diffs = differences(adapters)
    count_diffs = Counter(differences(adapters))
    print("Part 1: ", (count_diffs[1]) * (count_diffs[3]))
    print("Part 2: ", calc_combinations(diffs))
