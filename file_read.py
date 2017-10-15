# bad way
# file = open('./resources/sample.txt')
# text = file.read()
# for line in text.split('\n'):
#     print(line)
# file.close()

# better way
# file = open('./resources/sample.txt')
# for line in file:
#     print(line)
# file.close()

# good way
with open('./resources/sample.txt') as file:
    for line in file:
        print(line)
