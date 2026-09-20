import sys

import glfw
from OpenGL import GL


# reshape หน้าต่าง
def resize(window, w, h):
    GL.glViewport(0, 0, w, h)

def refresh(window):
    GL.glClearColor(1.0, 1.0, 0.5, 1.0)
    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glColor3f(1.0, 1.0, 1.0)

    GL.glBegin(GL.GL_POLYGON) # การเพิ่มรูปทรงเลขาคณิต -> หลายเหลี่ยม
    GL.glVertex3f(-0.5, -0.5, 0.0)
    GL.glVertex3f(0.5, -0.5, 0.0)
    GL.glVertex3f(0.0, 0.5, 0.0)
    GL.glVertex3f(-0.5, 0.5, 0.0)

    GL.glEnd()
    GL.glFlush()


if not glfw.init():
    sys.exit("Cannot initialize GLFW")

glfw.window_hint(glfw.DOUBLEBUFFER, glfw.TRUE)
window = glfw.create_window(800, 600, "GLFW Code Sample", None, None)
glfw.set_window_refresh_callback(window, refresh)
glfw.set_window_size_callback(window, resize) # function callback reshape

if not window:
    glfw.terminate()
    sys.exit("Cannot create the GLFW window")

glfw.make_context_current(window)

while not glfw.window_should_close(window):
    refresh(window)
    glfw.swap_buffers(window)
    glfw.poll_events()

glfw.destroy_window(window)
glfw.terminate()
