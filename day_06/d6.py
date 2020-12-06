def somebody_yes(form_groups):
    totals = []
    for form_group in form_groups:
        unique_answers = set()
        for form in form_group:
            unique_answers.update(list(form))
        totals.append(len(unique_answers))
    return totals


def all_yes(form_groups):
    totals = []
    for form_group in form_groups:
        letter_forms = [set(list(form)) for form in form_group]
        yes = set.intersection(*letter_forms)
        totals.append(len(yes))
    return totals


def parse_input(blob: str):
    return [passport.strip().split() for passport in blob.split("\n\n")]


if __name__ == '__main__':
    with open('6.txt') as f:
        forms = parse_input(f.read())

    print("part 1", sum(somebody_yes(forms)))
    print("part 2", sum(all_yes(forms)))
