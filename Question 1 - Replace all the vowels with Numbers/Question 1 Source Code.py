# *********************************************** QUESTION 1 ***********************************************************
"""
Question:
Replace all the vowels of the given input string with a single digit number.
Input:
String of length L and all lower-case letters.
Output:
Input String replaced with the digit.
"""


# ************************************************ FUNCTIONS ***********************************************************
def prime_sum(n):
    """Function to return the sum of prime numbers upto the given number(n-th number). """

    def prime_checker(number):
        """Function to check if the given number is a prime or not and return the result."""
        is_prime = True  # starting by assuming all numbers given is a prime number.
        for num in range(2, number):
            """Checking if the number is divisible by any numbers between 1 and the number and set is_prime to false
            if divisible by any"""
            if number % num == 0:
                is_prime = False
        if is_prime:  # if the given number is prime return true.
            return True

    prime_num = []  # creating a empty list.

    for j in range(2, n):
        """for every numbers n Check every prime numbers and append it to the list"""
        if prime_checker(j):
            prime_num.append(j)

    return sum(prime_num)  # returning the sum of the elements in the list.


# ********************************************** CONSTANT **************************************************************
VOWELS = ('a', 'e', 'i', 'o', 'u')  # tuple of vowels

# ************************************************* MAIN ***************************************************************

change_num = 0
input_string = input().lower()

for i in range(len(input_string)):  # getting hold of index of every letters in the input string.
    if input_string[i] in VOWELS:  # checking if letters of input string is a VOWEL
        ix100 = i*100  # multiplying index of VOWEL with 100
        sum_of_prime = prime_sum(ix100)  # getting sum of prime numbers up to the index X 100
        while sum_of_prime > 10:
            """Summing every digit of sum of prime numbers continuously until it become a single digit. """
            change_num = 0
            sum_in_str = str(sum_of_prime)
            for numb in sum_in_str:
                change_num += int(numb)
            sum_of_prime = change_num
        # replacing the input sting letter which is a VOWEL with the result number
        input_string = input_string.replace(input_string[i], str(change_num))

# printing the final output
print(input_string)
# **********************************************************************************************************************
