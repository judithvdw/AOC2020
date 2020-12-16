def parse_ticket_info(ticket_info):
    info = {}
    for line in ticket_info.split('\n'):
        name, conditions = line.split(': ')
        condition_a, condition_b = conditions.split(" or ")
        min_a, max_a = condition_a.split("-")
        min_b, max_b = condition_b.split("-")
        info[name] = (int(min_a), int(max_a), int(min_b), int(max_b))
    return info

def parse_other_tickets(other_tickets):
    minimum = 27 # yes, I looked at the input
    maximum = 974
    # minimum = 0
    # maximum = 19
    tickets = []
    for ticket in other_tickets.split('\n')[1:]:
        new_ticket = [int(i) for i in ticket.split(',')]
        if min(new_ticket) >= minimum and max(new_ticket) <= maximum:
            tickets.append(new_ticket)
    return tickets


def parse_input(blob):
    ticket_info, my_ticket, other_tickets = blob.split("\n\n")
    ticket_info = parse_ticket_info(ticket_info)
    my_ticket = [int(i) for i in my_ticket.split('\n')[1].split(',')]
    other_tickets = parse_other_tickets(other_tickets)
    return my_ticket, other_tickets, ticket_info


def possible(collumn,  values):
    for cell in collumn:
        if (values[0] <= cell <= values[1]) or (values[2] <= cell <= values[3]):
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    with open('16.txt') as f:
        blob = f.read()


my_ticket, other_tickets, ticket_info = parse_input(blob)
entries_per_field = [list(i) for i in zip(*other_tickets)]

overview = {}
for field, values in ticket_info.items():
    possible_colls = []
    for i, collumn in enumerate(entries_per_field):
        if possible(collumn, values):
            possible_colls.append(i)
    overview[field] = possible_colls


for i, tick in enumerate(my_ticket):
    print(tick, i)

# for k in sorted(overview, key=lambda k: len(overview[k]), reverse=True):
#     print(k, overview[k])

'''
With some magic hand work: 
departure platform [ 8]
departure track [ 7]
departure time [0]
departure station [ 3]
departure location [1]
departure date [14]
'''

total = 1
departures = [8,7,0,3,1,14]
for i, tick in enumerate(my_ticket):
    if i in departures:
        total *= tick
print(total)


