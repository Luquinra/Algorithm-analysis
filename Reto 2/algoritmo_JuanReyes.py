import time

def algoritmo_JuanReyes(lista, val):
    inicio = time.time()

    for i in range(len(lista)-1):
        num1 = lista[i]
        lista_sin_num1 = lista[i+1:]

        for j in range(len(lista_sin_num1)):
            num2 = lista_sin_num1[j]
            if num1 + num2 == val:
                print("Pareja encontrada:", num1, "+", num2, "=", val)
                lista.remove(num2)
                break

    # Calcular el tiempo
    tiempo_transcurrido = time.time() - inicio
    print("Tiempo transcurrido:", tiempo_transcurrido, "segundos")


lista = [1, 9, 5, 0, 20, -4, 12, 16, 7, 8, -1, 3, 2, 6, 4, 11, 10, 13, 14, 15, 17, 18, 19, -3, -5, 50, 30, -24, 60, 25, -74, 94, 500, -319, 257, 243, 1500, -500, 376, 624]
suma_objetivo = 1000

'''
lista = [1, 9, 5, 0, 20, -4, 12, 16, 7]
suma_objetivo = 12
'''

algoritmo_JuanReyes(lista, suma_objetivo)