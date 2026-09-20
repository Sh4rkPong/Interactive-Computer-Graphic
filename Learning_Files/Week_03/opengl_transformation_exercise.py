import os
import sys

import numpy as np
import pandas as pd
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

win_w, win_h = 800, 600
np.set_printoptions(precision=2, suppress=True)


def draw_Triangles():
    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(0.5 * (normals[i] + 1))
        glVertex3fv(positions[i])
    glEnd()


def refresh(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glViewport(0, 0, win_w, win_h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w / win_h, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(0, 2.5, 3.5, 0, 0, 0, 0, 1, 0)
    glRotatef(degree, 0, 1, 0)
    scale_factor = 1 / np.max(bbox)

    glPushMatrix()
    glTranslatef(-1.3, 0, 0)
    glScalef(0.8 * scale_factor, 0.8 * scale_factor, 0.8 * scale_factor)
    glTranslatef(-centroid[0], -centroid[1], -centroid[2])
    draw_Triangles()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0, -0.4)
    glScalef(1.3 * scale_factor, 1.3 * scale_factor, 1.3 * scale_factor)
    glTranslatef(-centroid[0], -centroid[1], -centroid[2])
    draw_Triangles()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.2, 0, 0.4)
    glScalef(0.4 * scale_factor, 0.4 * scale_factor, 0.4 * scale_factor)
    glTranslatef(-centroid[0], -centroid[1], -centroid[2])
    draw_Triangles()
    glPopMatrix()

    glfwSwapBuffers(window)

    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(0.5 * (normals[i] + 1))
        glVertex3fv(positions[i])
    glEnd()


degree = 0


def animation(window):
    global degree
    degree = degree + 3
    glfwPostEmptyEvent()


wireframe_on, animation_on = False, False


def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)
    glfwPostEmptyEvent()


def my_init():
    global n_vertices, positions, colors, normals, uvs
    global centroid, bbox

    glClearColor(0.2, 0.8, 0.8, 1)
    df = pd.read_csv(
        "../models/teapot.tri", sep="\s+", comment="#", header=None, dtype=np.float32
    )
    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]

    bbox = positions.max(axis=0) - positions.min(axis=0)
    centroid = 0.5 * (positions.min(axis=0) + positions.max(axis=0))

    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % (n_vertices, n_vertices // 3))
    print("centroid:", np.array2string(centroid, separator=", "))
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)


def main():
    if not glfwInit():
        glfwTerminate()
        return

    window_w, window_h = 800, 600
    window = glfwCreateWindow(
        window_w, window_h, "OpenGL Transformation Exercise - TeAPOT", None, None
    )
    glfwMakeContextCurrent(window)
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetKeyCallback(window, keyboard)

    my_init()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        refresh(window)
        glfwWaitEvents()
    glfwDestroyWindow(window)
    glfwTerminate()


if __name__ == "__main__":
    main()
