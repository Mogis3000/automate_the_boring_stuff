# Automate the Boring Stuff by Al Sweigart
# pg 64

def a():
    print('def a() starts')
    b()
    d()
    print('def a() returns')

def b():
    print('def b() starts')
    c()
    print('def b() returns')

def c():
    print('def c() starts')
    print('def c() returns')

def d():
    print('def d() starts')
    print('def d() returns')

a()