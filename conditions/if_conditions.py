num = 10
# simple condition
if (num > 11 and num > 5) or num > 5 :
    print("number is greater than 2")
    
    

    print("JVFKVJ")
else:
    print("else block")
    if num > 5:
        print("greater than 5")
# even condition
if num % 2 == 0:
    print(num,"number is even")

# incremented by 1    
num += 1    #value 11

# odd condition
if num % 2 != 0:
    print(num,"number is odd")

# modification: addition of 2 with existed num 
num +=2
# printing 13
print(num)

# modification: substract of extsted num value addition of 5
num -= num+5
# printing -5
print(num)

# just printing absolute +ve value 
# what ever the value you give it will be in +ve. 
print(abs(num))

# above you not mensioned assignment BCS of that it will not reflect
print(num)

# now assigning functionality
num = abs(num)

print(num)

# prime number sample code
x = 7
count = 0
for i in range(2,x):
    if x % i != 0:
        count +=1
        
if(count > 0):
    print(x,"Prime number")
else:
    print(x,"Not Prime")



