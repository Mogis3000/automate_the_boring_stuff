# Automate the Boring Stuff by Al Sweigart
# pg 69

from pkg_resources import EGG_DIST


def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is a global

eggs = 42 # this is the global
spam()
print(eggs)
