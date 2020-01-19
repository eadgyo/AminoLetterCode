from builtins import input

AminoLetter = {"A": "Alanine",
               "C": "Cysteine",
               "R" : "Arginine",
               "N" : "Asparagine",
               "D": "Aspartic Acid",
               "E" : "Glutamic Acid",
               "Q" : "Glutamine",
               "G" : "Glycine",
               "H" : "Histidine",
               "I" : "IsoLeucine",
               "L" : "Leucine",
               "K" : "Lysine",
               "M" : "Methionine",
               "F" : "Phenylalanine",
               "P" : "Proline",
               "S" : "Serine",
               "T" : "Threonine",
               "W" : "Tryptophan",
               "Y" : "Tyrosine",
               "V" : "Valine"}
Count = {}

code = input("Enter your amino acid code sequence: ")
print("\n")
code = code.upper()
newCode = ""
for k in code:
    if k != ' ':
        if k not in AminoLetter:
            print("Error: This amino letter does not exist '" + k + "'")
        else:
            value = AminoLetter[k]
            newCode += value + "-"
            if value in Count:
                Count[value] += 1
            else:
                Count[value] = 1

# Remove the - terminaison
if len(newCode) != 0:
    newCode = newCode[:-1]
print("Your Amino Sequence: " + newCode)

print("Count: ")
for x in Count:
    print (x + " : " + str(Count[x]))
