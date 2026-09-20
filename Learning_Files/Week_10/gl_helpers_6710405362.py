from numpy import array, ndarray, zeros, dot, cross, float32, identity
from numpy.linalg import norm
from math import sqrt, sin, cos, tan, acos, pi

def Identity():
    return array(((1, 0, 0, 0),
                  (0, 1, 0, 0),
                  (0, 0, 1, 0),
                  (0, 0, 0, 1)), dtype=float32)

def normalize(v, eps=1e-5):
    l = norm(v)
    if l == 0:
        return v
    else:
        return v/l

def Translate(tx, ty, tz):
    return array(((1, 0, 0, tx),
                  (0, 1, 0, ty),
                  (0, 0, 1, tz),
                  (0, 0, 0, 1)), dtype=float32)

def Scale(sx, sy, sz):
    return array(((sx, 0,  0,  0),
                  (0,  sy, 0,  0),
                  (0,  0,  sz, 0),
                  (0,  0,  0,  1)), dtype=float32)

def Rotate(angle, x, y, z):
    axis = array((x, y, z), dtype=float32)
    axis = normalize(axis)
    x, y, z = axis[0], axis[1], axis[2]

    rad = angle * pi / 180.0
    c = cos(rad)
    s = sin(rad)
    t = 1.0 - c

    return array(((t*x*x + c,   t*x*y - s*z, t*x*z + s*y, 0),
                  (t*x*y + s*z, t*y*y + c,   t*y*z - s*x, 0),
                  (t*x*z - s*y, t*y*z + s*x, t*z*z + c,   0),
                  (0,           0,           0,           1)), dtype=float32)

def LookAt(eyex, eyey, eyez, atx, aty, atz, upx, upy, upz):
    eye = array((eyex, eyey, eyez), dtype=float32)
    at  = array((atx, aty, atz), dtype=float32)
    up  = array((upx, upy, upz), dtype=float32)

    f = normalize(at - eye)
    upN = normalize(up)
    s = normalize(cross(f, upN))
    u = cross(s, f)

    R = array(((s[0], s[1], s[2], 0),
               (u[0], u[1], u[2], 0),
               (-f[0], -f[1], -f[2], 0),
               (0,     0,     0,    1)), dtype=float32)

    T = Translate(-eyex, -eyey, -eyez)
    return dot(R, T)

def Perspective(fovy, aspect, zNear, zFar):
    f = 1.0 / tan((fovy * pi / 180.0) / 2.0)

    return array(((f/aspect, 0, 0,                                 0),
                  (0,        f, 0,                                 0),
                  (0,        0, (zFar+zNear)/(zNear-zFar),         (2*zFar*zNear)/(zNear-zFar)),
                  (0,        0, -1,                                0)), dtype=float32)

def Frustum(left, right, bottom, top, near, far):
    A = (right + left) / (right - left)
    B = (top + bottom) / (top - bottom)
    C = -(far + near) / (far - near)
    D = -(2 * far * near) / (far - near)

    return array(((2*near/(right-left), 0,                    A,  0),
                  (0,                    2*near/(top-bottom),  B,  0),
                  (0,                    0,                    C,  D),
                  (0,                    0,                    -1, 0)), dtype=float32)

def Ortho(left, right, bottom, top, near, far):
    tx = -(right + left) / (right - left)
    ty = -(top + bottom) / (top - bottom)
    tz = -(far + near) / (far - near)

    return array(((2/(right-left), 0,               0,               tx),
                  (0,               2/(top-bottom),  0,               ty),
                  (0,               0,               -2/(far-near),   tz),
                  (0,               0,               0,               1)), dtype=float32)
