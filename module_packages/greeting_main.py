from my_package import geet, greet1
import greeting
import utils
import datetime


print("Birth day wish: ")
result = greeting.birth_day_wish("prabhakar")
print(result)
print()

print("Marriage Wish: ")
result = greeting.marriage_wish("Jhon","Lila")
print(result)
print()

print("Invitation: ")
result = greeting.invitation_wish(datetime.datetime.now().date())
print(result)
print()

print("Helloo!")
print("Below are util functions:")

result = utils.addition(10,20)
print("addition:",result)

result = utils.substract(10,3)
print("substract:",result)

result = utils.multiply(3,3)
print("multiply: ",result)

result = utils.square_my(2,3)
print("square: ",result)

result = utils.division(12,4)
print("division:",result)

result = utils.dividion_accurate(12,4)
print("division accurate:",result)

result = utils.remainder(13,3)
print("remainder:",result)

print("this id from packages")
geet.hi()

greet1.hello()
