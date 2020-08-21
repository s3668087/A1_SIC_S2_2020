from num2words import num2words
import getpass

person1 = "11111"
person2 = "22222"
person3 = "33333"

#Inputs from each person
while True:
    #person1 = getpass.getpass(prompt="\nPerson 1 Code: ")
    if len(person1) != 5:
        print("You must enter 5 digits!")
    if not person1.isdigit():
        print("Your input must be a number!")
    elif len(person1) == 5:
        break;

while True:
    #person2 = getpass.getpass(prompt="\nPerson 2 Code: ")
    if len(person2) != 5:
        print("You must enter 5 digits!")
    if not person2.isdigit():
        print("Your input must be a number!")
    elif len(person2) == 5:
        break;

while True:
    #person3 = getpass.getpass(prompt="\nPerson 3 Code: ")
    if len(person3) != 5:
        print("You must enter 5 digits!")
    if not person3.isdigit():
        print("Your input must be a number!")
    elif len(person3) == 5:
        break;

#Concatinates each persons code
code = person1 + person2 + person3

#Converts the concatinated integer into a string that is human readable (eg. 1000 = one thousand)
code = num2words(code)

#Shift by n
s = 4

def encrypt(code,s): 
    result = ""
  
    for i in range(len(code)): 
        char = code[i] 
  
        if (char.isupper()): 
            result += chr((ord(char) + s-65) % 26 + 65) 
  
        else: 
            result += chr((ord(char) + s - 97) % 26 + 97) 
  
    return result 



#Debugging
print ("\nText  : " + code)
print ("\nShift : " + str(s))
print ("\nCipher: " + encrypt(code,s))

#Write to a file
#file1 = open("myfile.txt","w") 
#file1.writelines(encrypt(code,s)) 
#file1.close()

#Removing unused variables and their data
del person1, person2, person3
del code
print ("\nKeyPad Data Cleared")
