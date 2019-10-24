def representar():
    file  = open("triangles.off", "r")
    head = file.readline().strip("\n")
    if head != "OFF":
	    file.close()
           
    cfg = file.readline()
    cfg = cfg.split(" ")
    resultados = map(int, cfg)

    numero_pontos = resultados[0]
    numero_triangulos = resultados[1]
    normal = resultados[2]

    coordenadas = []

    for x in xrange(0,numero_pontos):
        ponto = file.readline().strip("\n")
        ponto = ponto.split(" ")
        ponto = map(float ,ponto)
        coordenadas.insert(x,ponto)
        print(ponto)
    retornar = []

    for x in xrange(0,numero_triangulos):
        triangulo = file.readline().strip("\n")
        triangulo = triangulo.split(" ")
        triangulo = map(int ,triangulo)
        temp = []
        for y in xrange(1, triangulo[0]+1):
                temp.append(coordenadas[triangulo[y]])
        retornar.insert(x,temp)
    file.close()
    print(retornar)

representar()