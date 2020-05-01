## star operator
## args

def total(a, b):
    return a+b
print(total(9, 8))## if you pass more than 2 parametres in this funcitons it will show error

## *args will solove this problems


def all_total(*args):
    return args

print(all_total(1,3,4,5,58))

def all_total1(*args):
    total1 = 0

    for i in args:
        total1 +=i
    return total1
print(all_total1(1, 2, 5, 4, 8))

# one more example for multiply

def multiply_nums(*args):
    multiply = 1

    for i in args:

        multiply*=i
    return multiply

print(multiply_nums(2, 3, 4))



##
def multiply_nums(num,*args):## in this funciton when calling num must be provided
    multiply = 1

    for i in args:

        multiply*=i
        print(num)
        print(args)
    return multiply

print(multiply_nums(2, 3, 5, 5))



### if you are providing a list than * must be used before list in arguments
## same with tuple


def multiply_nums(*args):
    multiply = 1

    for i in args:

        multiply*=i
    return multiply

nums1 = [ 2, 3, 5]

print(multiply_nums(*nums1))

##
def to_power(a, *args):
    if args:
        return [i**a for i in args]
    else:
        return "You didn't pass any args"



print(to_power(2, *[4, 5]))



















