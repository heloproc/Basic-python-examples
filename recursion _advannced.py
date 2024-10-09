def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)  # Print the indentation and function call
    if n == 0:
        print(space, 'returning 1') # Print the indentation and return value
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result) # Print the indentation and return value
        return result

factorial(4)

# output-
#                  factorial 4
#              factorial 3
#          factorial 2
#      factorial 1
#  factorial 0
#  returning 1
#      returning 1
#          returning 2
#              returning 6
#                  returning 24