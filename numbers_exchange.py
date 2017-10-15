x = 20
y = -20

print('Before: x = %d, y = %d' % (x, y))

# bad way
# temp = x
# x = y
# y = temp
# print('After: x = %d, y = %d' % (x, y))

# good way
x, y = y, x
print('After: x = %d, y = %d' % (x, y))
