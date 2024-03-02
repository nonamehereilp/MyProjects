import random
import math

simple_letters = 'abcdefghijklmnopqrstuvwxyz'
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
symbles = '!@#$%^&*()_+'

def shuffle_password(password):
    # Convert the password to a list of characters
    password_list = list(password)

    # Use Fisher-Yates shuffle algorithm
    for i in range(len(password_list) - 1, 0, -1):
        j = random.randint(0, i)
        password_list[i], password_list[j] = password_list[j], password_list[i]

    # Convert the shuffled list back to a string
    shuffled_password = ''.join(password_list)

    return shuffled_password


def main(min_len=14 , max_len=18):
    print('--------======--------')
    #take random length between 12-18
    password_length = random.randint(min_len, max_len)
    print('Password length       : ' , password_length)
    
    #select amount from each catogory
    #letters
    letters_amount = math.ceil(password_length/2)
    print('letters amount        : ' , letters_amount)

    simple_letters_amount = math.ceil((letters_amount/100)*(random.randint(55, 70))) #simple letters amout
    print('simple letters amount : ' , simple_letters_amount)
    capital_letters_amount = letters_amount-simple_letters_amount #capital letters amout
    print('capital letters amount: ', capital_letters_amount)
    
    print()
    
    #numbers and symbles
    numbers_symbles_amout = password_length-letters_amount
    print('numbers and symbles  : ', numbers_symbles_amout)
    numbers_amount = math.ceil(numbers_symbles_amout/2)
    print('numbers amount       : ', numbers_amount)
    symbles_amount = numbers_symbles_amout-numbers_amount
    print('symbles amount       : ' , symbles_amount)
    
    print()
    
    #selecting letters
    selected_simple_letters = ''
    for i in range(0 ,simple_letters_amount):
        selected_simple_letters += simple_letters[(random.randint(1, len(simple_letters)))-1]
    print('selected simple letters  : ' , selected_simple_letters)
    selected_capital_letters = ''
    for i in range(0 ,capital_letters_amount):
        selected_capital_letters += capital_letters[(random.randint(1, len(capital_letters)))-1]
    print('selected capital letters : ' ,selected_capital_letters)    
    selected_numbers = ''
    for i in range(0 , numbers_amount):
        selected_numbers += numbers[(random.randint(1, len(numbers)))-1]
    print('selected numbers         : ' ,selected_numbers)
    selected_symbles = ''
    for i in range(0 , symbles_amount):
        selected_symbles += symbles[(random.randint(1, len(symbles)))-1]
    print('selected symbles         : ' ,selected_symbles)
    
    print()
    #unshuffled password
    unshuffled_password = selected_simple_letters+selected_capital_letters+selected_numbers+selected_symbles
    print('unshuffled password : ' , unshuffled_password)
    print()
    #shuffle
    password = shuffle_password(unshuffled_password)
    print('Generated password  : ' , password)
    
    print()
    return password

main(min_len=14 , max_len=18)

#      :)

# if __name__ == "__main__":
#     passwords = []
#     i = 0
#     while True:    
#         print(i)
#         i+=1
#         password = main(min_len=14, max_len=18)

#         if password in passwords:
#             print('Rare Rare Rare')
#             print('The Same password Generated again' , password)
#             break
#         passwords.append(password)
#         with open('passwords.txt','a') as file:
#             file.write(password+'\n')