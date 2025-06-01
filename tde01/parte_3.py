import random

direcoes = [(1, 0), (-1, 1), (0, -1)]

def triangular_random_walk(n):
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice(direcoes)
        x += dx
        y += dy
    return x, y

def triangular_distance(x, y):
    return abs(x) + abs(y)

numero_caminhadas = 30000
media_mais_longa = [100]
caminhada_mais_longa = [0]

for comprimento_caminhada in range(1, 51):
    sem_transporte = 0

    for _ in range(numero_caminhadas):
        x, y = triangular_random_walk(comprimento_caminhada)
        distancia = triangular_distance(x, y)
        if distancia <= 5:
            sem_transporte += 1

    sem_transporte_porcentagem = (sem_transporte / numero_caminhadas) * 100

    if sem_transporte_porcentagem > 50:
        caminhada_mais_longa.append(comprimento_caminhada)
        media_mais_longa.append(sem_transporte_porcentagem)

    print(f"Comprimento da caminhada = {comprimento_caminhada} / % sem precisar transporte = {sem_transporte_porcentagem:.2f}%")

print(f"\nO maior comprimento que te deixa em média mais próximo de casa é {caminhada_mais_longa[-1]} com uma média de {media_mais_longa[-1]:.2f}%")
