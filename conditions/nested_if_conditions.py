# To achieve nested conditions

data = -20

if(data > 0):
    print("+ve")
    if data % 2 == 0:
        print(data,"Even")
    elif data % 2 != 0:
        print(data,"Odd")
elif(data == 0):
    print("Zero")
    data += data+6
    if(data > 0):
        print("+ve number",data) 
else:
    print("-ve",data)