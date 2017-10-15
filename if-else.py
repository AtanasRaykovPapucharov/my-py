latest_version = 3
my_version = 3

# bad way
# if latest_version > my_version:
#     print('Update available!')
# else:
#     print('Up to date!')

# good way
print('Update available!' if latest_version > my_version else 'Up to date!')