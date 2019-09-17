# <>=================================<>
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# ||        Armstrong Lohãns         ||
# ||    Computação Gráfica 2019.2    ||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# <>=================================<>

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


nomeArquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = abrirArquivo(nomeArquivo)
    listaDeLinhas = arquivo.readlines()  # Ler todas as linhas do arquivo e guarda numa lista
    numPontos, numFaces = qtdPontosFaces(listaDeLinhas)  # Obtendo numero de pontos e faces

    arquivo.seek(0)  # Zerando o método readlines

    linha = arquivo.readline()  # Ignorando a primeria linha do arquivo
    linha = arquivo.readline()  # Ignorando a segunda linha do arquivo

    listaDePontos = listarPontos(arquivo, numPontos)  # Gerando lista de pontos
    listaDeFaces = listarFaces(arquivo, numFaces)  # Gerando lista de faces

    print("\n")
    print("Arquivo:", nomeArquivo, "/", "Número de pontos:", numPontos, "/ Número de faces: ", numFaces)
    print("\n")

    print("Lista de pontos:\n")
    for indice in range(len(listaDePontos)):
        print(listaDePontos[indice])

    print("\n")

    print("Lista de faces:\n")
    for indice in range(len(listaDeFaces)):
        print(listaDeFaces[indice])
except IOError:
    print("Arquivo incorreto!")
