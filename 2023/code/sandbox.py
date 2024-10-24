hand = 'AA'

num_jokers = sum([1 if c == "J" else 0 for c in hand ])

print(num_jokers)