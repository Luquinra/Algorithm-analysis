import random
import string

def generar_cadena_aleatoria():
  return ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

def busqueda_secuencial (lista, id_buscado):
  tamano_lista = len(lista)
  for actual in range(0, tamano_lista):
      if (lista[actual] == id_buscado):
          return actual
  return -1

def busqueda_binaria(lista, id_buscado):
    tamano_de_lista = len(lista)
    inicio = 0
    fin = tamano_de_lista-1

    while inicio <= fin:
        medio=(inicio+fin)//2
        if lista[medio] == id_buscado:
            return medio
        elif lista[medio] < id_buscado:
            inicio=medio+1
        elif lista[medio] > id_buscado:
            fin = medio-1
    return -1

if __name__ == '__main__' :
   
  cantidad_elementos = 500000

  # Creacion de estructuras de datos
  lista_ids = list(range(1, cantidad_elementos + 1))
  lista_nombre = [generar_cadena_aleatoria() for _ in range(cantidad_elementos)]
  lista_edad = [random.randint(18, 100) for _ in range(cantidad_elementos)]
  lista_impuestos = [random.choice([True, True, True, False]) for _ in range(cantidad_elementos)]
  lista_registros = list(zip(lista_ids, lista_nombre, lista_edad, lista_impuestos))
  print(lista_registros[-1])
  print()
  
  # Menu
  while True:
    print("1. Buscar por Id")
    print("2. Buscar por nombre")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))
    print()
    
    if opcion == 1:
        id_buscado = int(input("Ingrese el ID a buscar: "))
        indice = busqueda_binaria(lista_ids, id_buscado)
        if indice != -1:
            print(f"Se encontro el ID {id_buscado} en la posición {indice} \n")
        else:
            print(f"ID no encontrado \n")
    elif opcion == 2:
        nombre_buscado = input("Ingrese el nombre a buscar: ")
        indice = busqueda_secuencial(lista_nombre, nombre_buscado)
        if indice != -1:
            print(f"Se encontro el nombre {nombre_buscado} en la posición {indice} \n")
        else:
            print(f"Nombre no encontrado \n")
    if opcion == 3:
        break