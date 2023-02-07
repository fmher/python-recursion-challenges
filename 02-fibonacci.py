'''
The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.

Read more about it:

https://www.mathsisfun.com/numbers/fibonacci-sequence.html

Write a recursive function called fib that accepts a number N greater than zero and returns the Nth fibonacci number

Examples:

input: 10
output: 55

input: 3
output: 2

input: 30
output: 832040
'''

def fib(n):
    # base case
    if n < 2:
        return n
    # recursive case
    else:
        return fib(n-1) + fib(n-2)
# test
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(10))