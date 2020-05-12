def swap_indices(swap, ind1, ind2):
    temp = swap[ind1]
    swap[ind1] = swap[ind2]
    swap[ind2] = temp
    print(swap)


def moveZeroes(list_nums):
    iterator = 0
    zero_counter = 0
    for i in range(len(list_nums)):
        if list_nums[i] == 0:  # is element 0, and not first elem
            zero_counter += 1  # increase counter
        elif zero_counter != 0:  # else, it is non zero AND not first elem
            temp = list_nums[i]  # number at current index
            list_nums[(i - zero_counter)] = temp  # move zero_counter steps back and set that to number at indx
            list_nums[i] = 0

    print(list_nums)


listOfNums = [3, 0, 9, 1, 0, 2]
listOfNums1 = [0, 0, 0, 1, 2, 3]
listOfNums2 = [1, 0, 2, 0, 3, 0]

# swap_indices(listOfNums, 0, 1)
# swap_indices(listOfNums, 0, 1)
moveZeroes(listOfNums)
moveZeroes(listOfNums1)
moveZeroes(listOfNums2)
"""
to_swap = [0, 1, 2, 5] 0    
        = [1, 0, 2, 5] 1
        = [1, 2, 0, 5] 2
        = [1, 2, 5, 0] 3

to_swap = [0, 1, 0, 2, 5] 
        = [1, 0, 0, 2, 5]
        = [1, 0, 0, 2, 5]

to_swap = [1, 0, 2, 0, 3, 0, 4, 0]

        = [1, 2, 2, 0, 3, 0, 4, 0]
        = [1, 2, 0, 0, 3, 0, 4, 0]
        = [1, 2, 0, 0, 3, 0, 4, 0]
        = [1, 2, 3, 0, 3, 0, 4, 0]
        = [1, 2, 3, 0, 0, 0, 4, 0]
        = [1, 2, 3, 0, 0, 0, 4, 0]
        = [1, 2, 3, 4, 0, 0, 4, 0]
        = [1, 2, 3, 4, 0, 0, 0, 0]

        = [1, 2, 3, 4, 0, 0, 0, 0]

between index of first 0, and index of non-zero
    of # of 0s 

to_swap = [0, 0, 0, 0, 1, 2, 3, 4]

        = [0, 0, 0, 0, 1, 2, 3, 4]
        = [1, 0, 0, 0, 1, 2, 3, 4]
        = [1, 0, 0, 0, 0, 2, 3, 4]
        = [1, 2, 0, 0, 0, 2, 3, 4]
        = [1, 2, 0, 0, 0, 0, 3, 4]
        = [1, 2, 0, 0, 0, 0, 3, 4]
        = [1, 2, 3, 0, 0, 0, 3, 4]
        = [1, 2, 3, 0, 0, 0, 0, 4]
        = [1, 2, 3, 4, 0, 0, 0, 4]

        = [1, 2, 3, 4, 0, 0, 0, 0]
"""
