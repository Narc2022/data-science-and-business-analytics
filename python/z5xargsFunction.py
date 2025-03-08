# lists [2,3,4,5]
# tuples (2,3,4,5)


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)

# output => (2, 3, 4, 5)


# Iterate above tuple
def iterateXArgs(*numbers):
    for number in numbers:
        print(number)


iterateXArgs(2, 3, 4, 5)
