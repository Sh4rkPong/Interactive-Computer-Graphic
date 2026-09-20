import sys

import numpy as np
import pandas as pd
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *


def display(window):
    # [Depth Buffering] เคลียร์ทั้งสองบัฟเฟอร์
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        # [โจทย์กำหนด] เปลี่ยนมาใช้ค่า 0.5 * (normals + 1)
        color_val = 0.5 * (normals[i] + 1.0)
        glColor3fv(color_val)
        glVertex3fv(positions[i])
    glEnd()

    # [Double Buffering] เปลี่ยนมาใช้ glfwSwapBuffers
    glfwSwapBuffers(window)


def reshape(window, w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()


def animation(window):
    glRotatef(1, 0, 1, 0)
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
        elif key == GLFW_KEY_Q:
            glfwSetWindowShouldClose(window, GLFW_TRUE)
    glfwPostEmptyEvent()


def my_init():
    global n_vertices, positions, colors, normals, uvs

    df = pd.read_csv(
        "../models/monkey.tri", sep="\s+", comment="#", header=None, dtype=np.float32
    )
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    positions = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals = df.values[:, 6:9]
    uvs = df.values[:, 9:11]
    n_vertices = len(positions)
    print("no. of vertices: %d, no. of triangles: %d" % (n_vertices, n_vertices // 3))


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
    global window

    if not glfwInit():
        glfwTerminate()
        return

    # [Double Buffering] เปลี่ยนเป็น GL_TRUE
    glfwWindowHint(GLFW_DOUBLEBUFFER, GL_TRUE)
    window = glfwCreateWindow(
        800, 800, "Double & Depth Framebuffer Exercise", None, None
    )
    glfwMakeContextCurrent(window)
    show_versions()

    # [Depth Buffering] เปิดใช้งาน Depth Test
    glEnable(GL_DEPTH_TEST)

    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowRefreshCallback(window, display)
    glfwSetWindowSizeCallback(window, reshape)

    my_init()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        display(window)
        glfwPollEvents()

    glfwDestroyWindow(window)
    glfwTerminate()


if __name__ == "__main__":
    main()
