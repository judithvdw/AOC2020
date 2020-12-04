import re
from typing import Tuple, List


def byr_valid(yr: str) -> bool:
    return len(yr) == 4 and yr.isdigit() and 1920 <= int(yr) <= 2002


def iyr_valid(yr: str) -> bool:
    return len(yr) == 4 and yr.isdigit() and 2010 <= int(yr) <= 2020


def eyr_valid(yr: str) -> bool:
    return len(yr) == 4 and yr.isdigit() and 2020 <= int(yr) <= 2030


def hgt_valid(hgt: str) -> bool:
    if hgt[-2:] == "in":
        if hgt[:-2].isdigit() and 59 <= int(hgt[:-2]) <= 76:
            return True
    elif hgt[-2:] == "cm":
        if hgt[:-2].isdigit() and 150 <= int(hgt[:-2]) <= 193:
            return True
    return False


def hcl_valid(hcl: str) -> bool:
    regex = re.compile('#[0-9a-f]{6}', re.I)
    match = regex.match(hcl)
    return bool(match)


def ecl_valid(ecl: str) -> bool:
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def pid_valid(pid: str) -> bool:
    return len(pid) == 9 and pid.isdigit()


def check_passports(passports: List[dict]) -> Tuple[int, int]:
    total_day_1 = 0
    total_day_2 = 0
    for passport in passports:
        if is_valid_part_1(passport):
            total_day_1 += 1
            if is_valid_part_2(passport):
                total_day_2 += 1
    return total_day_1, total_day_2


def is_valid_part_1(ppt: dict) -> bool:
    if ("byr" in ppt) and ("iyr" in ppt) and ("eyr" in ppt) and ("hgt" in ppt) and ("hcl" in ppt) and (
            "ecl" in ppt) and ("pid" in ppt):
        return True
    return False


def is_valid_part_2(ppt: dict) -> bool:
    return pid_valid(ppt["pid"]) and \
           ecl_valid(ppt["ecl"]) and \
           hcl_valid(ppt["hcl"]) and \
           hgt_valid(ppt["hgt"]) and \
           eyr_valid(ppt["eyr"]) and \
           iyr_valid(ppt["iyr"]) and \
           byr_valid(ppt["byr"])


def parse_input(blob: str) -> List[dict]:
    passports = blob.split("\n\n")
    passports = [passport.strip().split() for passport in passports]

    pasp_dicts = []
    for passport in passports:
        d = {}
        for entry in passport:
            spl = entry.split(":")
            d.update({spl[0]: spl[1]})
        pasp_dicts.append(d)

    return pasp_dicts


if __name__ == '__main__':
    with open("4.txt") as f:
        blob = f.read()

passports = parse_input(blob)

part_1, part_2 = check_passports(passports)
print("Part 1: ", part_1)
print("Part 2: ", part_2)
