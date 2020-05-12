"""
1. start dictionary
2a. start loop
 b. inside loop, iterate through array of ints
 c. with each int, store in dictionary
 d. when pair is found, remove existing int in dictionary
3. return remaining int from dictionary



4,1,2,1,9,2,4

dictionary: 4
                <empty>
loop            dict
4               4
1               4->1,  1->1
2               4->1, 1->1, 2->1
1               4->, 2->1
9
"""

from collections import defaultdict


def singleNumber(list_of_nums):
    num_dictionary = {}
    for nums in list_of_nums:
        key = nums
        if key in num_dictionary:
            del num_dictionary[key]
        else:
            num_dictionary[key] = 1
    return num_dictionary.popitem()[0]

    #return num_dictionary


num_list = [8, 1, 2, 1, 5, 2, 8]
print(singleNumber(num_list))