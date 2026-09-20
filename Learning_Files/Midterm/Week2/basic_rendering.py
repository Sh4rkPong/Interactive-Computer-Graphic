from OpenGL.GL import *
import math
from OpenGL.GLU import *

from glfw.GLFW import *


def window_reshape(window, w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    aspect = w / h
    if w >= h:
        glOrtho(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0, -1.0, 1.0)
    else:
        glOrtho(-1, 1, -aspect, aspect, -1, 1)

    glMatrixMode(GL_MODELVIEW)

def refresh(window):

    glClearColor(0,1,1,0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,1)
    glBegin(GL_QUADS)
    glVertex2f(-0.4, -0.4)
    glVertex2f(0.4, -0.4)
    glVertex2f(0.4, 0.4)
    glVertex2f(-0.4, 0.4)
    glEnd()

    glColor3f(0,1,0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)

    num_segment = 100

    for i in range(num_segment + 1):
        theta = i * 2 * math.pi / num_segment
        x = 0.25 * math.cos(theta)
        y = 0.25 * math.sin(theta)
        glVertex2f(x, y)
    glEnd()
    glfwSwapBuffers(window)


def main():

    if not glfwInit():

        glfwTerminate()

        return


    window = glfwCreateWindow(800, 600, "Week 2 - Basic Rendering", None, None)

    glfwMakeContextCurrent(window)

    glfwSetWindowSizeCallback(window, window_reshape)


    while not glfwWindowShouldClose(window):

        refresh(window)


        glfwPollEvents()



    glfwTerminate()


if __name__ == "__main__":

    main()
