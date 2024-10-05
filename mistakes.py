def is_prime(number):
    for divisor in range(2, number):
        if (number % divisor) == 0:
            return False
        return True
print(is_prime(9))

#vs
#correct one
def is_prime(number):
    for divisor in range(2, number):
        if (number % divisor) == 0:
            return False
    return True
print(is_prime(9))