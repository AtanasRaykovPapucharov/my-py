x_list = [3, 5, 9]
y_list = [7, 11, 33]

# bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)

# good way
for x, y in zip(x_list, y_list):
    print(x, y)
