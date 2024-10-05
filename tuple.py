#A py program to change values of elements of a tuple
new_tuple = (5, 6, 7, 8)
# Because tuples are immutable, we cannot redefine
#  a single element (remember this does work with lists, though)
#new_tuple[1] = 77 # Returns an error

# We can  do something called _tuple unpacking_

(a, b, c, d) = new_tuple
print ("a is:", a)
print ("b is:", b)
print ("c is:", c)
print ("d is:", d
)
# Make sure that you always have the same number of
# variables when you unpack a tuple!

# Tuples are immutable. To change a tuple, we would need
# to first unpack it, change the values, then repack it:

# Redefine b
b = 77

# Repack the tuple
new_tuple = (a, b, c, d)
print ("new_tuple is now:", new_tuple)