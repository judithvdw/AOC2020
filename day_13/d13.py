num = 1009310
busses = [19,37,599,29,17,23,761,41,13]

for bus in busses:
    print(bus, bus - num%bus)

# eyeball lowest
print("part 1:", 5*599)
