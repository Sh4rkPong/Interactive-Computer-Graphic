import os, sys, time
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
from pywavefront import Wavefront, visualization as vis
from gl_helpers_6710405362 import *

model = Wavefront("../models/bunny.obj")
prog_id = 0
win_w, win_h = 1024, 768

def print_shader_info_log(shader, prompt=""):
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetShaderInfoLog(shader).decode("utf-8")))
        os._exit(1)

def print_program_info_log(shader, prompt=""):
    result = glGetProgramiv(shader, GL_LINK_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetProgramInfoLog(shader).decode("utf-8")))
        os._exit(1)

def create_shaders():
    global prog_id

    vert_code = '''
#version 130
uniform mat4 proj_mat, view_mat, model_mat;
out vec3 smooth_color;
void main()
{
   gl_Position = proj_mat * view_mat * model_mat * gl_Vertex;
   smooth_color = abs(gl_Normal);
}'''
    frag_code = '''
#version 130
in vec3 smooth_color;
void main()
{
   gl_FragColor = vec4(smooth_color, 1);
}'''

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vert_code)
    glShaderSource(frag_id, frag_code)

    glCompileShader(vert_id)
    glCompileShader(frag_id)
    print_shader_info_log(vert_id, "Vertex Shader")
    print_shader_info_log(frag_id, "Fragment Shader")

    prog_id = glCreateProgram()
    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    print_program_info_log(prog_id, "Link error")


arcball_rot = Identity()
dragging = False
last_vec = array((0, 0, 1), dtype=float32)

def project_to_sphere(x, y, w, h):
    """Map a screen-space mouse position (x, y) in pixels to a 3D point on
    (or, once outside the disc, hyperbolically projected onto) the arcball's
    unit sphere. Screen space has y growing downward, so it must be flipped."""
    nx = (2.0*x - w) / w
    ny = (h - 2.0*y) / h
    r2 = nx*nx + ny*ny
    if r2 <= 1.0:
        nz = sqrt(1.0 - r2)
    else:
        s = sqrt(r2)
        nx, ny = nx/s, ny/s
        nz = 0.0
    return normalize(array((nx, ny, nz), dtype=float32))

def mouse_button(window, button, action, mods):
    global dragging, last_vec

    if button == GLFW_MOUSE_BUTTON_LEFT:
        if action == GLFW_PRESS:
            dragging = True
            x, y = glfwGetCursorPos(window)
            last_vec = project_to_sphere(x, y, win_w, win_h)
        elif action == GLFW_RELEASE:
            dragging = False
    glfwPostEmptyEvent()

def cursor_pos(window, x, y):
    global last_vec, arcball_rot

    if not dragging:
        return

    cur_vec = project_to_sphere(x, y, win_w, win_h)

    cosang = dot(last_vec, cur_vec)
    cosang = max(-1.0, min(1.0, cosang))
    angle_rad = acos(cosang)
    axis = cross(last_vec, cur_vec)

    if norm(axis) > 1e-6 and angle_rad > 1e-6:
        angle_deg = angle_rad * 180.0 / pi
        delta = Rotate(angle_deg, axis[0], axis[1], axis[2])
        arcball_rot = dot(delta, arcball_rot)
        last_vec = cur_vec
    glfwPostEmptyEvent()

def scroll(window, xoffset, yoffset):
    global eye_pos

    direction = normalize(eye_pos - centroid)
    dist = norm(eye_pos - centroid)
    dist -= yoffset * 0.1 * dist
    dist = max(0.1, dist)
    eye_pos = centroid + direction * dist
    glfwPostEmptyEvent()


wireframe_on, animation_on = False, True
def keyboard(window, key, scancode, action, mods):
    global wireframe_on, animation_on, arcball_rot

    if action == GLFW_PRESS or action == GLFW_REPEAT:
        if key == GLFW_KEY_SPACE:
            animation_on = not animation_on
        elif key == GLFW_KEY_W:
            wireframe_on = not wireframe_on
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE if wireframe_on else GL_FILL)
        elif key == GLFW_KEY_R:
            arcball_rot = Identity()
        elif key in (GLFW_KEY_ESCAPE, GLFW_KEY_Q):
            glfwSetWindowShouldClose(window, GLFW_TRUE)
        glfwPostEmptyEvent()

def resize(window, w, h):
    global win_w, win_h, proj_mat

    win_w, win_h = w, h
    glViewport(0, 0, w, h)
    proj_mat = Perspective(60, win_w/win_h, 0.01, 10)

def refresh(window):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    view_mat = LookAt(*eye_pos, *centroid, 0, 1, 0)
    model_mat = arcball_rot

    glUseProgram(prog_id)
    proj_loc = glGetUniformLocation(prog_id, "proj_mat")
    view_loc = glGetUniformLocation(prog_id, "view_mat")
    model_loc = glGetUniformLocation(prog_id, "model_mat")

    glUniformMatrix4fv(proj_loc, 1, GL_TRUE, proj_mat)
    glUniformMatrix4fv(view_loc, 1, GL_TRUE, view_mat)
    glUniformMatrix4fv(model_loc, 1, GL_TRUE, model_mat)

    vis.draw(model)
    glfwSwapBuffers(window)

angle = 0
def animation(window):
    global angle

    angle += 1
    glfwPostEmptyEvent()

def init_model():
    global centroid, eye_pos

    glClearColor(0.4, 0.95, 0.95, 1)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)

    centroid = np.array((0, 0, 0))
    eye_pos = centroid + (0, 0, 2.5)

def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(1, 1, "gl_helpers Tester Exercise", None, None)
    glfwMakeContextCurrent(window)
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowSizeCallback(window, resize)
    glfwSetKeyCallback(window, keyboard)
    glfwSetMouseButtonCallback(window, mouse_button)
    glfwSetCursorPosCallback(window, cursor_pos)
    glfwSetScrollCallback(window, scroll)
    glfwSetWindowPos(window, 20, 50)
    glfwSetWindowSize(window, win_w, win_h)

    init_model()
    create_shaders()
    while not glfwWindowShouldClose(window):
        if animation_on:
            animation(window)
        refresh(window)
        glfwWaitEvents()
    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()
