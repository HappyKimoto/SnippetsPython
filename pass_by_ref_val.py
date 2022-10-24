# Test1
# when an integer is passed to a function, 
# the passed variable address stays the same.
# However, if the passed variable is used within the function,
# the variable will be assigned to a new local variable.
def fnc1(x, y):
    print(f'1 called: id(x) = {id(x)}') # same as the caller
    print(f'1 called: id(y) = {id(y)}') # same as the caller
    x += 3
    y += 4
    print(f'2 called: id(x) = {id(x)}') # newly created
    print(f'2 called: id(y) = {id(y)}') # newly created
    return x + y

x = 3
y = 4
print(f'caller: id(x) = {id(x)}')
print(f'caller: id(y) = {id(y)}')

fnc1(x, y)

# Test2
# In class, self is the object instance.
# The address of the class instance stays the same even if the object is passed and returned.
class Cls1:
    def __init__(self, x):
        self.x = x
    
    def print_x(self):
        print(f'self - id(self)={id(self)}') # address of self
        print(f'{self.x} was passed')

def fnc2(c):
    print(f'passed - id(c)={id(c)}') # address of the passed class instance
    c.print_x()
    return c

x = 5

c1 = Cls1(x)
print(f'original - id(c1)={id(c1)}')
c11 = fnc2(c1)
print(f'returned - id(c11)={id(c11)}')
print()

c2 = Cls1(x)
print(f'original - id(c2)={id(c2)}')
c22 = fnc2(c2)
print(f'returned - id(c22)={id(c22)}')
print()

# Test3
# In class, self is the object instance.
def fnc3(c):
    print(f'On fnc3: id(c)={id(c)}')
    return c

from pathlib import Path
script_path = Path( __file__ ).absolute()
f = open(script_path, 'rb')
print(f'id(f)={id(f)}')
print(type(f)) # <class '_io.BufferedReader'>
f.close()
print(f'id(f)={id(f)}') # after closing, the address is still the same.
f2 = fnc3(f)
print(f'id(f2)={id(f2)}') # returned from function but the address stays the same.


