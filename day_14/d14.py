from typing import List, Dict


def apply_mask_1(mask: str, value: str) -> str:
    new_value = ""
    assert len(mask) == len(value)
    for m, v in zip(mask, value):
        if m == 'X' or m == v:
            new_value += v
        else:
            new_value += m
    return new_value


def run_program_1(prog: List[str]) -> Dict[int:int]:
    register = {}
    mask = ""
    for line in prog:
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1].strip()
        else:
            address = line[0][4:-1]
            value = str(bin(int(line[1])))[2:].zfill(36)  # lol
            register[address] = int(apply_mask_1(mask, value), 2)
    return register


def apply_mask_2(mask: str, address: str) -> str:
    new_address = ""
    assert len(mask) == len(address)
    for m, a in zip(mask, address):
        if m == '0':
            new_address += a
        if m == '1':
            new_address += '1'
        if m == 'X':
            new_address += 'X'
    return new_address


def get_addresses(address_with_floats: str) -> List[int]:
    addresses = []
    xes = address_with_floats.count("X")
    num_permutations = 2 ** xes
    max_len = len(str(bin(num_permutations))[2:])
    for i in range(num_permutations):
        digits_to_fill = list(str(bin(i))[2:].zfill(max_len - 1))
        new_address = ""
        for bit in address_with_floats:
            if bit == "X":
                new_address += digits_to_fill.pop(0)
            else:
                new_address += bit
        addresses.append(int(new_address, 2))
    assert len(addresses) == num_permutations
    return addresses


def run_program_2(prog: List[str]) -> Dict[int:int]:
    register = {}
    mask = ""
    for line in prog:
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1].strip()
        else:
            address = str(bin(int(line[0][4:-1])))[2:].zfill(36)
            address_with_floats = apply_mask_2(mask, address)
            addresses = get_addresses(address_with_floats)
            for ad in addresses:
                register[ad] = int(line[1])
    return register


if __name__ == '__main__':
    with open("14.txt") as f:
        masks_and_mems = f.readlines()

    print("part 1:", sum(run_program_1(masks_and_mems).values()))
    print("part 2:", sum(run_program_2(masks_and_mems).values()))
