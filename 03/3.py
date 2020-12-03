from typing import List


def calc_trees(track: List[str], down: int, right: int) -> int:
    current_width_index = 0
    trees = 0

    for y in range(0, len(track), down):
        if track[y][current_width_index] == '#':
            trees += 1
        current_width_index = (current_width_index + right) % len(track[0])

    return trees


if __name__ == '__main__':
    with open("3.txt") as f:
        inp = f.readlines()
        track = [i.strip() for i in inp]

    print("part 1: ", calc_trees(track, 1, 3))
    print("part 2: ", calc_trees(track, 1, 1) * calc_trees(track, 1, 3) * calc_trees(track, 1, 5) * calc_trees(track, 1, 7) * calc_trees(track, 2, 1))
