import random

def random_walk_2(n):
    x, y = 0, 0
    for _ in range(n):
        dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        x += dx
        y += dy
    return (x, y)

numero_caminhadas = 20000
limite_distancia_media = 5
max_n = 100  # podemos aumentar se quiser

melhor_n = 0
melhor_media = 0

for comprimento in range(1, max_n + 1):
    soma_distancias = 0

    for _ in range(numero_caminhadas):
        x, y = random_walk_2(comprimento)
        distancia = abs(x) + abs(y)
        soma_distancias += distancia

    distancia_media = soma_distancias / numero_caminhadas
    print(f"Comprimento = {comprimento} / Distância média = {distancia_media:.4f}")

    if distancia_media <= limite_distancia_media:
        melhor_n = comprimento
        melhor_media = distancia_media

print(f"\n📌 Maior comprimento com distância média ≤ {limite_distancia_media}: {melhor_n}")
print(f"   Distância média nesse ponto: {melhor_media:.4f}")
