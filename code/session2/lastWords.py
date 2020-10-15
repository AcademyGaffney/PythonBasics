inString = input("Please enter a sentence: ")

firstSpace = inString.find(" ")
outString = inString[firstSpace + 1:]

print(outString)

outString = outString[0].upper() + outString[1:]

print(outString)

