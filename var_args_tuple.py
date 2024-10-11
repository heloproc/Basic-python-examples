# Functions can take a variable number of arguments. A parameter name that begins with
# * gathers arguments into a tuple. For example, printall takes any number of arguments
# and prints them:
def printall(*args):
print args
# The gather parameter can have any name you like, but args is conventional. Here’s how
# the function works:
printall(1, 2.0, '3')
(1, 2.0, '3')
# The complement of gather is scatter. If you have a sequence of values and you want to pass
# it to a function as multiple arguments, you can use the * operator. For example, divmod
# takes exactly two arguments; it doesn’t work with a tuple:
t = (7, 3)
divmod(t)
TypeError: divmod expected 2 arguments, got 1
# But if you scatter the tuple, it works:
divmod(*t)
(2, 1)
