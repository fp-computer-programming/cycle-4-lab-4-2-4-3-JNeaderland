#Author: Jacob Neaderland
#Lab 4-2
school = "Fairfield Prep"
print (school[0:9])
print (school[10:])

#Lab 4-3
word = input ("word?")
if word == "Fairfield Prep":
    print ("Fairfield Prep")
elif word > "Fairfield Prep":
    print (word + " comes before Fairfield Prep")
elif word < "Fairfield Prep":
    print (word + " comes after Fairfield Prep")
else:
    print (word)