import random
import math

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

def generate_password():
    # pass_len=random.randint(8,13)  #without User INput
    length = int(input("Enter Password Length :"))

    # length of password by 50-30-20 formula
    alpha_len = length//2
    num_len = math.ceil(length*30/100)
    special_len = length-(alpha_len+num_len)


    password = []


    def generate_pass(input_length, array, is_alpha=False):
        for i in range(input_length):
            index = random.randint(0, len(array) - 1)
            character = array[index]
            if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()
            password.append(character)


    # alphabetical password
    generate_pass(alpha_len, alpha, True)

    # numerical password
    generate_pass(num_len, num)

    # special Character password
    generate_pass(special_len, special)

    # suffle the generated password list
    random.shuffle(password)

    # convert List To string
    gen_password = ""
    for i in password:
        gen_password = gen_password + str(i)
        
    print(gen_password)
    
if __name__ == '__main__':
    generate_password()