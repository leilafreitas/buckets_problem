import numpy as np
import matplotlib.pyplot
import random

import time

inicio = time.time()


tm = 0.1 
lim = 4 
tp = 100 

'''ESSA LISTA CONTES OS PESOS PARA SERES DIVIDIDOS ENTRE OS BALDES, PARA ESSE CASO, SERIAM NECESSÁRIOS 3 BALDES'''
'''São necessarios 8 baldes, para esse exemplo aqui, ou seja, é pra sobrar 4 baldes'''
'''lista = [2, 2, 1, 4, 2, 3, 2, 2, 1, 2, 4, 4]'''

'''lista = [2, 2, 1, 4, 2, 3]'''
lista = []
for j in range(10):
  lista.append(random.randint(1, 4))
print('LISTA')
print(lista)
tam_lista = len(lista)


def modificacao_sexual(gene):
    global lista
    global lim
    index = random.randint(0, len(lista)-1)
    valor = lista[index]
    cont = 0
    for j in lista:
        if(j+valor) <= lim:
            gene[index] = cont
            break
        cont = cont+1
    return gene


def gpopulacao_i():
    populacao = []
    global tp
    global tam_lista
    for x in range(tp):
        gene = []
        for j in range(tam_lista):
            gene.append(j)
        gene_m = modificacao_sexual(gene)
        populacao.append(gene_m)
    return populacao 


def definir_fitness(gene):
    global lista
    global tam_lista
    global lim
    baldes = np.zeros((1, tam_lista), dtype=int) 
    cont = 0
    fit = 0
    for i in gene:
        baldes[0][i] = baldes[0][i] + lista[cont]
        cont = cont + 1         
    for j in range(tam_lista):
        if baldes[0][j] > lim:
            fit = 0
            return fit
        if baldes[0][j] == 0:
            fit = fit + 1
    return fit


def escolha(popul):
    global tp
    index1 = random.randint((tp*0.85-1), (tp-1))
    index2 = random.randint((tp*0.85-1), (tp-1))
    if(definir_fitness(populacao[index1]) > definir_fitness(populacao[index2])):
        return populacao[index1]
    return populacao[index2]  


def sexual(mae1, mae2):
    filho = []
    global tam_lista
    for t in range(tam_lista):
        if(random.randint(0, 1) == 0):
            filho.append(mae1[t])
        else:
            filho.append(mae2[t])
    return filho


def mutate(child):
    global tam_lista
    x = random.randint(0, (tam_lista-1))
    y = random.randint(0, (tam_lista-1))
    child[x] = y
    return child


populacao = gpopulacao_i()
populacao.sort(key=lambda s: definir_fitness(s))
graph = []
for i in range(100): 
    next_generation = [] 
    for i in range(tp):
        mae1 = escolha(populacao)
        mae2 = escolha(populacao)
        femea = sexual(mae1, mae2) 
        if(random.random() < tm): 
            femea = mutate(femea) 
        next_generation.append(femea)
    populacao = next_generation 
    populacao.sort(key=lambda s: definir_fitness(s))
    graph.append(definir_fitness(populacao[99])) 
matplotlib.pyplot.plot(graph)
print(populacao) 
print("NUMEROS DE BALDES USADOS:")
print(tam_lista - definir_fitness(populacao[99])) 
print("TEMPO EM SEGUNDOS:")
fim = time.time()
print(fim - inicio)
matplotlib.pyplot.show()


