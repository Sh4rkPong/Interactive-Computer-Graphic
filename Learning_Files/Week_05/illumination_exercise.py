#bullet-1
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
import numpy as np
import pandas as pd
import time

win_w, win_h = 1024, 768


def resize(window, w, h):
    global win_w, win_h

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w / win_h, 0.01, 30)


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


ticks, frame_cnt = 0, 0


def animation(window):
    global ticks, frame_cnt

    ticks += 1
    frame_cnt += 1
    glfwPostEmptyEvent()


def normalize(v):
    v = np.asarray(v, dtype=np.float32)
    n = np.linalg.norm(v)
    if n == 0.0:
        return v
    return v / n


def phong_lighting(P, N, eye_pos, light_pos, ka, kd, ks, ia, il, shininess):
    P = np.asarray(P, dtype=np.float32)
    N = normalize(N)
    eye_pos = np.asarray(eye_pos, dtype=np.float32)
    light_pos = np.asarray(light_pos, dtype=np.float32)

    L = normalize(light_pos - P)
    V = normalize(eye_pos - P)

    ambient = ka * ia

    ndotl = max(float(np.dot(N, L)), 0.0)
    diffuse = kd * il * ndotl

    if ndotl > 0.0:
        R = normalize(2.0 * ndotl * N - L)
        rdotv = max(float(np.dot(R, V)), 0.0)
        specular = ks * il * (rdotv ** shininess)
    else:
        specular = np.zeros(3, dtype=np.float32)

    color = ambient + diffuse + specular
    return np.clip(color, 0.0, 1.0)


EYE_POS = np.array((0.0, 3.0, 3.0), dtype=np.float32)
LIGHT_POS = np.array((3.0, 4.0, 20.0), dtype=np.float32)

KA = np.array((0.1, 0.1, 0.1), dtype=np.float32)
KD = np.array((1.0, 0.0, 0.0), dtype=np.float32)
KS = np.array((1.0, 1.0, 0.0), dtype=np.float32)
IA = np.array((1.0, 1.0, 1.0), dtype=np.float32)
IL = np.array((1.0, 1.0, 1.0), dtype=np.float32)
SHININESS = 50


def refresh(window):
    global start_time, frame_cnt
    if frame_cnt == 20:
        print("%.2f fps" % (frame_cnt / (time.time() - start_time)), ticks, end='\r')
        start_time = time.time()
        frame_cnt = 0

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(
        EYE_POS[0], EYE_POS[1], EYE_POS[2],
        centroid[0], centroid[1], centroid[2],
        0, 1, 0
    )

    for i in range(n_vertices):
        colors[i] = phong_lighting(
            positions[i],
            normals[i],
            EYE_POS,
            LIGHT_POS,
            KA, KD, KS,
            IA, IL,
            SHININESS,
        )

    glBegin(GL_TRIANGLES)
    for i in range(n_vertices):
        glColor3fv(colors[i])
        glVertex3fv(positions[i])
    glEnd()

    glfwSwapBuffers(window)


def gl_init_models():
    global start_time
    global n_vertices, positions, colors, normals, uvs, centroid, bbox

    glClearColor(0, 0, 0, 0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    df = pd.read_csv(
        "../models/bunny_uv.tri",
        sep='\s+',
        comment='#',
        header=None,
        dtype=np.float32,
    )

    values = df.values.astype(np.float32)
    centroid = values[:, 0:3].mean(axis=0)
    bbox = values[:, 0:3].max(axis=0) - values[:, 0:3].min(axis=0)

    n_vertices = len(values)
    positions = values[:, 0:3].copy()
    normals = values[:, 6:9].copy()
    uvs = values[:, 9:11].copy()
    colors = np.zeros((n_vertices, 3), dtype=np.float32)

    start_time = time.time() - 0.0001


def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "Illumination Exercise", None, None)
    glfwMakeContextCurrent(window)
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    gl_init_models()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        refresh(window)
        glfwWaitEvents()

    glfwDestroyWindow(window)
    glfwTerminate()


if __name__ == "__main__":
    main()
