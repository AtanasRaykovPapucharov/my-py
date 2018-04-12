def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)

test_var_args('yasoob','python','eggs','test')

print("-------------------------")

def sum(*args):
    result = 0
    for a in args:
        result += a
    return result

print("-------------------------")

def multiply(*args):
    result = 1
    for a in args:
        result *= a
    return result

print("-------------------------")

print(sum(3, 5, 6, 9))

print(multiply(3, 9))