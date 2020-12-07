"""
Challenge #7:

Given a string of lowercase and uppercase alpha characters, write a function
that returns a string where each character repeats in an increasing pattern,
starting at 1. Each character repetition starts with a capital letter and the
rest of the repeated characters are lowercase. Each repetition segment is
separated by a `-` character.

Examples:
- repeat_it("abcd") -> "A-Bb-Ccc-Dddd"
- repeat_it("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
- repeat_it("cwAt") -> "C-Ww-Aaa-Tttt"
"""
def repeat_it(input_str):
    # Your code here
    # empty list for results
    results = []
    # for loop to get each char
    # +1 to increment
    for char in input_str:
        new_inp = input_str.find(char) + 1
        # get each ind'l character
        for i in char:
            # multiply each char by it's increment from 1st loop
            results.append(i * new_inp)
    # join with - char & capitalize first letter
    result = '-'.join(str(ele).capitalize() for ele in results)    
    return result

        
print(repeat_it("abcd"))