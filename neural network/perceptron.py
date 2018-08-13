import random
import numpy as np
class Perceptron:
    def __init__(self, amostras, saidas, taxa_aprendizagem = 0.1, epocas = 10, limiar = -1):
        self.amostras = amostras
        self.saidas = saidas
        self.taxa_aprendizagem = taxa_aprendizagem
        self.epocas = epocas
        self.limiar = limiar
        self.n_amostras = len(amostras)
        self.n_atributos = len(amostras[0])
        self.pesos = []

    def treinar(self):
        #for amostra in self.amostras:
         #   amostra.insert(0, -1)
        for i in range(self.n_atributos):
            self.pesos.insert(i, random.random())

        #self.pesos.insert(0, self.limiar)
        epoca = 0
        self.pesos = np.array(self.pesos)

        while True:
            erro = False   


            for i in range(self.n_amostras):
                u = 0

                #for j in range(self.n_atributos):
                 #   u += self.pesos[j] * self.amostras[i][j]
                u = self.pesos.dot(self.amostras[i])
                y = self.degrau(u)
               
                if y != self.saidas[i]:
                    erro = self.saidas[i] - y

                    for j in range(self.n_atributos):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizagem * erro * self.amostras[i][j] 
                        erro = True
            epoca = epoca + 1
            
            if not erro or epoca > self.epocas:
                break
        
    def degrau(self, u):
        if u >= 0:
            return 1
        return 0
    def testar(self, amostra):
        #amostra.insert(0, -1)
        u = 0
        for i in range(self.n_atributos):
            u += self.pesos[i] * amostra[i]
        y = self.degrau(u)
        print(y)

entradas = np.array([[0,0], [0,1], [1,0], [1,1]])
saidas = np.array([0, 1, 1, 1])
perceptron = Perceptron(entradas, saidas)
perceptron.treinar()
perceptron.testar([1,1])