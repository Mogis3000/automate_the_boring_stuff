# Automate the Boring Stuff by Al Sweigart
# pg 70

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()
