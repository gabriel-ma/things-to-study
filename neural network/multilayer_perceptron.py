import numpy as np

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def sigmoidDerivative(y):
    return y * (1 - y)

def delta(erro, y):
    return erro * sigmoidDerivative(y)

entradas = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

saidas = np.array([[0],[1],[1],[0]])

pesos0 = 2 * np.random.random((2,3)) - 1
pesos1 = 2 * np.random.random((3,1)) - 1

epocas = 10000

momento = 1
taxaAprendizagem = 0.3

for j in range(epocas):
    camadaEntrada = entradas
    somaSinapse0 = np.dot(camadaEntrada, pesos0)
    camadaOculta = sigmoid(somaSinapse0)
    somaSinapse1 = np.dot(camadaOculta, pesos1)
    camadaSaida = sigmoid(somaSinapse1)

    erro = saidas - camadaSaida

    mediaErro = np.mean(np.abs(erro))
    print('Erro: ' + str(mediaErro) )
    deltaSaida = erro * sigmoidDerivative(camadaSaida)
    pesos1Transposta = pesos1.T
    deltaSaidaXPesos = deltaSaida.dot(pesos1Transposta)
    deltaCamadaOculta = deltaSaidaXPesos * sigmoidDerivative(camadaOculta)
    camadaOcultaTransposta = camadaOculta.T
    novosPesos1 = camadaOcultaTransposta.dot(deltaSaida)
    pesos1 = pesos1 * momento + (novosPesos1 * taxaAprendizagem)
    camadaEntradaTransposta = camadaEntrada.T
    novosPesos0 = camadaEntradaTransposta.dot(deltaCamadaOculta)
    pesos0 = (pesos0 * momento) + (novosPesos0 * taxaAprendizagem)

    #print(deltaCamadaOculta)