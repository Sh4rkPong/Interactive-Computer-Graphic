import os
import sys

import numpy as np
import pandas as pd
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *

overlays = False
normal_on = False
normal_lens = 0.5


def display(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(*(centroid + (0, 10, max(bbox))), *centroid, 0, 1, 0)
    glRotatef(degree, 0, 1, 0)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(0.5 * (normals[i] + 1))
        glVertex3fv(positions[i])
    glEnd()

    if overlays:
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        glLineWidth(1.5)
        glEnable(GL_POLYGON_OFFSET_LINE)
        glPolygonOffset(-1.0, -1.0)

        glBegin(GL_TRIANGLES)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(n_vertices):
            glVertex3fv(positions[i])
        glEnd()

        glDisable(GL_POLYGON_OFFSET_LINE)
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        if normal_on:
            glLineWidth(2.0)
            glBegin(GL_LINES)
            for i in range(0, n_vertices, 3):
                p0 = positions[i]
                p1 = positions[i + 1]
                p2 = positions[i + 2]

                center = (p0 + p1 + p2) / 3.0
                u = p1 - p0
                v = p2 - p0
                face_normal = np.cross(u, v)

                norm = np.linalg.norm(face_normal)
                if norm > 0:
                    face_normal = face_normal / norm

                head = center + (face_normal * normal_lens)

                glColor3f(0.0, 1.0, 0.0)
                glVertex3fv(center)
                glColor3f(1.0, 0.0, 0.0)
                glVertex3fv(head)
            glEnd()

        glfwSwapBuffers(window)


def reshape(window, w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, w / h, 1, 50)


degree = 0


def animation(window):
    global degree
    degree = degree + 1
    glfwPostEmptyEvent()


wireframe_on, animation_on = False, False


def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on
    global overlays, normal_on, normal_lens

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key == GLFW_KEY_T:
            overlays = not overlays
        elif key == GLFW_KEY_N:
            normal_on = not normal_on
        elif key == GLFW_KEY_O:
            normal_lens = max(0.05, normal_lens - 0.05)
        elif key == GLFW_KEY_P:
            normal_lens += 0.05
        elif key == GLFW_KEY_Q or key == GLFW_KEY_ESCAPE:
            glfwSetWindowShouldClose(window, GLFW_TRUE)
        glfwPostEmptyEvent()


def my_init():
    global n_vertices, positions, colors, normals, uvs
    global centroid, bbox

    glClearColor(0.2, 0.8, 0.8, 1)
    df = pd.read_csv(
        "../models/ashtray.tri", sep="\s+", comment="#", header=None, dtype=np.float32
    )
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % (n_vertices, n_vertices // 3))
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glLineWidth(1)


def show_versions():
    lists = [
        ["Vendor", GL_VENDOR],
        ["Renderer", GL_RENDERER],
        ["OpenGL Version", GL_VERSION],
        ["GLSL Version", GL_SHADING_LANGUAGE_VERSION],
    ]
    for x in lists:
        print("%s: %s" % (x[0], glGetString(x[1]).decode("utf-8")))


def main():
    global window, win_w, win_h

    if not glfwInit():
        glfwTerminate()
        return

    win_w, win_h = 1024, 768
    window = glfwCreateWindow(1, 1, "Show Normals Exercise", None, None)
    glfwMakeContextCurrent(window)
    show_versions()

    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowRefreshCallback(window, display)
    glfwSetWindowSizeCallback(window, reshape)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    my_init()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        display(window)
        glfwWaitEvents()
        # glfwPollEvents()
    glfwDestroyWindow(window)
    glfwTerminate()


if __name__ == "__main__":
    main()
