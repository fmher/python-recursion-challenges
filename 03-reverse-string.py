'''
Write a recursive function called reverse that accepts a string and returns a reversed string.

Examples:

input: "computer"
output: "retupmoc"

input: "ab"
output: "ba"

input: "abcdefghijklmnopqrstuvwxyz"
output: "zyxwvutsrqponmlkjihgfedcba"
'''

def reverse(str):
    if len(str) == 0:
        return str
    else:
        return str[-1] + reverse(str[:-1])


print(reverse("ab"))


# Write a recursive function called reverse that accepts a string and returns a reversed string.
# def reverse(string):
#     # base case
#     if len(string) == 0:
#         return string
#     # recursive case
#     else:
#         return string[-1] + reverse(string[:-1])
# # test
# print(reverse("abcdefghijklmnopqrstuvwxyz"))