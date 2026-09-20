## **Chapter 2 Basic Rendering with OpenGL Interactive Computer Graphics** 



<!-- Start of picture text -->
Basic Rendering with OpenGL<br><!-- End of picture text -->



<!-- Start of picture text -->
Interactive Computer Graphics<br><!-- End of picture text -->

**Chakrit Watcharopas** 

### **Outline** 



<!-- Start of picture text -->
PyOpenGL<br><!-- End of picture text -->

- OpenGL and PyOpenGL 

- GLFW 



<!-- Start of picture text -->
OpenGL<br><!-- End of picture text -->

- Primitives in OpenGL 

- Face Culling 



<!-- Start of picture text -->
How to handle when window size is changed<br><!-- End of picture text -->

- How to handle when window size is changed 

2 

### **O enGL** **<u>p</u>** 

- Application Programming Interface (API) used for rendering 2D and 3D scene 

- Primitive Geometry in OpenGL: point, line, triangle, polygon 

- 

- OpenGL is designed to be platform independent 



<!-- Start of picture text -->
OpenGL takes advantage of hardware acceleration and GPU to improve<br><!-- End of picture text -->

- OpenGL takes advantage of hardware acceleration and GPU to improve graphics performance 

- OpenGL renders a scene to framebuffer 



<!-- Start of picture text -->
- -<br>accelerated capabilities enable interactive, real<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>time<br><!-- End of picture text -->

- - 

- OpenGL's hardware accelerated capabilities enable interactive, real time rendering 



<!-- Start of picture text -->
Microsoft's Direct3D, akin to OpenGL, is a graphics API, an alternative option<br><!-- End of picture text -->

- Microsoft's Direct3D, akin to OpenGL, is a graphics API, an alternative option for developers 



<!-- Start of picture text -->
for developers<br><!-- End of picture text -->

3 

### **What O enGL won’t do?** **<u>p</u>** 

- 

- OpenGL does not provide built in management for framebuffers 

   - developers need to create framebuffer for OpenGL 

- No window management 



<!-- Start of picture text -->
-<br>in support for user interaction, such as handling<br><!-- End of picture text -->

- 

- Does not include built in support for user interaction, such as handling mouse input and keyboard input 

- Render only simple primitives like points, lines, and triangles 



<!-- Start of picture text -->
developers are responsible for rendering complex model (horse, teapot, bunny)<br><!-- End of picture text -->

- developers are responsible for rendering complex model (horse, teapot, bunny) 

4 

### **GLFW (OpenGL Framework)** 

- Graphics Library Framework for managing user interaction and window management in OpenGL applications 

- Handles user interaction 

- Manages windows 

- Does not provide GUI Widgets 

   - we will use ImGUI to create GUI Widgets 



<!-- Start of picture text -->
-<br>Facilitates event<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>driven programming<br><!-- End of picture text -->

- 

- Facilitates event driven programming 

5 

### **GLFW Code Sam le** **<u>p</u>** 

```
1ifnotglfwInit():
2glfwTerminate()
3exit()
4
```

```
5glfwWindowHint(GLFW_DOUBLEBUFFER, GL_FALSE)
""
6window = glfwCreateWindow(800, 600, GLFW Code Sample, None, None)
7glfwMakeContextCurrent(window)
8glfwSetWindowRefreshCallback(window, refresh)
9
```

```
10whilenotglfwWindowShouldClose(window):
11refresh(window)
12glfwWaitEvents()  # or glfwPollEvents()
13glfwDestroyWindow(window)
14glfwTerminate()
```

6 



<!-- Start of picture text -->
Exam le of Refresh Callback Function<br>p<br><!-- End of picture text -->

|**Exa**|**mple of Refresh Callback Function**|
|---|---|
|`def `<br>`1`|`refresh(window):`<br>|
|`2`<br>`3`<br>`4`|`glClearColor(1, 1, 0.5, 0)`<br>`glClear(GL_COLOR_BUFFER_BIT)`<br>`glColor3f(0, 1, 0)`|
|`5`|`glBegin(GL_TRIANGLES)`|
|`6`<br>`7`|`glVertex3f(-0.5, -0.5, 0)`<br>`glVertex3f( 0.5, -0.5, 0)`<br>OpenGL Code|
|`8`<br>`9`|`glVertex3f( 0, 0.5, 0)`<br>`glEnd()`|
|`10`|`glFlush()`|





7 

#### <u>Explain code each line</u> 

O giClearColor(1, 1, 0.5, 0) O sets the color used to clear the color buffer O Red: 1, Green: 1, Blue: 0.5, 



<!-- Start of picture text -->
(1, 0, 0) Red LLAN<br>(0, 1, 0) Green | 1%<br>(0, 0, 1) Blue hau<br>(1, 1, 0) Yellow | iwaas<br>(1, 0, 1) Magenta | ww<br>(0, 1, 1) Cyan WW<br>(0, 0, 0) Black an<br>(1, 1, 1) White | 97 C)<br><!-- End of picture text -->



### **Ex lain code each line** **<u>p</u>** 

- glClear(GL_COLOR_BUFFER_BIT) 



<!-- Start of picture text -->
clears the color buffer of the currently bound framebuffer with the color specified<br><!-- End of picture text -->

   - clears the color buffer of the currently bound framebuffer with the color specified by glClearColor 

- 3 0 1 0 

- glColor f( , , ) 

   - sets the current color for next rendering objects 

- Begin(GL_POLYGON) 



<!-- Start of picture text -->
specifies the beginning of a sequence of vertices that define a polygon primitive<br><!-- End of picture text -->

- specifies the beginning of a sequence of vertices that define a polygon primitive 

9 

### **Ex lain code each line** **<u>p</u>** 

- glVertex3f(x, y, z) 



<!-- Start of picture text -->
specifies a vertex coordinate (x, y, z) in 3D space<br><!-- End of picture text -->

######  specifies a vertex coordinate (x, y, z) in 3D space 

#####  glEnd() 



<!-- Start of picture text -->
marks the end of a sequence of vertex data defining a geometric primitive<br><!-- End of picture text -->

- marks the end of a sequence of vertex data defining a geometric primitive 

#####  glFlush() 



<!-- Start of picture text -->
ensures all previously issued OpenGL commands are executed by the rendering<br><!-- End of picture text -->

- ensures all previously issued OpenGL commands are executed by the rendering pipeline 



<!-- Start of picture text -->
pipeline<br><!-- End of picture text -->

10 

### **Some O enGL Command S ntax** **<u>p y</u>** 

- Begins with the letter "gl" 

- Then followed by command names, e.g. Vertex, Color, etc. 



<!-- Start of picture text -->
Suffixes of the command provide information about arguments passed to the<br>function, e.g.<br><!-- End of picture text -->

- Suffixes of the command provide information about arguments passed to the function, e.g. 



<!-- Start of picture text -->
3f denotes the function expects three parameters of float<br><br><!-- End of picture text -->

- 3f denotes the function expects three parameters of float 

   - glVertex3f(1.0, 3.0, 4.0); 



<!-- Start of picture text -->
2i denotes the function expects two parameters of int<br>-<br><br><!-- End of picture text -->

- 2i denotes the function expects two parameters of int 

   - 

   - glVertex2i( 1, 5); 



<!-- Start of picture text -->
-<br>3fv indicates the function expects a pointer to an array of three floating<br><br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>point values<br><!-- End of picture text -->

- 

- 3fv indicates the function expects a pointer to an array of three floating point values 

 Example in C float colorArray[] = {1.0f, 0.0f, 0.0f}; glColor3fv(colorArray); 



<!-- Start of picture text -->
Example in Python (can use tuple or list as an argument)<br><!-- End of picture text -->

- Example in Python (can use tuple or list as an argument) 

   - q = [1.5, 2.5, 3.0] glVertex3fv(q) 



<!-- Start of picture text -->
glVertex3fv(q)<br><!-- End of picture text -->

11 

### <u>Command Suffixes</u> and <u>Argument Data Types</u> 

Suffix Data Type Typical OpenGL Type Definition Corresponding C-Language Type b 8-bit integer signed char GLbyte S 16-bit integer signed short GLshort i 32-bit integer int GLint, GLsizei f 32-bit floating-point float GLfloat, GLclampf d 64-bit floating-point double GLdouble, GLclampd ub 8-bit unsigned integer unsigned char GLubyte us 16-bit unsigned integer unsigned short GLushort ui 32-bit unsigned integer unsigned int GLuint, GLenum, GLbitfield 



<!-- Start of picture text -->
Source: OpenGL Programming Guide 8th OpenGL Programming Guide 8th Programming Guide 8th Guide 8th 8th Edition “OC<br><!-- End of picture text -->

Source: OpenGL Programming Guide 8th OpenGL Programming Guide 8th Programming Guide 8th Guide 8th 8th Edition “OC 



<!-- Start of picture text -->
O enGL is<br>p<br><!-- End of picture text -->



<!-- Start of picture text -->
State Machine<br><!-- End of picture text -->

### **O enGL is State Machine** **<u>p</u>** 

- In OpenGL, "state" specifically refers to various settings and parameters that control the behavior of the rendering pipeline 



<!-- Start of picture text -->
"machine" refers to transitions between different states based on inputs<br>or commands<br><!-- End of picture text -->

- "machine" refers to transitions between different states based on inputs or commands 



<!-- Start of picture text -->
Once a state is set, it remains in effect until explicitly changed by<br><!-- End of picture text -->

- Once a state is set, it remains in effect until explicitly changed by another OpenGL command 

- Example of States 

   - clear color state is set by glClearColor() 



<!-- Start of picture text -->
*()<br><!-- End of picture text -->

- current color state is set by glColor*() 



<!-- Start of picture text -->
transformation matrix state<br><!-- End of picture text -->

- transformation matrix state 

13 

### **How to check O enGL Version** **<u>p</u>** 

```
lists = [['Vendor', GL_VENDOR],
['Renderer',GL_RENDERER],
['OpenGL Version', GL_VERSION],
['GLSL Version', GL_SHADING_LANGUAGE_VERSION]]
for x in lists:
print('{0}: {1}'.format(
-
x[0],glGetString(x[1]).decode("utf8")))")))
```





<!-- Start of picture text -->
['GLSL Version', GL_SHADING_LANGUAGE_VERSION]]<br><!-- End of picture text -->





<!-- Start of picture text -->
-<br>(x[1]).decode("utf1]).decode("utf]).decode("utf<br><!-- End of picture text -->



<!-- Start of picture text -->
8")))")))<br><!-- End of picture text -->

14 

### Geometric Primitives in OpenGL 

### **Geometric Primitives in O enGL** **<u>p</u>** 



<!-- Start of picture text -->
can draw simple primitives<br><!-- End of picture text -->

 OpenGL can draw simple primitives 

   - point 

   - straight line 

   - triangle and polygon 

- No basic primitives that are curves or curved surfaces 



<!-- Start of picture text -->
We can draw curves by drawing short straight lines in succession<br><!-- End of picture text -->

- We can draw curves by drawing short straight lines in succession 



16 

### **How to Draw Geometric Primitive** 

- Start with glBegin(type of primitives) 



<!-- Start of picture text -->
* to specify the vertices of that primitive<br><!-- End of picture text -->

- Then use glVertex* to specify the vertices of that primitive 

- End with glEnd() 

- Example of code 

```
glBegin(GL_POLYGON)
--
glVertex3f(0.5, 0.5, 0.0)
-
glVertex3f( 0.5, 0.5, 0.0)
glVertex3f( 0.5,  0.5, 0.0)
-
glVertex3f(0.5,  0.5, 0.0)
glEnd()()
```



<!-- Start of picture text -->
-<br>0.5,  0.5, 0.0)<br><!-- End of picture text -->



<!-- Start of picture text -->
glEnd()()<br><!-- End of picture text -->

17 



<!-- Start of picture text -->
Geometric.. Primitivesaa ] > ]inin<br><!-- End of picture text -->



<!-- Start of picture text -->
OpenGL<br><!-- End of picture text -->

<u>Geometric.. Primitivesaa</u> ] > ]inin <u>OpenGL</u> 



<!-- Start of picture text -->
Voe Voe Vye<br>Vie Vae Vse<br><!-- End of picture text -->



<!-- Start of picture text -->
Vi V Vs<br>Wn, 7 Vo wo NT<br>Veee,Vs VaV3 Vy V; Vo<br>Vs Va Va<br>>.V3 VoVANINV2 V4 ve<br>Ne Vy V3 Vs V;<br>[|_GL_TRIANGLES | | GL_TRIANGLE_FAN |<br>Ve Vo Ve "A Ve<br>4 2<br><!-- End of picture text -->



### **lColor** **<u>g</u>** 



<!-- Start of picture text -->
sets the current color state for rendering subsequent primitives, such as<br><!-- End of picture text -->

- sets the current color state for rendering subsequent primitives, such as points, lines, or polygons 

- Full command syntax 

   - glColor[34][fd][v](colors) 

- Example of glColor4f(r, g, b, a) 

   - where r, g, b, a represent values of red, green, blue, and alpha (transparency) 

      - e.g., glColor4d(1.0, 1.0, 0.0, 0.4) sets current color to yellow with 40% opacity 

- Note: Though we set the alpha value for a color, OpenGL won't utilize it for opacity (or transparency) unless alpha blending is enabled explicitly 



<!-- Start of picture text -->
for opacity (or transparency) unless alpha blending is enabled explicitly<br><!-- End of picture text -->

19 

O 



<!-- Start of picture text -->
A<br><!-- End of picture text -->











<!-- Start of picture text -->
a oor vos a iI ee ES ‘+ a<br><!-- End of picture text -->























OO) 



























<!-- Start of picture text -->
Drawing Polygon in OpenGL<br><!-- End of picture text -->

<u>Drawing Polygon in OpenGL</u> O OpenGL guarantees it can accurately draw polygons whose vertices are all on the same plane O If not, the result may not be as intended O Observation: every point that lies on the triangle is on the same plane O But this is not always true for rectangles or other polygons 



<!-- Start of picture text -->
OpenGL guarantees it can accurately draw polygons whose vertices are<br><!-- End of picture text -->



<!-- Start of picture text -->
But this is not always true for rectangles or other polygons<br><!-- End of picture text -->

PEEP EP i CeCe _—_ CCC EC CECE Hun 



C) 



<!-- Start of picture text -->
Drawing Polygon in OpenGL<br><!-- End of picture text -->

<u>Drawing Polygon in OpenGL</u> O Polygons drawn using glBegin(GL_POLYGON) must have the following properties: 



<!-- Start of picture text -->
must have the following<br><!-- End of picture text -->

O their edges must not intersect O they must be convex polygons O they must not have holes 



<!-- Start of picture text -->
they must not have holes<br><!-- End of picture text -->





<!-- Start of picture text -->
Convex<br>Polygon<br><!-- End of picture text -->



<!-- Start of picture text -->
a<br>(sUvariewasayy)<br><!-- End of picture text -->



Convex a <u>Polygon (sUvariewasayy)</u> O For any two points within a polygon, whena straight line connecting those two points is drawn, that line segment must also lie within the polygon O Note: triangles are always convex 



<!-- Start of picture text -->
those two points is drawn, that line segment must also lie within the<br><!-- End of picture text -->



<!-- Start of picture text -->
triangles are always convex<br><!-- End of picture text -->





<!-- Start of picture text -->
Solution for Drawing Concave Polygon in OpenGL<br><!-- End of picture text -->

Solution for Drawing Concave Polygon in OpenGL O Then, how do we draw polygons that are not convex? O Divide those polygons into multiple triangles 



<!-- Start of picture text -->
Divide those polygons into multiple triangles<br><!-- End of picture text -->







### **lCullFace** **<u>g</u>** 

- glCullFace(mode) sets the polygon culling mode 

   - mode can take three values 

      - GL_FRONT = do not draw the front faces 

      - GL_BACK = do not draw the back faces 

      - GL_FRONT_AND_BACK = do not draw both side 

- Do not call this command between glBegin(...) and glEnd() 



<!-- Start of picture text -->
Culling takes effect only when glEnable(GL_CULL_FACE) is called<br>beforehand<br><!-- End of picture text -->



<!-- Start of picture text -->
glEnable(GL_CULL_FACE) is called<br><!-- End of picture text -->



<!-- Start of picture text -->
(GL_CULL_FACE) is called<br><!-- End of picture text -->

- Culling takes effect only when glEnable(GL_CULL_FACE) is called beforehand 



<!-- Start of picture text -->
Disable culling (draw all sides) by calling glDisable(GL_CULL_FACE)<br><!-- End of picture text -->



<!-- Start of picture text -->
glDisable(GL_CULL_FACE)<br><!-- End of picture text -->



<!-- Start of picture text -->
(GL_CULL_FACE)<br><!-- End of picture text -->

- Disable culling (draw all sides) by calling glDisable(GL_CULL_FACE) 

28 

### **How to determine Front Face** 

- Normally, for polygons where we see the vertices arranged in a - 

- clockwise direction, they are considered "front facing“ 

- Conversely, if we see the vertices arranged in a counterclockwise - 

- direction, they are considered "back facing“ 

- However, we can change this using glFrontFace(…) 

   - glFrontFace(GL_CCW) specifies counterclockwise as the front face 



<!-- Start of picture text -->
glFrontFace(GL_CW) specifies clockwise as the front face<br><!-- End of picture text -->



<!-- Start of picture text -->
(GL_CW) specifies clockwise as the front face<br><!-- End of picture text -->

- glFrontFace(GL_CW) specifies clockwise as the front face 

29 

### **Demo** 





<!-- Start of picture text -->
glBegin(GL_QUADS)<br><!-- End of picture text -->



<!-- Start of picture text -->
(GL_QUADS)<br><!-- End of picture text -->



```
glBegin(GL_QUADS)
```

```
glColor3f(1.0, 0.5, 0.5)
--
glVertex2f(0.9, 0.4)
--
glVertex2f(0.1, 0.4)
-
glVertex2f(0.1,  0.4)
-
glVertex2f(0.9,  0.4)
glColor3f(0.5, 1.0, 0.5)
-
glVertex2f(0.1, 0.4)
glVertex2f(0.1,  0.4)
glVertex2f(0.9,  0.4)
-
glVertex2f(0.9, 0.4)
glEnd()
```



<!-- Start of picture text -->
glVertex2f(<br><!-- End of picture text -->





<!-- Start of picture text -->
()<br><!-- End of picture text -->

30 

### How to handle when a window is resized 





(ii <mark>us»</mark> 

C) 



### **Default Vertex Coordinate Ran e on Window** **<u>g</u>** 

- In OpenGL, when drawing vertices to the window, the default coordinate range often follows conventions of normalized device coordinates (NDC) 

- 

- In NDC, the coordinate range typically spans from 1.0 to 1.0 along each axis: 

- -  X axis: The left edge of the window is usually mapped to 1.0, while the right edge is mapped to 1.0 - -  Y axis: The bottom edge of the window is often mapped to 1.0, and the top edge is mapped to 1.0 - -  Z axis: The depth range usually extends from 1.0 (near plane) to 1.0 (far plane) 



<!-- Start of picture text -->
The default viewport mapping in OpenGL refers to how the NDC space is mapped to<br>the window or framebuffer<br><!-- End of picture text -->

- The default viewport mapping in OpenGL refers to how the NDC space is mapped to the window or framebuffer 



<!-- Start of picture text -->
By default, OpenGL sets up a viewport that matches the dimensions of the window or<br>framebuffer<br><!-- End of picture text -->

- By default, OpenGL sets up a viewport that matches the dimensions of the window or framebuffer 

- - - 

- The point ( 1.0, 1.0) in NDC maps to the bottom left corner of the window. 



<!-- Start of picture text -->
-<br>The point (1.0, 1.0) in NDC maps to the top<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>right corner of the window.<br><!-- End of picture text -->

- 

- The point (1.0, 1.0) in NDC maps to the top right corner of the window. 

33 

### **lfwSetWindowSizeCallback** **<u>g</u>** 

- glfwSetWindowSizeCallback(window, resize_callback) 



<!-- Start of picture text -->
glfwSetWindowSizeCallback<br><!-- End of picture text -->



- A resize callback function provided to glfwSetWindowSizeCallback must be defined as follows: 

- def <function_name>(window, width, height): 



<!-- Start of picture text -->
The function takes a GLFW window object and two integers as<br><!-- End of picture text -->

- The function takes a GLFW window object and two integers as arguments 

- This function will be called every time the window is resized 



<!-- Start of picture text -->
The two integer arguments represent the new width and height of the<br><!-- End of picture text -->

- The two integer arguments represent the new width and height of the window in pixels 



<!-- Start of picture text -->
window in pixels<br><!-- End of picture text -->

34 



<!-- Start of picture text -->
Exam le code for<br>p g<br><!-- End of picture text -->



<!-- Start of picture text -->
lfwSetWindowSizeCallback<br>g<br><!-- End of picture text -->

### **Exam le code for lfwSetWindowSizeCallback** **<u>p g</u>** 

```
def resize(window, w, h):if not glfwInit():
glViewport(0, 0, w, h)
glfwTerminate()
exit()
def refresh(window):
glClearColor(0, 0, 0, 0)
glClear(GL_COLOR_BUFFER_BIT)glfwWindowHint(GLFW_DOUBLEBUFFER, GL_FALSE)
glBegin(GL_POLYGON)window = glfwCreateWindow(800, 800, "Resize", None, None)
glColor3f(1, 1, 1)glfwMakeContextCurrent(window)
--
glVertex3f(0.5, 0.5, 0)
glfwSetWindowRefreshCallback(window, refresh)
-
glVertex3f( 0.5, 0.5, 0)
glfwSetWindowSizeCallback(window, resize)
glVertex3f( 0.5,  0.5, 0)
-
glVertex3f(0.5,  0.5, 0)
glEnd()while not glfwWindowShouldClose(window):
glFlush()refresh(window)
glfwPollEvents()
glfwTerminate()
```



<!-- Start of picture text -->
800, "Resize", None, None), "Resize", None, None)<br><!-- End of picture text -->



<!-- Start of picture text -->
glfwTerminate()<br><!-- End of picture text -->



<!-- Start of picture text -->
()<br><!-- End of picture text -->

35 

### **lView ort** **<u>g p</u>** 



<!-- Start of picture text -->
h ) sets the area within the window that OpenGL will<br><!-- End of picture text -->

- _x w h_ 

- glViewport( , _y_ , , ) sets the area within the window that OpenGL will use to draw 



<!-- Start of picture text -->
-<br>The coordinates (x, y) specify the position of the bottom<br>the area<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>left corner of<br><!-- End of picture text -->

- 

- The coordinates (x, y) specify the position of the bottom left corner of the area 

- The w and h specify the width and height of the area 



<!-- Start of picture text -->
0, w, h), which means using the , w, h), which means using the<br><!-- End of picture text -->

- 0 

- In the example, we use glViewport( , 0, w, h), which means using the , w, h), which means using the entire window area to display 



<!-- Start of picture text -->
entire window area to display<br><!-- End of picture text -->

36 



<!-- Start of picture text -->
SSS<br><!-- End of picture text -->

# <mark>rT</mark> 























<!-- Start of picture text -->
If we want polygon to remain squared<br> We need to adjust range of vertex coordinate<br>accordingly, when window size is changed<br><!-- End of picture text -->



<!-- Start of picture text -->
2D sets coordinate range along  D sets coordinate range along<br>-<br>axis<br><!-- End of picture text -->

- gluOrtho2D sets coordinate range along  D sets coordinate range along - - 

- x axis and y axis 

- gluOrtho2D(left, right, bottom, top) takes parameters to transform the projection matrix into an orthographic projection (Discuss in Week 3) 

- Think of it as specifying corners of the area where to draw shapes 

   - 

   - bottom left corner of the window is (left, bottom) 

   - 

   - bottom right corner of the window is (right, bottom) 

   - 

   - top left corner of the window is (left, top) 



<!-- Start of picture text -->
-<br>right corner of the window is (right, top)<br><!-- End of picture text -->

- 

- top right corner of the window is (right, top) 

38 







<!-- Start of picture text -->
gluOrtho2D (fei)<br>a<br><!-- End of picture text -->



<!-- Start of picture text -->
3 giuOrtho2D. ek)<br>:<br><!-- End of picture text -->



<!-- Start of picture text -->
i pluOrtho2D Se)<br>a<br><!-- End of picture text -->





### **Put together and adjust Resize() callback** 

- We call glMatrixMode(GL_PROJECTION) and glLoadIdentity() before calling gluOrtho2D(...) to set up the coordinate system 



<!-- Start of picture text -->
gluOrtho2D(...) to set up the coordinate<br><!-- End of picture text -->

 Both functions are related to setting the projection transform, which we will discuss in week 3 

```
def resize(window, w, h):
glViewport(0, 0, w, h)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
# choose a shortest side
-
#        to have range of [1, 1]
if w < h:
```



<!-- Start of picture text -->
-<br>1, 1]<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>gluOrtho2D(<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>h/w, h/w)<br><!-- End of picture text -->

```
--
gluOrtho2D(1, 1, h/w, h/w)
else:
```





<!-- Start of picture text -->
-<br>gluOrtho2D(<br><!-- End of picture text -->



<!-- Start of picture text -->
- -<br>w/h, w/h,<br><!-- End of picture text -->



<!-- Start of picture text -->
-<br>1, 1)<br><!-- End of picture text -->

```
--
gluOrtho2D(w/h, w/h, 1, 1)
```

- Remember these two functions must always be called before calling gluOrtho2D 



<!-- Start of picture text -->
Using gluOrtho2D, we need to import<br><!-- End of picture text -->

- Using gluOrtho2D, we need to import OpenGL.GLU 



<!-- Start of picture text -->
OpenGL.GLU<br><!-- End of picture text -->

40 

###### References 

Dave Shreiner, Bill The Khronos OpenGL ARB Working Group, et al. OpenGL Programming Guide: The Official Guide To Learning OpenGL, Versions 3.0 and 3.1. Pearson Education, 2009. 



<!-- Start of picture text -->
Official Guide To Learning OpenGL, Versions 3.0 and 3.1.<br><!-- End of picture text -->



<!-- Start of picture text -->
Pearson Education, 2009.<br><!-- End of picture text -->



<!-- Start of picture text -->
and Edward Angel. Interactive Computer Graphics: A top-down<br><!-- End of picture text -->



<!-- Start of picture text -->
approach<br><!-- End of picture text -->

Dave Shreiner and Edward Angel. Interactive Computer Graphics: A top-down approach with OpenGL, 2nd Edition, 2009. 



<!-- Start of picture text -->
with OpenGL, 2nd Edition, 2009.<br><!-- End of picture text -->

Fletcher, M. PyOpenGL (The Python OpenGL® Binding). Available at: http://pyopengl.sourceforge.net, accessed Oct 14, 2011. 



<!-- Start of picture text -->
accessed Oct 14, 2011.<br><!-- End of picture text -->



GLFW Community. Community. GLFW Documentation: https://www.glfw.org/documentation, 



<!-- Start of picture text -->
GLFW Community. Community. GLFW Documentation: https://www.glfw.org/documentation,<br><!-- End of picture text -->

