from tabulate import tabulate

#Define ciphertext as a string
ciphertext = "\nEFA OBE_HA FBK OA_D IBNGDN BHH JBM G_ EFA JGKEBDRA BDJ _ BP SDBOHA EC BKRAIEBGD LFAEFAI BDMEFGDN FBK OAAD NBGDAJ CI DCE. \n_ FCL G HCDN QCI EFGK LBI EC ADJ. FCL G HC_N QCI TABRA. FCL LG_H G FBGH EFA JBM LFAD G IAESID EC EFA OCKCP CQ PM QBPGHM. \nP_ JABI G FCTA EC KAA MCS."

#Show the ciphertext
print "Ciphertext" + (ciphertext) +  "\n"


print "Solved EFA"
print "E = T"
print "F = H"
print "A = E\n"

print(tabulate([['E', 'T'], ['F', 'H'], ['A', 'E']], headers=['Original Ciphertext', 'Estimated Character']) + "\n")

ciphertext = (ciphertext.replace("EFA", "THE"))

print "Ciphertext" + (ciphertext) +  "\n"


raw_input("Press Enter to continue...")
print "\n"
