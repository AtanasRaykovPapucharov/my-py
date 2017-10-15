needle = 'd'
haystack = ['a', 'b', 'c']

# bad way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not found!')

# good way
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else: # If no break occurred
    print('Not found!')
