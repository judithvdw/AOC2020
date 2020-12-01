def get_answer_1(amounts) -> int:
    for amount_1 in amounts:
        for amount_2 in amounts:
            if amount_1 + amount_2 == 2020:
                return amount_1 * amount_2


def get_answer_2(amounts) -> int:
    for amount_1 in amounts:
        for amount_2 in amounts:
            for amount_3 in amounts:
                if amount_1 + amount_2 + amount_3 == 2020:
                    return amount_1 * amount_2 * amount_3


if __name__ == '__main__':
    with open("1.txt") as f:
        amounts = f.readlines()
        amounts = [int(x) for x in amounts]

    print("part 1: ", get_answer_1(amounts))
    print("part 2: ", get_answer_2(amounts))
