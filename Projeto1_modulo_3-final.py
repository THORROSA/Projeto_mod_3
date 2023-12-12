#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


#Simulação de Dados: Crie uma função que simule o lançamento de dois dados de seis lados (valores de 1 a 6). 
#Esta função deve retornar a soma dos resultados dos dados.
def lancamento_dados():
    dado1 = np.sum((np.random.randint (1, 7)))
    dado2 = np.sum((np.random.randint (1, 7)))
    return dado1+dado2


# In[17]:


lancamento_dados()


# In[75]:


#Múltiplas Simulações: Use a função do passo 1 para simular um grande número de jogos de dados (digamos, 1000 jogos). 
#Armazene o resultado de cada jogo em um array NumPy.


def multiplos_jogos(jogos):
    
    resultados = np.array([lancamento_dados() for i in range(jogos)])
    
#Análise de Dados: Agora, vamos analisar os resultados desses jogos. Calcule e imprima o seguinte:

#A média dos resultados.
#O lançamento máximo e mínimo.
#O número de vezes que cada possível lançamento (2, 3, 4, 5, 6, 7, 8, 9, 10, 11 e 12) ocorreu.
#Teste de Hipótese: Agora vamos fazer um pouco de teste de hipóteses:
#Supondo um jogo justo (ou seja, todos os lançamentos são igualmente prováveis), 
#o resultado da sua simulação coincide com essa suposição? Por que sim ou por que não?
#O que isso significa para um jogador do jogo de dados?

    media = np.mean(resultados)
    maximo =np.max(resultados)
    minimo =np.min(resultados)
    possiveis =  (2, 3, 4, 5, 6, 7, 8, 9, 10, 11 , 12)
    for i in possiveis:
        contagem = np.bincount(resultados)
    #contagem
    print(f'a média é de {media}')
    print(f'o maximo valor é de {maximo}')
    print(f'o minimo valor é de {minimo}')
    print(f'a contagem dos valores das listas de possiveis foi {contagem}')
    print(f'as amostras analisadas foram{resultados}')
    return 


# In[88]:


multiplos_jogos(1000)

