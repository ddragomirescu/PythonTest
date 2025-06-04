import random   
import string # usefull module contains constans like ascii_letters 

print(" --- Welcome to Random Password Generator V1 ---")
special_check = False 
pass_length = int(input("Please enter the Password Length:"))
password = "qwe123QWE!@#" # default answer
retry = 0

def special_Characters(counter):
    if counter > 3:
        print("Error: Invalid input")
        return None # Should I exit program ?? 
    answer = input("Do you want to add special characters to the password (y\n)? or leave blank for no ")
    if(answer == 'y' or answer == 'Y'):
        return True 
    elif(answer == 'n' or answer == 'N'):
        return None
    elif(len(answer) != 0):
        print("Sorry, didn't get that, please try again")
        counter += 1
        special_Characters(counter)


# char_list = ["a" ,"b" ,"c" ,"d" ,"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
char_list = list(string.ascii_letters)

num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_list = ["!", "@", "#", "$", "%", "&", "?"]

special_check = special_Characters(retry)

def pass_Generator(special_check, pass_length):
    password = []
    # index = 0

    if special_check:
        pass_length += -1 
        password.append(special_list[random.randrange(len(special_list) - 1)])
    
    n_letters = random.randrange(pass_length//2, pass_length)                # Have at least 1/2 of characters 
    n_number = pass_length - n_letters
    
    # for index in range(n_letters - 1):
    #    password.append(char_list[random.randrange(len(char_list) - 1)])
    
    for _ in range(n_letters):
        password.append(random.choice(char_list))
        
    for index in range(n_number - 1):
        password.insert(random.randrange(pass_length - 1), num_list[random.randrange(len(num_list) - 1)])
        12
    for index in range(2):
        password.insert(random.randrange(pass_length - 1), char_list[random.randrange(len(char_list) - 1)].upper)
        
    return password

print("Here is your password:", ''.join(pass_Generator(special_check, pass_length)))





