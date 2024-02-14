import pytest
from main import problem_1, problem_2, problem_3, problem_4, problem_5


def test_problem_1_basic():
  assert problem_1(
      1000) == 233168, "La función debería retornar 233168 para el límite 1000"

def test_problem_2_basic():
  assert problem_2(
      10
  ) == 10, "La función debería retornar 10 como la suma de los primeros términos pares"


def test_problem_3_basic():
  assert problem_3(
      600851475143
  ) == 6857, "La función debería retornar 6857 como el mayor factor primo de 600851475143"


def test_problem_4_is_palindrome():
  result = problem_4()
  assert str(result) == str(
      result)[::-1], "El resultado debería ser un palíndromo"


def test_problem_4_within_expected_range():
  result = problem_4()
  assert 10000 <= result <= 998001, "El resultado debería estar dentro del rango de productos de dos números de 3 dígitos"


def test_problem_5_basic():
  assert problem_5(20) == 232792560, "La función debería retornar 232792560 como el número divisible por todos los números del 1 al 20"
