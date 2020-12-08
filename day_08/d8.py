from typing import List, Union
from copy import deepcopy


def parse_input(inp: list) -> List[List[Union[str, int]]]:
    program = []
    for line in inp:
        line = line.split()
        program.append([line[0], int(line[1])])
    return program


def run_program(program: List[List[Union[str, int]]]) -> (int, str):
    accumulator = 0
    i = 0
    lines_seen = []
    while True:
        # check if program finished successful
        if i >= len(program):
            return accumulator, "YAY!"

        # check for infinite loop
        if i in lines_seen:
            return accumulator, "loop"

        instruction = program[i]
        lines_seen.append(i)

        if instruction[0] == 'acc':
            accumulator += instruction[1]
            i += 1
        elif instruction[0] == 'jmp':
            i += instruction[1]
        elif instruction[0] == 'nop':
            i += 1
        else:
            raise ValueError


def debugger(program: List[List[Union[str, int]]]) -> int:
    for i, line in enumerate(program):
        debug_copy = deepcopy(program)
        if line[0] == 'jmp':
            debug_copy[i][0] = 'nop'
        elif line[0] == 'nop':
            debug_copy[i][0] = 'jmp'
        accumulator, code = run_program(debug_copy)
        if code == "YAY!":
            return accumulator
    print("Debuging unsucccesfull")


if __name__ == '__main__':
    with open("8.txt") as f:
        inp = f.readlines()

    program = parse_input(inp)
    print("part 1:", run_program(program)[0])
    print("part 2:", debugger(program))
