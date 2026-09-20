import math

from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def refresh(window):

    glClearColor(1.0, 1.0, 0.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(-0.5, 0.5)
    glEnd()

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0.0, 0.0)

    num_segments = 100
    radius = 0.3

    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i / num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex2f(x, y)
    glEnd()

    glfwSwapBuffers(window)


def main():
    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(800, 600, "Week 2 - Basic Rendering", None, None)
    if not window:
        glfwTerminate()
        return

    glfwMakeContextCurrent(window)

    while not glfwWindowShouldClose(window):
        refresh(window)
        glfwPollEvents()

    glfwTerminate()


if __name__ == "__main__":
    main()
