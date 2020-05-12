"""
21
2^2 + 1 ^2 = 5
5^2 = 25
2^2 + 5^2 = 29
2^2 + 9^2 = 85
8^2 + 5^2 = 89
8^2 + 9^2 = 145
1^2 + 4^2 + 5^2 = 42
4^2 + 2^2 = 20
2^2 + 0^2 = 4

29
2 r 9
9 r 0

145
14
 r 5
10
100
1000

if it's 1 digit


"""


def num_convert(num):
    return [int(d) for d in str(num)]


def square_sum(num):
    split_digits = [int(d) for d in str(num)]
    sum_digits = 0
    for digit in split_digits:
        sum_digits += (digit ** 2)

    return sum_digits


def isHappy(n):
    past_numbers = []
    while n != 1:
        past_numbers.append(n)
        n = square_sum(n)
        if n in past_numbers:
            return False
    return True


"""
take in a number
do the square and add it
add that number to the list
"""
print(isHappy(19))


def happyNumber(num) -> bool:
    print(num)
    if num == 1:
        return True

    if num in storage:
        return False
    storage.append(num)
    split_digits = [int(d) for d in str(num)]

    sum_digits = 0
    for digit in split_digits:
        sum_digits += (digit ** 2)

    return happyNumber(sum_digits)


"""

happynumber                 sum_digit
19                              82        
    82                              68
        68                            100
            1


[1, 9]

if empty, do work
if not empty
    if number found return false
    if number NOT found do work

"""
storage = [3, 9]

# print(num_convert(53))

# print(happyNumber(18))

# print(square_sum(storage))
