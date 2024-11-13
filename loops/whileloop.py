# simple basic loop
print("first way")
i = 0
while i<=10:
    print(i)
    i += 1


print("second way")
i = 0
while i < 10:
    print(1+i)
    i += 1
    

print("third way")
i = 1
while i <= 10:
    print(i)
    i +=1
 
    
print("even 1 ")
i=0
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1


print("Even 2")
i = 2
while i <= 10:
    print(i)
    i += 2
   
 
print("odd 1")
i=0
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1
    

print("odd 2")
i = 1
while i <= 10:
    print(i)
    i += 2

print(" while loop demo")
value = 0
while value <=10:
    value += 1
    if value == 5:
        continue
    print(value)
else:
    print("Value is now equals to ",value)

