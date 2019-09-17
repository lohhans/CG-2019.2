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
        listaDeFaces.append(lista[1:lista[0]+1])

    return listaDeFaces


nomeArquivo = 'hand-hybrid.off'
arquivo = abrirArquivo(nomeArquivo)
listaDeLinhas = arquivo.readlines()  # Ler todas as linhas do arquivo
numPontos, numFaces = qtdPontosFaces(listaDeLinhas)

arquivo.seek(0)  # Zerando o método readlines

linha = arquivo.readline()
linha = arquivo.readline()

print(numPontos, numFaces)

listaDePontos = listarPontos(arquivo, numPontos)
listaDeFaces = listarFaces(arquivo, numFaces)

print(listaDePontos)
print(listaDeFaces)
