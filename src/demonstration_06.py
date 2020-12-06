"""
Challenge #6:

Return the number (count) of vowels in the given string.

We will consider `a, e, i, o, u as vowels for this challenge (but not y).

The input string will only consist of lower case letters and/or spaces.
"""
def get_count(input_str):
    # Your code here
    # create empty dict to hold the vowel counts
    VOWELS = {}

    # for loop to iterate through the string 
    # tell the dict what letters to look for
    for vowel in 'aeiou':
        count = input_str.count(vowel)
        VOWELS[vowel]= count
    return VOWELS     

print(get_count('How do you do today'))
print(get_count('A plethora of vowels'))