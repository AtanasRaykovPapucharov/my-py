x = '1'

# bad way
# print('Converting...')
# try:
#     print(int(x))
# except:
#     print('Convertion failed!')
# print('Done!')

# good way
print('Converting...')
try:
    print(int(x))
except:
    print('Error: Convertion failed!')
else:
    print('Convertion successful!')
finally: # Always
    print('Done!')
