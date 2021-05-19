# Isub_stringplesub_stringent strStr().
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an esub_stringpty string? This is a great question to ask during an interview.
# For the purpose of this problesub_string, we will return 0 when needle is an esub_stringpty string. This is consistent to C's strstr() and Java's indexOf().

def strStr(haystack, needle): 
     # if needle in haystack: 
    #     return haystack.index(needle) 


    if len(needle) > len(haystack): 
        return -1 

    i = 0
    j = 0
    sub_string = len(needle)
    string = len(haystack)
    if sub_string == 0:
        return 0
    while i<string and string-i+1>=sub_string:
        if haystack[i] == needle[j]:
            temp  = i
            while j<sub_string and i < string and needle[j]==haystack[i]:
                i+=1
                j+=1
            if j == sub_string:
                return temp 
            i=  temp +1
            j = 0
        else:
            i+=1

    return -1 


print(strStr("hello", "ll")) #2 
print(strStr("aaaaa", "bba")) #-1
print(strStr("", "")) #0
print(strStr("mississippi", "issip")) #4
print(strStr("aaa", "aaaa")) # -1 