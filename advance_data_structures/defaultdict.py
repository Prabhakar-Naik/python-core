from collections import defaultdict

# Basic usage
dd = defaultdict(int)
dd['a'] += 1
print(dd['a'])  # Output: 1
print(dd['b'])  # Output: 0 (default int value)

# advance level

def group_by_category(pairs):
    grouped = defaultdict(list)
    for key, value in pairs:
        grouped[key].append(value)
    return dict(grouped)

pairs = [('fruit', 'apple'), ('fruit', 'banana'), ('vegetable', 'carrot')]
print(group_by_category(pairs))  # Output: {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']}
