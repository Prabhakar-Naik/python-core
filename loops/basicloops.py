# In python 2 loops they are
# 1. for loop and 2. while loop

for data in range(20):
    print(data," added by 2:",data+2)
    
data = [2,4,6,8,10,12,14,16,18,20]

print("list of data iterate in sequence")
for value in data:
    print(value,end=" ")

print("\n============")
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
print("=============")
while count<len(data):
    print(data[count],end=" ")
    count += 1

print("\n=============")
