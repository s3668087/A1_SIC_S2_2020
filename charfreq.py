cihpertext = raw_input("Enter a cyphertext: ")

alphabet = [
    'A','B','C','D','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','z'
]

hits = [
    (alphabet[i], cihpertext.count(alphabet[i]))
    for i in range(len(alphabet))
    if cihpertext.count(alphabet[i])
]

for letter, frequency in hits:
    print letter.upper(), frequency
