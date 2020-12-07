"""
Challenge #9:

Given a string, write a function that returns the "middle" character of the
word.

If the word has an odd length, return the single middle character. If the word
has an even length, return the middle two characters.

Examples:
- get_middle("test") -> "es"
- get_middle("testing") -> "t"
- get_middle("middle") -> "dd"
- get_middle("A") -> "A"
"""
def get_middle(input_str):
    # Your code here
    if len(input_str) == 1:
        return input_str


print(get_middle("testing"))
print(get_middle("A"))

# edge cases: if str == 1: rtn str
# split the word in 2. return the last letter from the 1st half
# and 1stletter from the 2nd half
# pseudocode: mid = input_str // 2