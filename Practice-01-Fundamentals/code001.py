# separate vowels and consonants

phrase = "Python is so good, that make it all easy"

vowels = "aeiou"

vlist = []
clist = []

for letter in phrase:
    if letter in vowels:
        vlist.append(letter)
    if letter not in vowels:
        clist.append(letter)

print(vlist)
print(clist)

# writing in one line
vlist2 = [letter for letter in phrase if letter in vowels]
print(vlist2)

# working with sets
# set of vowels not repeating
setv2 = {letter for letter in phrase if letter in vowels}
print(setv2, "<<<<<<<<< set v2")
