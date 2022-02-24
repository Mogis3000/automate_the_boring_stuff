# Automate the Boring Stuff by Al Sweigart
# pg 68

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
