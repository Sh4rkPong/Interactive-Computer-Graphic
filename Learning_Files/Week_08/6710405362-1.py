from OpenGL.GL import *
from OpenGL.GLU import *
from glfw.GLFW import *
from pywavefront import Wavefront, visualization as vis

model = Wavefront("../models/teapot.obj")
prog_id = 0
win_w, win_h = 800, 600

def printShaderInfoLog(shader, prompt=""):
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetShaderInfoLog(shader).decode("utf-8")))

def printProgramInfoLog(program, prompt=""):
    result = glGetProgramiv(program, GL_LINK_STATUS)
    if not result:
        print("%s: %s" % (prompt, glGetProgramInfoLog(program).decode("utf-8")))
        exit()

def compileProgram(vertex_code, fragment_code):
    prog_id = glCreateProgram()

    vert_id = glCreateShader(GL_VERTEX_SHADER)
    frag_id = glCreateShader(GL_FRAGMENT_SHADER)

    glShaderSource(vert_id, vertex_code)
    glShaderSource(frag_id, fragment_code)

    glCompileShader(vert_id)
    printShaderInfoLog(vert_id, "Vertex Shader Error")

    glCompileShader(frag_id)
    printShaderInfoLog(frag_id, "Fragment Shader Error")

    glAttachShader(prog_id, vert_id)
    glAttachShader(prog_id, frag_id)

    glLinkProgram(prog_id)
    printProgramInfoLog(prog_id, "Link Program Error")

    return prog_id

def gl_init():
    global prog_id

    glViewport(0, 0, win_w, win_h)
    glEnable(GL_DEPTH_TEST)

    vert_code = '''
#version 120
varying vec3 v_color;

void main()
{
    vec3 n = normalize(gl_NormalMatrix * gl_Normal);
    v_color = 0.5 * (n + vec3(1.0));

    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
'''
    frag_code = '''
#version 120
varying vec3 v_color;

void main()
{
    gl_FragColor = vec4(v_color, 1.0);
}
'''
    prog_id = compileProgram(vert_code, frag_code)

def refresh(window):
    glClear(int(GL_COLOR_BUFFER_BIT) | int(GL_DEPTH_BUFFER_BIT))

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, win_w/win_h, 0.01, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0.5, 2, 0, 0.5, 0, 0, 1, 0)

    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    vis.draw(model)
    glfwSwapBuffers(window)

    glUseProgram(0)


def main():
    global window

    if not glfwInit():
        glfwTerminate()
        return

    window = glfwCreateWindow(win_w, win_h, "GLSL Shaders Exercise", None, None)
    if not window:
        glfwTerminate()
        return

    glfwMakeContextCurrent(window)
    glfwSetWindowRefreshCallback(window, refresh)
    glfwSetWindowPos(window, 20, 50)

    gl_init()
    while not glfwWindowShouldClose(window):
        refresh(window)
        glfwPollEvents()

    glfwDestroyWindow(window)
    glfwTerminate()

if __name__ == "__main__":
    main()
