# Sets
nums = {1,2,3,4,5}
nums2 = set((1,2,3,4,5))

print(nums)
print(nums2)

print(type(nums))
print(type(nums2))

print(len(nums))

# no duplicates alllowed
nums = {1,2,2,2,3,4,5}
print(nums)

# True ia a dupe of 1, False is dupe of zero
nums = {1, True, 2, 3, False, 4, 0, 5}
print(nums)

# check if a value is in a set
print(2 in nums)

# but we cannot refer to an element in the set with an index position or key
# add a new element to a set
nums.add(8)
print(nums)

# add an elements from one set to another
morenums = {6,7,9}
nums.update(morenums)

print(nums)

# we can use update with list, tuples, and dictionaries, too.

# merge two sets to create a new set
one = {1,2,3}
two = {4,5,6}

mynewSet = one.union(two)
print(mynewSet)

# keep only duplicates
one = {1,2,3}
two = {2,3,6}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)
