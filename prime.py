def is_prime(n, i=2):
  """
  Recursively checks if n is a prime number.

  Args:
    n: The number to check for primality.
    i: The current divisor to check (starts from 2).

  Returns:
    True if n is prime, False otherwise.
  """

  # Base Cases:
  if n <= 1:  # 1 and numbers less than 1 are not prime
    return False
  if i * i > n:  # If i*i > n, we've checked all possible divisors
    return True
  if n % i == 0: # If n is divisible by i, it's not prime
    return False

  # Recursive Step: Check divisibility by the next number
  return is_prime(n, i + 1)

# Get user input
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")