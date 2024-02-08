import random 

def generar_lista(n):
  lista = []
  for i in range(n):
    numero = 0
    margen = n+int(n/4)
    while numero in lista:
      numero = random.randint((-1*margen), (margen))      
    lista.append(numero)
  return lista

def funcion_jerson(lista,valor):
  lista.sort()
  parejas = []

  tam_lista = len(lista)
      
  
  for i in lista:
    complemento = valor - i
    if complemento > i :
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
        parejas.append([i,lista[posicion]])
  return parejas
  
def main():
  enteros = generar_lista(int(input("Ingrese el tamaño del arreglo: ")))
  parejas = []
  print("La lista de enteros es: ")
  print(enteros)
  entero_dado = int(input("Ingrese el valor objerivo: "))
  
  print("Buscando las parejas que suman ",entero_dado)
  parejas = funcion_jerson(enteros, entero_dado)

  print("Las parejas que suman ",entero_dado," son: ")
  print(parejas)
  
  return 0

main()