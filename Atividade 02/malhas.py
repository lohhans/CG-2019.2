# <>=================================<>
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# ||        Armstrong Lohans         ||
# ||    Computacao Grafica 2019.2    ||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# <>=================================<>

# Use Python2

def abrirArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    return arquivo


def qtdPontosFaces(lista):
    numPontos = int(lista[1].split()[0])
    numFaces = int(lista[1].split()[1])
    return numPontos, numFaces


def converterFloat(lista):
    for k in range(len(lista)):
        lista[k] = float(lista[k])

    return lista


def converterInt(lista):
    for k in range(len(lista)):
        lista[k] = int(lista[k])

    return lista


def listarPontos(arquivo, numPontos):
    listaDePontos = []
    for k in range(numPontos):
        linha = arquivo.readline()
        linha = linha.split()
        lista = converterFloat(linha)
        listaDePontos.append(lista)

    return listaDePontos


def listarFaces(arquivo, numFaces):
    listaDeFaces = []
    for k in range(numFaces):
        linha = arquivo.readline()
        linha = linha.split()
        lista = converterInt(linha)
        listaDeFaces.append(lista[1:lista[0] + 1])

    return listaDeFaces

def iniciarLeitura(nomeArquivo):
    arquivo = abrirArquivo(nomeArquivo)
    # Ler todas as linhas do arquivo e guarda numa lista
    listaDeLinhas = arquivo.readlines()
    # Obtendo numero de pontos e faces
    numPontos, numFaces = qtdPontosFaces(listaDeLinhas)

    arquivo.seek(0)  # Zerando o metodo readlines

    linha = arquivo.readline()  # Ignorando a primeria linha do arquivo
    linha = arquivo.readline()  # Ignorando a segunda linha do arquivo

    listaDePontos = listarPontos(arquivo, numPontos)  # Gerando lista de pontos
    listaDeFaces = listarFaces(arquivo, numFaces)  # Gerando lista de faces

    return numPontos, numFaces, listaDePontos, listaDeFaces