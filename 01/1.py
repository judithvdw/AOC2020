with open("1.txt") as f:
    amounts = f.readlines()

for amount_1 in amounts:
    for amount_2 in amounts:
        for amount_3 in amounts:
            if int(amount_1) + int(amount_2) + int(amount_3) == 2020:
                    print(int(amount_1) * int(amount_2) * int(amount_3))
                    exit(0)


