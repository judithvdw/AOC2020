def somebody_yes(forms):
    unique_answers = set()
    for form in forms:
        unique_answers.update(list(form))
    return len(unique_answers)

def all_yes(forms):
    letter_forms = [set(list(form)) for form in forms]
    yes = set.intersection(*letter_forms)
    return len(yes)


def parse_input(blob: str):
    form_groups = [passport.strip().split() for passport in blob.split("\n\n")]
    totals = []
    print(form_groups)
    for form_group in form_groups:
        totals.append(all_yes(form_group))
    return totals


if __name__ == '__main__':
    with open('6.txt') as f:
        blob = f.read()

    #print("part 1", sum(parse_input(blob)))
    print("part 2", sum(parse_input(blob)))