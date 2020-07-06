def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n!=0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
