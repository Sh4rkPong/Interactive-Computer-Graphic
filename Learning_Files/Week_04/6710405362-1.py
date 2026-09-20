# Client Side Code
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import time, math as m

win_w, win_h = 1024, 766
bunny = 18

def resize(window, w, h):
    global win_w, win_h
    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w/win_h, 0.01, 50)

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

ticks = 0
def animation(window):
    global ticks
    ticks += 1

def get_color(i, total):
    hue = (i / total) * 2.0 * m.pi
    r = (m.sin(hue) + 1.0) / 2.0
    g = (m.sin(hue + 2.0 * m.pi / 3.0) + 1.0) / 2.0
    b = (m.sin(hue + 4.0 * m.pi / 3.0) + 1.0) / 2.0
    return np.array((r, g, b), dtype=np.float32)

def refresh(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    eye_pos = centroid + (0, 15, 10 * max(bbox))
    gluLookAt(*eye_pos, *centroid, 0, 1, 0)

    glRotatef(ticks, 0, 1, 0)

    glEnableClientState(GL_VERTEX_ARRAY)
    glEnableClientState(GL_COLOR_ARRAY)
    glEnableClientState(GL_NORMAL_ARRAY)

    glVertexPointer(3, GL_FLOAT, 0, positions)
    glColorPointer(3, GL_FLOAT, 0, colors)
    glNormalPointer(GL_FLOAT, 0, normals)

    radius = max(bbox) * 4.5

    for i in range(bunny):
        angle = (i / bunny) * 2.0 * m.pi
        x_off = radius * m.cos(angle)
        z_off = radius * m.sin(angle)

        Kd = get_color(i, bunny)
        colors[:, :] = Kd

        glPushMatrix()
        glTranslatef(x_off, 0, z_off)
        glRotatef(ticks - (i * (360.0 / bunny)) + 90, 0, 1, 0)
        glTranslatef(*(-centroid))
        glDrawArrays(GL_TRIANGLES, 0, n_vertices)
        glPopMatrix()

    glDisableClientState(GL_VERTEX_ARRAY)
    glDisableClientState(GL_COLOR_ARRAY)
    glDisableClientState(GL_NORMAL_ARRAY)
    glfwSwapBuffers(window)

def gl_init_models():
    global n_vertices, positions, colors, normals, uvs, centroid, bbox

    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    df = pd.read_csv("../models/bunny_uv.tri", sep=r'\s+',
                     comment='#', header=None, dtype=np.float32)
    centroid = df.values[:, 0:3].mean(axis=0)
    bbox = df.values[:, 0:3].max(axis=0) - df.values[:, 0:3].min(axis=0)

    n_vertices = len(df.values)
    positions = np.ones((n_vertices, 3), np.float32)
    normals = np.zeros((n_vertices, 3), np.float32)
    positions[:, 0:3] = df.values[:, 0:3]
    colors = df.values[:, 3:6]
    normals[:, 0:3] = df.values[:, 6:9]
    uvs = df.values[:, 9:11]

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Client-side Vertex Arrays", None, None)
    glfwMakeContextCurrent(window)
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    gl_init_models()

    frame_count = 0
    prev_time = glfwGetTime()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        refresh(window)
        frame_count += 1
        curr_time = glfwGetTime()
        if curr_time - prev_time >= 1.0:
            fps = frame_count / (curr_time - prev_time)
            glfwSetWindowTitle(window, f"Client-side Vertex Arrays | {fps:.1f} fps")
            frame_count = 0
            prev_time = curr_time
        glfwPollEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()
