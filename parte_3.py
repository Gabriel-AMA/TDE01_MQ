import random

def hex_random_walk(n):
    # Coordenadas axiais q, r
    q, r = 0, 0
    direcoes = [(+1, 0), (+1, -1), (0, -1), (-1, 0), (-1, +1), (0, +1)]

    for _ in range(n):
        dq, dr = random.choice(direcoes)
        q += dq
        r += dr

    return q, r

def hex_distance(q, r):
    # Distância de Manhattan para hexágonos (coordenadas axiais)
    return (abs(q) + abs(q + r) + abs(r)) // 2

numero_caminhadas = 20000
limite_distancia_media = 5
max_n = 100

melhor_n = 0
melhor_media = 0

for comprimento in range(1, max_n + 1):
    soma_distancias = 0

    for _ in range(numero_caminhadas):
        q, r = hex_random_walk(comprimento)
        distancia = hex_distance(q, r)
        soma_distancias += distancia

    distancia_media = soma_distancias / numero_caminhadas
    print(f"Comprimento = {comprimento} / Distância média = {distancia_media:.4f}")

    if distancia_media <= limite_distancia_media:
        melhor_n = comprimento
        melhor_media = distancia_media

print(f"\n📌 Maior comprimento com distância média ≤ {limite_distancia_media}: {melhor_n}")
print(f"   Distância média nesse ponto: {melhor_media:.4f}")
