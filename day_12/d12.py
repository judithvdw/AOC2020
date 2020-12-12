from typing import Tuple, List


def sail_away(directions: List[Tuple[str, int]]) -> Tuple[int, int]:
    degrees_to_direction = {90: "E", 180: "S", 270: "W", 0: "N"}
    degrees = 90
    ns = 0
    ew = 0
    for direction, num in directions:
        if direction == "F":
            direction = degrees_to_direction[degrees]
        if direction == "N":
            ns -= num
        if direction == "S":
            ns += num
        if direction == "E":
            ew += num
        if direction == "W":
            ew -= num
        if direction == "L":
            degrees = (degrees - num) % 360
        if direction == "R":
            degrees = (degrees + num) % 360
    return ns, ew


def waypoint_wackyness(directions: List[Tuple[str, int]]) -> Tuple[int, int]:
    ns = 0
    ew = 0
    waypoint_ns = -1
    waypoint_ew = 10
    for direction, num in directions:
        if direction == "F":
            ns += waypoint_ns * num
            ew += waypoint_ew * num
        if direction == "N":
            waypoint_ns -= num
        if direction == "S":
            waypoint_ns += num
        if direction == "E":
            waypoint_ew += num
        if direction == "W":
            waypoint_ew -= num
        if direction in ["L", "R"]:
            if (num == 90 and direction == "L") or (num == 270 and direction == "R"):
                waypoint_ew, waypoint_ns = waypoint_ns, waypoint_ew * -1
            if num == 180:
                waypoint_ew, waypoint_ns = waypoint_ew * -1, waypoint_ns * -1
            if (num == 90 and direction == "R") or (num == 270 and direction == "L"):
                waypoint_ew, waypoint_ns = waypoint_ns * -1, waypoint_ew
    return ns, ew


if __name__ == '__main__':
    with open('12.txt') as f:
        directions = [(line[0], int(line[1:].strip())) for line in f.readlines()]

    end = sail_away(directions)
    print("part 1:", abs(end[0]) + abs(end[1]))

    end = waypoint_wackyness(directions)
    print("part 2:", abs(end[0]) + abs(end[1]))
