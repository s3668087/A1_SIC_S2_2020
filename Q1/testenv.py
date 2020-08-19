while True:
    person1 = getpass.getpass(prompt="\nPerson 1 Code: ")
    if len(person1) != 5:
        print("You must enter 5 digits!")
    if not person1.isdigit():
        print("Your input must be a number!")
    elif len(person1) == 5:
        break;
