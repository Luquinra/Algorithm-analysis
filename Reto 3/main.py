def problem_1(limit):
  total_sum = 0
  for i in range(limit):
    if i % 3 == 0 or i % 5 == 0:
      total_sum += i
  return total_sum


limit = 1000
result = problem_1(limit)
print("The sum of all the multiples of 3 or 5 below", limit, "is:", result)


def problem_2(max_limit):
  prev_term = 1
  current_term = 2
  sum_even = 0

  while current_term <= max_limit:
    if current_term % 2 == 0:
      sum_even += current_term

    next_term = prev_term + current_term
    prev_term = current_term
    current_term = next_term

  return sum_even


max_limit = 4000000
result = problem_2(max_limit)
print("The sum of even-valued terms in the Fibonacci sequence not exceeding",
      max_limit, "is:", result)


def problem_3(n):
  factor = 2  # Comenzamos con el primer número primo
  largest_factor = 0

  while n > 1:
    while n % factor == 0:  # Mientras n sea divisible por el factor
      largest_factor = factor  # Actualizamos el factor primo más grande encontrado
      n //= factor  # Dividimos n por el factor
    factor += 1  # Pasamos al siguiente número primo

  return largest_factor


number = 600851475143
result = problem_3(number)
print("The largest prime factor of", number, "is:", result)


def is_palindrome(n):
  # Convierte el número a una cadena y verifica si es igual a su reverso
  return str(n) == str(n)[::-1]


def problem_4():
  largest_palindrome = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i * j
      if is_palindrome(product) and product > largest_palindrome:
        largest_palindrome = product
  return largest_palindrome


result = problem_4()
print(
    "The largest palindrome made from the product of two 3-digit numbers is:",
    result)


def gcd(a, b):
  while b:
    a, b = b, a % b
  return a


def lcm(a, b):
  return a * b // gcd(a, b)


def problem_5(limit):
  result = lcm(1, 2)
  for i in range(3, limit + 1):
      result = lcm(result, i)
  return result


print(
    "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:",
    result)
