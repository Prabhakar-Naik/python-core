# Tuples

mytuple = tuple(('prabha',24,True))

anothertuple = (1,2,3,4,2,5,2,6,2)

print(mytuple)
print(anothertuple)

print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('subject')
newtuple = tuple(newlist)
print(newtuple)

(one,*two,hey) = anothertuple

print(one)
print(two)
print(hey)

print(anothertuple.count(2))
