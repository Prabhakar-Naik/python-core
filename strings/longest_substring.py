"""
Longest Substring Without Repeating Characters
Given a string s, return the length of the longest substring without repeating characters.

O(n) optimization instead of O(n²)

Input: "abcabcbb"
Output: 3
Explanation: "abc"
Input: "bbbbb"
Output: 1
Explanation: "b"

Input: "pwwkew"
Output: 3
Explanation: "wke"
"""

def length_of_longest_substring(s):
    left = 0
    max_length = 0
    char_index = {}

    for right in range(len(s)):
        current_char = s[right]

        if current_char in char_index and char_index[current_char] >= left:
            left = char_index[current_char] + 1

        char_index[current_char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


print(length_of_longest_substring("abcabcbb"))  # 3
print(length_of_longest_substring("bbbbb"))     # 1
print(length_of_longest_substring("pwwkew"))    # 3
print(length_of_longest_substring(""))          # 0
