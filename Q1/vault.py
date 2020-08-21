#User input
person1 = input("Person 1! Enter a single digit code: ")
person2 = input("Person 2! Enter a single digit code: ")
person3 = input("Person 3! Enter a single digit code: ")

#Convert into binary and remove unwanted characters
person1 = (bin(person1).replace("0b","").zfill(20))
person2 = (bin(person2).replace("0b","").zfill(20))
person3 = (bin(person3).replace("0b","").zfill(20))

print "\nBinary"
print "Person 1 " + person1
print "Person 2 " + person2
print "Person 3 " + person3 + "\n"

#XOR person1 and person2 into masterkey1 variable
masterkey1 = int(person1,2) ^ int(person2,2)
print "XOR person1 and person2 into masterkey1 variable " + ('{0:b}'.format(masterkey1).zfill(20))

#XOR person2 and masterkey1 into key variable
masterkey2 = int('{0:b}'.format(masterkey1).zfill(20),2) ^ int(person3,2)
print "XOR person2 and prekey into key variable " + ('{0:b}'.format(masterkey2).zfill(20))

#Clearing number pad variables
del person1
del person2
del person3

#Wait for user input
raw_input("\nMaster key generated. Press any key to continue...")

#User input
person1 = input("Person 1! Enter a single digit code: ")
person2 = input("Person 2! Enter a single digit code: ")
person3 = input("Person 3! Enter a single digit code: ")

#Convert into binary and remove unwanted characters
person1 = (bin(person1).replace("0b","").zfill(20))
person2 = (bin(person2).replace("0b","").zfill(20))
person3 = (bin(person3).replace("0b","").zfill(20))

print "\nBinary"
print "Person 1 " + person1
print "Person 2 " + person2
print "Person 3 " + person3 + "\n"

#XOR person1 and person2 into masterkey3 variable
masterkey3 = int(person1,2) ^ int(person2,2)
print "XOR person1 and person2 into masterkey3 variable " + ('{0:b}'.format(masterkey3).zfill(20))

#XOR person2 and prekey into masterkey4 variable
masterkey4 = int('{0:b}'.format(masterkey3).zfill(20),2) ^ int(person3,2)
print "XOR person2 and prekey into masterkey4 variable " + ('{0:b}'.format(masterkey4).zfill(20))

#Checks if both master keys are correct
if masterkey2 == masterkey4:
	print("\nBoth master keys match! ACCESS GRANTED")
else:
	print("\nERROR! An incorrect number has been enetered! ACCESS DENIED")