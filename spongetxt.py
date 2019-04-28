import random
print("sPoNGeBoB tExT gEneRAtOr")
str = input("Enter your text here: ")
flip = 0 #FIRST CHAR ALWAYS LOWERCASE

spongetext = ""
for x in range(len(str)):
    flip = flip ^ random.randrange(0,2) #XOR
    
    if flip==0:
        spongetext += str[x].lower()
    else:
        spongetext += str[x].upper()

print(spongetext)
