# **Chapter 2 Double and Depth Buffering Interactive Computer Graphics** 



<!-- Start of picture text -->
Double and Depth Buffering<br><!-- End of picture text -->



<!-- Start of picture text -->
Interactive Computer Graphics<br><!-- End of picture text -->

**Chakrit Watcharopas** 

O) 

##### Outline 

O Single Buffering O Double Buffering O Depth Buffering 



<!-- Start of picture text -->
Depth Buffering<br><!-- End of picture text -->



<!-- Start of picture text -->
Flickering on Display with Single Framebuffer<br><!-- End of picture text -->



<!-- Start of picture text -->
et |<br><!-- End of picture text -->

a 



#### <u>Single Buffering</u> 



<!-- Start of picture text -->
— nes<br><!-- End of picture text -->



<!-- Start of picture text -->
O)<br><!-- End of picture text -->

### <u>Double Buffering</u> 



<!-- Start of picture text -->
Bs ini<br>|<br>C)<br><!-- End of picture text -->

### <u>Using Double Buffering</u> 



<!-- Start of picture text -->
O By default, GLFW default, GLFW GLFW creates a window with with a double-buffered color buffer<br><!-- End of picture text -->

O By default, GLFW default, GLFW GLFW creates a window with with a double-buffered color buffer O You can also enable or disable it by using glfwWindowHint(GLFW_DOUBLEBUFFER, flag) where flag is Boolean 

O Aprocess of rendering a scene: 1. Clear color buffer glClear( GL_COLOR_BUFFER_BIT) GL_COLOR_BUFFER_BIT) 



<!-- Start of picture text -->
glClear( GL_COLOR_BUFFER_BIT) GL_COLOR_BUFFER_BIT)<br><!-- End of picture text -->

2. Render scene 

3. Request swap of front and back buffers glfwSwapBuffers(window) 4. Repeat steps 1 - 3 for animation 

e 

<u>Depth Buffering and Hidden Surface Removal</u> 



### <u>Depth Buffering</u> 

| draw last draw first Viewpoint p ) ) eee increasing Z Source: (Pfister and Chan, 2005) 



<!-- Start of picture text -->
Source: (Pfister and Chan, 2005)<br><!-- End of picture text -->



## **De th Bufferin** **<u>p g</u>** 



9 

C) 

### <u>Depth Buffering</u> 

O GLFW will typically create a window with a depth buffer if the specified depth bits are greater than 0. The default value is 24 O glfwWindowHint(GLFW_DEPTH_BITS, 24) will set depth bits to 24 O A process of rendering a scene: 

1. Enable depth buffering in OpenGL glEnable( GL_DEPTH_TEST ) 2. Clear color and depth buffers giClear( GL_COLOR_BUFFER_BIT 

   - | GL_DEPTH BUFFER BIT ) 

3. Render a scene 



4. Swap color buffers 

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

