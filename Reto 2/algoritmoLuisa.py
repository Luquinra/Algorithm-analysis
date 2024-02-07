def encontrar_pares(lista, suma_objetivo):
  pares = []
  # Crear un conjunto para almacenar los números que ya hemos visto
  numeros_vistos = set()

  for num in lista:
      # Calcular el complemento necesario para alcanzar la suma objetivo
      complemento = suma_objetivo - num
      # Si el complemento está en el conjunto de números vistos, encontramos un par
      if complemento in numeros_vistos:
          pares.append((num, complemento))
      # Agregar el número actual al conjunto de números vistos
      numeros_vistos.add(num)

  return pares

# Ejemplo de uso
lista = [1, 9, 5, 0, 20, -4, 12, 16, 7]
suma_objetivo = 12
resultado = encontrar_pares(lista, suma_objetivo)
for par in resultado:
  print(f"{par[0]},{par[1]}")