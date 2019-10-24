# <>=================================<>
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# ||        Armstrong Lohans         ||
# ||    Computacao Grafica 2019.2    ||
# ||\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\||
# <>=================================<>

# Use Python2

import malhas

import OpenGL
import OpenGL.GL
import OpenGL.GLUT
import OpenGL.GLU

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from malhas import *

w, h, escala = 600, 600, 500


def visualizar():
    for face in listaDeFaces:
        tamFace = len(face)

        if tamFace == 3:
            glBegin(GL_TRIANGLES)
        elif tamFace == 4:
            glBegin(GL_QUADS)
        else:
            print('erro')
            exit()

        for i in face:
            glVertex3f(listaDePontos[i][0]*escala, listaDePontos[i]
                       [1]*escala, listaDePontos[i][2]*escala)

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
    glColor3f(0.0, 1.0, 0.0)
    visualizar()
    glutSwapBuffers()


nomeArquivo = raw_input("Digite o nome do arquivo: ")

try:
    numPontos, numFaces, listaDePontos, listaDeFaces = malhas.iniciarLeitura(
        nomeArquivo)
except IOError:
    print("Arquivo incorreto!")

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(w, h)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("Visualizador de pontos - Armstrong")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()