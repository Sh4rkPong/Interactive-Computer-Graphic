import numpy as np

def Perspective(fovy, aspect, zNear, zFar):
    rad = np.radians(fovy)
    tan_half_fovy = np.tan(rad / 2.0)
    res = np.zeros((4, 4), dtype=np.float32)
    res[0, 0] = 1.0 / (aspect * tan_half_fovy)
    res[1, 1] = 1.0 / tan_half_fovy
    res[2, 2] = -(zFar + zNear) / (zFar - zNear)
    res[2, 3] = -(2.0 * zFar * zNear) / (zFar - zNear)
    res[3, 2] = -1.0
    return res

def LookAt(eyeX, eyeY, eyeZ, centerX, centerY, centerZ, upX, upY, upZ):
    eye = np.array([eyeX, eyeY, eyeZ], dtype=np.float32)
    center = np.array([centerX, centerY, centerZ], dtype=np.float32)
    up = np.array([upX, upY, upZ], dtype=np.float32)

    f = center - eye
    f = f / np.linalg.norm(f)
    
    u = up / np.linalg.norm(up)
    s = np.cross(f, u)
    s = s / np.linalg.norm(s)
    u = np.cross(s, f)

    res = np.identity(4, dtype=np.float32)
    res[0, 0:3] = s
    res[1, 0:3] = u
    res[2, 0:3] = -f
    res[0, 3] = -np.dot(s, eye)
    res[1, 3] = -np.dot(u, eye)
    res[2, 3] = np.dot(f, eye)
    return res

def Rotate(angle, x, y, z):
    rad = np.radians(angle)
    c = np.cos(rad)
    s = np.sin(rad)
    axis = np.array([x, y, z], dtype=np.float32)
    norm = np.linalg.norm(axis)
    if norm == 0:
        return np.identity(4, dtype=np.float32)
    axis = axis / norm
    
    x, y, z = axis
    res = np.identity(4, dtype=np.float32)
    
    res[0, 0] = c + x * x * (1 - c)
    res[0, 1] = x * y * (1 - c) - z * s
    res[0, 2] = x * z * (1 - c) + y * s
    
    res[1, 0] = y * x * (1 - c) + z * s
    res[1, 1] = c + y * y * (1 - c)
    res[1, 2] = y * z * (1 - c) - x * s
    
    res[2, 0] = z * x * (1 - c) - y * s
    res[2, 1] = z * y * (1 - c) + x * s
    res[2, 2] = c + z * z * (1 - c)
    
    return res