def clean_key(k: str) -> str:
    return " ".join(k.split()[:2])


def clean_value(v: str) -> dict:
    if "no other bags" in v:
        return {}
    v_dict = {}
    v = v.strip().strip(".")
    for bag in v.split(","):
        bag = bag.split()
        color = " ".join(bag[1:3])
        n = bag[0]
        v_dict[color] = int(n)
    return v_dict


def parse_input(rules: list) -> dict:
    d = {}
    for rule in rules:
        rule = rule.split("contain")
        d[clean_key(rule[0])] = clean_value(rule[1])
    return d


def has_gold_bag(bag_rule: dict) -> bool:
    gold = False
    if bag_rule.get("shiny gold"):
        return True
    for k, v in bag_rule.items():
        gold = has_gold_bag(bag_rules[k]) or gold
    return gold


def n_of_bags(bag_rules: dict, bag: str, depth: int = 0) -> int:
    total_bags = 1
    for colour, n in bag_rules[bag].items():
        total_bags += n * n_of_bags(bag_rules, colour, depth + 1)
    return total_bags


def part_1(bag_rules: dict) -> int:
    count = 0
    for k, v in bag_rules.items():
        if has_gold_bag(v):
            count += 1
    return count


if __name__ == '__main__':
    with open("7.txt") as f:
        bag_rules = parse_input(f.readlines())

print("part 1:", part_1(bag_rules))
print("part 2:", n_of_bags(bag_rules, "shiny gold") - 1)
