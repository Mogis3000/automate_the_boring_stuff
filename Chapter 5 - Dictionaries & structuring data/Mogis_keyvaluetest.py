# Automate the Boring Stuff by Al Sweigart
# pg 114
# Mogis testing a theory about the variable assigned in the for loop.

from tkinter import N


spam = {'color': 'red', 'age': 42}
#for v in spam.values():  # Mogis' notes: the 'v' means nothing and is an arbitrary variable that is chosen BY THE WRITER OF THE CODE, it can be changed to anything and still work
#    print(v) # As long as it matches the value that is being called for printing

print('Printing the Values in the dictionary!')
for ambiguousVariable_klrdrvrg in spam.values():
    print(ambiguousVariable_klrdrvrg)

print('Printing the Keys in the dictionary!')
#for k in spam.keys(): # Same thing applies here, 'k' is not a predetermined value to go here, it can be changed to whatever you want
#    print(k) # So long as it matches what is being called here

for purplemonkeydishwasher in spam.keys():
    print(purplemonkeydishwasher)

print()
print('Printing the keys of the dictionary below using the spam.keys() command!')
print(spam.keys())
print()

print('Using the list(spam.keys()) command to see the difference below!')
print(list(spam.keys()))
print()

print('Printing the values of the dictionary below using the spam.values() command!')
print(spam.values())
print()

print('Using the list(spam.values()) command to see the difference below!')
print(list(spam.values()))
print()

print('Printing the keys and values of the dictionary below using the spam.items() command')
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
