import random
import time
import pandas as pd
import matplotlib.pylab as plt


def fun_jerson(lista, valor):
  lista.sort()
  parejas = []
  for i in lista:
    complemento = valor - i
    inicio = 0
    fin = len(lista) - 1
    posicion = -1

    while inicio <= fin:
      medio = (inicio + fin) // 2
      if lista[medio] == complemento:
        posicion = medio
        break
      elif lista[medio] < complemento:
        inicio = medio + 1
      else:
        fin = medio - 1

    if posicion != -1:
      parejas.append([i, lista[posicion]])
      lista.remove(i)
      lista.remove(lista[posicion])
  return parejas


def fun_Victor(lista, resultado):
  numeros_vistos = set()
  parejas = set()

  for num in lista:
    complemento = resultado - num
    if complemento in numeros_vistos:
      pareja = (min(num, complemento), max(num, complemento))
      parejas.add(pareja)
    numeros_vistos.add(num)

  return parejas


# algo 3 - daniel v
def fun_Daniel(numbers, target):
  numbers_set = set(numbers)
  pairs = [(x, target - x) for x in numbers
           if (target - x) in numbers_set and x < (target - x)]
  return pairs


#Algoritmo Kamilt
def fun_Kamilt(numbers, target):
  num_set = set(numbers)
  pairs = []
  for num in numbers:
    complement = target - num
    if complement in num_set:
      pairs.append((num, complement))
      num_set.remove(num)
  return pairs


#Algoritmo Luisa
def fun_Luisa(lista, suma_objetivo):
  lista.sort()  # Ordenar la lista
  pares = []
  izquierda = 0
  derecha = len(lista) - 1
  while izquierda < derecha:
    suma_actual = lista[izquierda] + lista[derecha]
    if suma_actual == suma_objetivo:
      pares.append((lista[izquierda], lista[derecha]))
      izquierda += 1
      derecha -= 1
    elif suma_actual < suma_objetivo:
      izquierda += 1
    else:
      derecha -= 1
  return pares


def fun_JuanReyes(lista, val):

  for i in range(len(lista)-1):
      num1 = lista[i]
      lista_sin_num1 = lista[i+1:]

      for j in range(len(lista_sin_num1)):
          num2 = lista_sin_num1[j]
          if num1 + num2 == val:
              print("Pareja encontrada:", num1, "+", num2, "=", val)
              lista.remove(num2)
              break



def main():

  lista = [random.randint(0, 5000) for _ in range(100)]
  resultado = int(input("Ingresa el número entero resultado: "))

  parejas = fun_Victor(lista, resultado)

  if parejas:
    print("Las parejas cuya suma es igual al número resultado son:")
    for pareja in parejas:
      print(pareja)
    else:
      print(
          "No se encontraron parejas cuya suma sea igual al número resultado.")

  tiempos = {
      'fun_Victor': [],
      'fun_jerson': [],
      'fun_Daniel': [],
      'fun_Kamilt': [],
      'fun_JuanReyes': []
  }

  
  inicio = time.perf_counter()
  fun_Victor(lista,resultado)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['fun_Victor'].append(diferencia)

  inicio = time.perf_counter()
  fun_jerson(lista,resultado)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['fun_jerson'].append(diferencia)

  inicio = time.perf_counter()
  fun_Daniel(lista,resultado)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['fun_Daniel'].append(diferencia)

  inicio = time.perf_counter()
  fun_Kamilt(lista,resultado)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['fun_Kamilt'].append(diferencia)

  inicio = time.perf_counter()
  fun_Luisa(lista,resultado)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['fun_Luisa'].append(diferencia)
  
  inicio = time.perf_counter()
  fun_JuanReyes(lista,resultado)
  fin = time.perf_counter()
  diferencia = fin - inicio
  tiempos['fun_JuanReyes'].append(diferencia)

  #imprimir tiempos de ejecucion
  for tipo in tiempos:
    print(f"tiempos de ejecucion ({tipo}):")
    for i, t in zip(lista, tiempos[tipo]):
      print(f"{i} -> {t} segundos")
    print()

  #Crear Dataframe
  
  df = pd.DataFrame(tiempos, index=lista)
  df.index.name = 'lista'
  df.reset_index(inplace=True)
  
  #Graficar tiempos de ejecucion
  plt.plot(df['Lista'], df['fun_Victor'], label='fun_Victor')
  plt.plot(df['Lista'], df['fun_jerson'], label='fun_jerson')
  plt.plot(df['Lista'], df['fun_Daniel'], label='fun_Daniel')
  plt.plot(df['Lista'], df['fun_Kamilt'], label='fun_Kamilt')
  plt.plot(df['Lista'], df['fun_Luisa'], label='fun_Luisa')
  plt.plot(df['Lista'], df['fun_JuanReyes'], label='fun_JuanReyes')
  plt.legend()
  plt.xlabel('Lista')
  plt.ylabel('tiempo de ejecucion (segundos)')
  plt.title('Tiempos de ejecucion')
  plt.savefig('tiempos.png')


main()
