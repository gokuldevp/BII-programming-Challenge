# ************************************************* QUESTION ***********************************************************
"""
Question:

Given a lowercase alphabet string s, find the minimum number of swaps required to make it a
symmetry string. If it's not possible, then return -1.
"""


# ************************************************** FUNCTION **********************************************************
def min_swaps(string):
    """Function to count the number of swaps"""
    str = list(string)  # converting the input string into a list.
    count = 0  # setting initial number of count to 0
    left = 0  # setting initial index of letter to be check to be 0 in left side
    right = len(str)-1  # setting initial index of letter to be check to be length of string - 1 on right side
    is_center_found = False  # setting is center found to be False
    while left < right:  # while index of left is greater than right
        search = right  # setting search as right
        while str[search] != str[left]:  # looping until the string in both side are same.
            search -= 1  # finding the index of the common string.
        if search == left:  # checking if index of same letter is equal to index of right
            if is_center_found and str[search].islower():  # If center is found is already found and search string is lower case
                return -1  # returning -1 since the word can't be swap to get symmetric
            else:
                is_center_found = True  # else set is string found as True
                middle_index = len(str)//2  # finding the middle index
                while search != middle_index:  # checking if the center letter is placed in the middle of the word.
                    str[search], str[search + 1] = str[search + 1], str[search]  # Swapping it until it is in middle
                    count += 1  # counting swap
                    search += 1
                str[middle_index] = str[middle_index].upper()  # making the middle letter upper case so that we don't check it again
        else:
            while search != right:  # is the same number is not in the index of right
                str[search], str[search+1] = str[search+1], str[search]  # Swap it until it is in right index
                count += 1  # counting swap
                search += 1
            left += 1  # changing the left and right to other index
            right -= 1
    return count  # returning count


# **************************************************** MAIN ********************************************************** #
input_string = input()
from_left = min_swaps(input_string)  # finding count from left
from_right = min_swaps(input_string[::-1])  # finding count from right
print(min(from_left, from_right))  # printing the minimum count
# ******************************************************************************************************************** #
