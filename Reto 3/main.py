from math import gcd

def sum_of_multiples(limit):
  total_sum = 0
  for i in range(limit):
      if i % 3 == 0 or i % 5 == 0:
          total_sum += i
  return total_sum

limit = 1000
result = sum_of_multiples(limit)
print("The sum of all the multiples of 3 or 5 below", limit, "is:", result)

def fibonacci_sum_even(max_limit):
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
result = fibonacci_sum_even(max_limit)
print("The sum of even-valued terms in the Fibonacci sequence not exceeding", max_limit, "is:", result)

def largest_prime_factor(n):
  factor = 2  # Comenzamos con el primer número primo
  largest_factor = 0

  while n > 1:
      while n % factor == 0:  # Mientras n sea divisible por el factor
          largest_factor = factor  # Actualizamos el factor primo más grande encontrado
          n //= factor  # Dividimos n por el factor
      factor += 1  # Pasamos al siguiente número primo

  return largest_factor

number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", result)

def is_palindrome(n):
  # Convierte el número a una cadena y verifica si es igual a su reverso
  return str(n) == str(n)[::-1]

def largest_palindrome_product():
  largest_palindrome = 0
  for i in range(100, 1000):
      for j in range(100, 1000):
          product = i * j
          if is_palindrome(product) and product > largest_palindrome:
              largest_palindrome = product
  return largest_palindrome

result = largest_palindrome_product()
print("The largest palindrome made from the product of two 3-digit numbers is:", result)

# Función para calcular el mínimo común múltiplo (LCM) de dos números
def lcm(a, b):
    return a * b // gcd(a, b)

# Función para calcular el mínimo común múltiplo (LCM) de una lista de números
def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

# Calcula el mínimo común múltiplo (LCM) de los números del 1 al 20
result = lcm_of_list(range(1, 21))

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is:", result)
