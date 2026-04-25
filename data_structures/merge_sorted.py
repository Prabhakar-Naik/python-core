"""
Merge two sorted lists into one sorted list without using built-in sort functions.
Input: [1, 3, 5], [2, 4, 6]
Output:[1, 2, 3, 4, 5, 6]

Approach: Use two pointers to compare elements from both lists and merge them in sorted order.
"""

def merge_sorted_lists(a, b):
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

# Example
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
# Output: [1, 2, 3, 4, 5, 6]
