import random as rd

cantidad_de_numeros = int(input('Cuantos numeros desea jugar? '))
numeros_jugados = []

# Esta funcion evaluara si fallas o Aciertas
def acierto(numeros_jugados, maquina):
    numeros_ganadores = []
    maquina.sort()
    numeros_jugados.sort()
    for i in numeros_jugados:
        for j in maquina:
            if i == j:
                numeros_ganadores.append(i)
                print(f'Ganaste con {numeros_ganadores}')
                break
            else:
                print('Te Guayaste')
                break


# Aqui se generan la preguntas de los numeros que ingresaras
for i in range(cantidad_de_numeros):
    numero_jugado = input(f'{i+1} numero a jugar: ')
    # Esto validara si el numero es ingresado, si no lo es preguntara nuevamente
    while True:
        if numero_jugado == '':
            numero_jugado = input(f'{i+1} numero a jugar: ')
        else:
            break

    numeros_jugados.append(numero_jugado)

# Aqui la maquina hara su jugada
maquina = []
for _ in range(cantidad_de_numeros):
    numero_ganador = rd.randint(1,100)
    maquina.append(str(numero_ganador))

acierto(numeros_jugados, maquina)

print(f'\nLa maquina: {maquina}')
print(f'Tu: {numeros_jugados}')
