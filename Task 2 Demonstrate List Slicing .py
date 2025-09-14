'''Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list'''
numbers = list(range(1, 11))

ff = numbers[:5]

rff = ff[::-1]
print("Original list of numbers :",numbers)
print("Extracted First five elements:", ff)
print("Reversed Extracted first five elements:", rff)
