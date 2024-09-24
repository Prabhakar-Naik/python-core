users = ["prabha","kiran","charan","varun","tharun","milka","singh"]

data = ["prabha",26,True]

emptylist = []

print("prabha" in users)
print("prabha" in data)
print("prabha" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])

print(users.index("varun"))

print(users[0:2])
print(users[1:])

print(users[-3:-1])

print(len(data))
print(len(users))

users.append("Elisa")
print(users)

users += ["Kiran"]
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0,'Bob')
print(users)

users[2:2] = ['Eddie', 'Maddie']
print(users)

users[1:1] = ['Veera', 'JPJ']
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 67, 35, 1, 5, 13]
print(nums)

nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums,reverse=True))

nums.reverse()
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(nums)
print(numscopy)
mycopy.sort(reverse=True)
print(mycopy)
print(mynums)

print(type(nums))

mylist = list([1,"jjjj",89.6])
print(mylist)