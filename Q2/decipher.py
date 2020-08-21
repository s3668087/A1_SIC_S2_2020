from tabulate import tabulate

#Define ciphertext as a string
ciphertext = "\nEFA OBE_HA FBK OA_D IBNGDN BHH JBM G_ EFA JGKEBDRA BDJ _ BP SDBOHA EC BKRAIEBGD LFAEFAI BDMEFGDN FBK OAAD NBGDAJ CI DCE. \n_ FCL G HCDN QCI EFGK LBI EC ADJ. FCL G HC_N QCI TABRA. FCL LG_H G FBGH EFA JBM LFAD G IAESID EC EFA OCKCP CQ PM QBPGHM. \nP_ JABI G FCTA EC KAA MCS."

#Make key table
key = (tabulate([['A', 'e'],['B', 'a'],['C', 'o'],['D', 'n'],['E', 't'],['F', 'h'],['G', 'i'],['H', 'l'],['I', 'r'],['J', 'd'],['K', 's'],['L', 'w'],['M', 'y'],['N', 'g'],['O', 'b'],['P', 'm'],['Q', 'f'],['R', 'c'],['S', 'u'],['T', 'p']], headers=['Original Ciphertext', 'Deciphered Text']) + "\n")

#Print ciphertext
print ("Ciphertext" + ciphertext + "\n")

#Print key table
print("Key\n"+ key)


#Wait for user input
raw_input("Press Enter to begin deciphering...")
print "\n"

for r in (("A", "e"),("B", "a"),('C', 'o'),('D', 'n'),('E', 't'),('F', 'h'),('G', 'i'),('H', 'l'),('I', 'r'),('J', 'd'),('K', 's'),('L', 'w'),('M', 'y'),('N', 'g'),('O', 'b'),('P', 'm'),('Q', 'f'),('R', 'c'),('S', 'u'),('T', 'p')):
    ciphertext = ciphertext.replace(*r)
print (ciphertext)


raw_input("\nPress Enter to begin adding the missing letters...")
print "\n"

#"_" replace with t for word "battle"
ciphertext = ciphertext.replace("_", "t", 1)

#"_" replace with a for word "been"
ciphertext = ciphertext.replace("_", "e", 1)

#"_" replace with i for the word "in"
ciphertext = ciphertext.replace("_", "n", 1)

#"_" replace with o for the word "i"
ciphertext = ciphertext.replace("_", "i", 1)

#"_" replace with o for the word "o"
ciphertext = ciphertext.replace("_", "o", 1)

#"_" replace with o for the word "long"
ciphertext = ciphertext.replace("_", "n", 1)

#"_" replace with i for the word "will"
ciphertext = ciphertext.replace("_", "l", 1)

#"_" replace with m for the word "my"
ciphertext = ciphertext.replace("_", "y", 1)

print (ciphertext)
