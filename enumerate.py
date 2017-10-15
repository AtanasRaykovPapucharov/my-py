cities = ['Sofia', 'New York', 'Paris', 'London', 'LA']

# bad way
i = 0
for city in cities:
    print(i, city)
    i += 1

# good way
for i, city in enumerate(cities):
    print(i, city)
