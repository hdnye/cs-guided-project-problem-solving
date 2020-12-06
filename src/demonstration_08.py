"""
Challenge #8:

Given an integer, write a function that returns "Even" for even integers and
"Odd" for odd integers.

Examples:
- parity(0) -> "Even"
- parity(1) -> "Odd"
- parity(2) -> "Even"
"""
def parity(input_int):
    # Your code here
    for x in range(input_int): 
        if x % 2 == 0:
            return 'Even'
        else: 
            return 'Odd'
   
print(parity(0))
print(parity(1))