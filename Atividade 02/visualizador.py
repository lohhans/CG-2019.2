# <>=================================<>
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# ||        Armstrong Lohans         ||
# ||    Computacao Grafica 2019.2    ||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# <>=================================<>

import malhas

import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from malhas import *

w, h = 500, 500

def visualizar():
    for numero in expression_list:
        pass

    if condition:
        pass
    else:
        pass
    glBegin(GL_TRIANGLES)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    visualizar()
    glutSwapBuffers()


nomeArquivo = raw_input("Digite o nome do arquivo: ")

try:
    numPontos, numFaces, listaDePontos, listaDeFaces, listaDeFormaDeFaces = malhas.iniciarLeitura(
        nomeArquivo)
    print(listaDeFormaDeFaces)
    print(numPontos, numFaces)
except IOError:
    print("Arquivo incorreto!")

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
