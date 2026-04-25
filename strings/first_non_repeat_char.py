"""
Given a string, return the first character that does not repeat.
 If all characters repeat, return None.
 "abcabcde" -> "d"
 Approach: Use a dictionary to count occurrences,
then iterate through the string again to find the first unique character.
"swiss" -> w
"hello" -> h
"aabbcc" -> None
"""

from collections import Counter

def first_non_repeat_char(s):
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None
print(first_non_repeat_char("swiss")) # w
print(first_non_repeat_char("aabbcc")) # None
print(first_non_repeat_char("hello")) # h
print(first_non_repeat_char("abcabcde")) # d
