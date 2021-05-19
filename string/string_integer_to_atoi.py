# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.

# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. 
# Assume the result is positive if neither is present.

# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.

# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:

# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
s = "   -42"
def atoi(s): 

    res = ''
    i = 0

    # loop through given string 
    while i <= len(s)-1:

        # ignore whitespace
        while s[i] == ' ':
            i += 1
             
        # if char is '-' or '+' write '-' it down to res
        if s[i] == '-' or s[i] == '+' and i < len(s) -1: 
            res += s[i] 
            i += 1 
        while s[i].isalpha() == True and i < len(s) -1 : 
            i += 1 
        
        while s[i].isalnum() == True and i < len(s) -1  : 
            res += s[i] 
            i += 1 
            if i == (len(s) -1) and s[i].isalnum() == True: 
                res += s[i]
        i += 1
        print(res)
        if res == '' or '-': 
            return 0 
        # Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32) 
        # check if If the integer is out of the 32-bit signed integer range [-231, 231 - 1]
        if int(res) > -2147483648:
            return int(res)
        if int(res) < 2147483647:
            return -2147483648
        else:
            return int(res)

    # Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32) 
    # check if If the integer is out of the 32-bit signed integer range [-231, 231 - 1] 
    
print(atoi(s))
print(atoi("4193 with words"))
print(atoi("-91283472332"))
print(atoi("words and 987"))
print(atoi("-+12"))