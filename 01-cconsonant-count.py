'''
Write a function that given a string, counts total number of consonants in it. 
A consonant is a English alphabet character that is not vowel (a, e, i, o and u). 
Examples of constants are b, c, d, f, g, ..
input will never have spaces or non letter characters

Examples: 

Input: 'snakes'
Output: 4

Input: 'SpamAndEggs'
Output: 8
'''

# def const_count_str(str):
#     vowels = 'aeiou'
#     constants = []
#     if str.__contains__(vowels):
#         return False
    
#     if str:



# print('snakes'[0])


def consonant_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    # base case
    if len(string) == 0:
        return 0
    # recursive case
    else:
        if string[0].lower() not in vowels:
            return 1 + consonant_count(string[1:])
        else:
            return consonant_count(string[1:])
# test
print(consonant_count('SpamAndEggs'))