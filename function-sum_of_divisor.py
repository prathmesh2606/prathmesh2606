def sum_divisors(n):
  add = 0
  div = 1
  while div<n:
    if n%div == 0:
      add = add+div
    div += 1
  return add

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114
