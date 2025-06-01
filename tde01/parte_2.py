import random

def random_walk_2(n):
    x,y=0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return x,y

numero_caminhadas=30000
media_mais_longa = [100]
caminhada_mais_longa = [0]

for comprimento_caminhada in range(1,51):
    sem_transporte=0
    for i in range(numero_caminhadas):
        x,y = random_walk_2(comprimento_caminhada)
        distancia = abs(x) + abs(y)
        if distancia <=5:
            sem_transporte+=1
    sem_transporte_porcentagem = (float(sem_transporte) / numero_caminhadas)*100
    if sem_transporte_porcentagem>50:
        caminhada_mais_longa.append(comprimento_caminhada)
        media_mais_longa.append(sem_transporte_porcentagem)
    print("comprimento da caminhada = ", comprimento_caminhada, "/ % de não ter transporte",sem_transporte_porcentagem)
print("O maior comprimento que te deixa em média mais próximo de casa é ", caminhada_mais_longa[-1], "com uma média de ", media_mais_longa[-1])