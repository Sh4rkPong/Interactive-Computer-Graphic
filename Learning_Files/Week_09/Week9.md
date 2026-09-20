*ตัวแปร uniform*
    โค้ดในการใช้ตัวแปร uniform เพื่อใช้ส่งข้อมูลจากโปรแกรมหลัก (application) ไปยัง shader (ทั้ง vertex shader และ fragment shader) ซึ่งตัวแปรประเภทนี้จะมีค่าเดียวกันสำหรับทุก vertex หรือทุก fragment ที่ถูกประมวลผล
    **โค้ดฝั่ง CPU**
```
        glUseProgram(prog_id)
    
    
        shininess_loc = glGetUniformLocation(prog_id, "shininess")
    
        glUniform1f(shininess_loc, 50)
    
    
        kd_loc = glGetUniformLocation(prog_id, "Kd")
    
        glUniform3f(kd_loc, 1.0, 0.25, 0.25)
    
    
        ks_loc = glGetUniformLocation(prog_id, "Ks")
    
        Ks = (1.0, 0.5, 0.5)
    
        glUniform3fv(ks_loc, 1, Ks)
    
    
        model_mat_loc = glGetUniformLocation(prog_id, "model_mat")
    
        model_mat = Translate(1, 2, 3)
    
        glUniformMatrix4fv(model_mat_loc, 1, True, model_mat)
```
**โค้ด Vertex shader ฝั่ง GPU**
```
    vert_code = '''

#version 110

uniform float shininess;

uniform vec3 Kd, Ks;

uniform mat4 model_mat;

void main()

{

   :

   :

}''
```
**ตัวแปร varying (หรือ in/out สำหรับ GLSL เวอร์ชัน >= 1.3)**

    โค้ดในการใช้ตัวแปร varying ใช้เพื่อส่งข้อมูลจาก vertex shader ไปยัง fragment shader โดยตัวแปร varying 
    จะถือเป็นตัวแปรที่มีค่าต่างกันสำหรับแต่ละ fragment เนื่องจากค่าในตัวแปรนี้จะถูกคำนวณด้วยการ interpolate จากค่าที่ถูกกำหนดไว้ใน vertex shader 
    ไปให้กับทุก fragment ที่อยู่ภายในโพลีกอน

**โค้ด Vertex shader ฝั่ง GPU**
```
    vert_code = '''

#version 110

varying vec3 v_color;

void main()

{

   :

   :

   v_color = gl_Color;

   

}'''
```

**โค้ด Fragment shader ฝั่ง GPU**
```
    frag_code = '''

#version 110

varying vec3 v_color;

void main()

{

   gl_FragColor = vec4(v_color, 1);

}'''
```
*ตัวแปร attribute (หรือ in สำหรับ GLSL เวอร์ชัน >= 1.3)*

    โค้ดในการใช้ตัวแปร attribute ซึ่งถูกใช้ใน vertex shader เพื่อรับข้อมูลจากโปรแกรมหลัก (application) ซึ่งข้อมูลเหล่านี้กำหนดคุณลักษณะเฉพาะของจุด vertex เช่น ตำแหน่ง สี หรือเวกเตอร์นอร์มัล

**โค้ดฝั่ง CPU**
```
    glUseProgram(prog_id)


    vao = glGenVertexArrays(1)

    glBindVertexArray(vao)

    vbo = glGenBuffers(4)

    glBindBuffer(GL_ARRAY_BUFFER, vbo[0])

    glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)

    position_loc = glGetAttribLocation(prog_id, "position")

    if position_loc != -1:

        glVertexAttribPointer(position_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))

        glEnableVertexAttribArray(position_loc)


    color_loc = glGetAttribLocation(prog_id, "color")

    glBindBuffer(GL_ARRAY_BUFFER, vbo[1])

    glBufferData(GL_ARRAY_BUFFER, colors, GL_STATIC_DRAW)

    if color_loc != -1:

        glVertexAttribPointer(color_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))

        glEnableVertexAttribArray(color_loc)


    normal_loc = glGetAttribLocation(prog_id, "normal")

    glBindBuffer(GL_ARRAY_BUFFER, vbo[2])

    glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)

    if normal_loc != -1:

        glVertexAttribPointer(normal_loc, 3, GL_FLOAT, GL_FALSE, 0, c_void_p(0))

        glEnableVertexAttribArray(normal_loc)


    uv_loc = glGetAttribLocation(prog_id, "uv")

    glBindBuffer(GL_ARRAY_BUFFER, vbo[3])

    glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)

    if uv_loc != -1:

        glVertexAttribPointer(uv_loc, 2, GL_FLOAT, GL_FALSE, 0, c_void_p(0))

        glEnableVertexAttribArray(uv_loc)
```

**โค้ด Vertex shader ฝั่ง GPU**

```
    vert_code = '''

#version 110

attribute vec3 position, color, normal;

attribute vec2 uv;

void main()

{

   :

   :

}'''
```
# Assignment Week 9 
**เรนเดอร์ตัวนิ่มด้วย GLSL**

ให้ใช้โค้ด model_vao_vbo_exercise.py โดยปรับให้โปรแกรมมีการใช้ VAO และ VBO ในการส่งข้อมูลเวอร์เท็กซ์ไปยัง vertex shader 
และมีการใช้ตัวแปรที่มี qualifer เป็น in, out, และ uniform ในการทำงานของเฉดเดอร์ โดยมีรายละเอียดดังต่อไปนี้

    ให้โปรแกรมส่งข้อมูลตัวนิ่มจากไฟล์ armadillo.tri เข้าไปยัง vertex shader ผ่านการใช้ VAO และ VBO และมีการประกาศตัวแปร in ใน vertex shader เพื่อรับข้อมูลตำแหน่ง (position เป็น vec3), เวกเตอร์นอร์มัล (normal เป็น vec3) และพิกัดเท็กเจอร์ (uv เป็น vec2) ของแต่ละจุดเวอร์เท็กซ์

    ประกาศตัวแปร uniform ใน vertex shader เพื่อรับข้อมูลจาก CPU ผ่าน widget ของ ImGui โดยให้ผู้ใช้สามารถปรับเปลี่ยนค่าดังต่อไปนี้

        Kd1 และ Kd2 มีชนิดข้อมูลเป็น vec3

        light_position มีชนิดข้อมูลเป็น vec3

    ประกาศตัวแปร out ใน vertex shader ที่มีชนิดข้อมูลเป็น vec3 ที่มีชื่อว่า smooth_color (ที่สอดคล้องกับตัวแปร in ใน fragment shader)
    เพื่อส่งข้อมูลสีไปยัง fragment shader

    ประกาศตัวแปร in ใน fragment shader ที่รับค่าจาก smooth_color

    ประกาศตัวแปร out ใน fragment shader ที่มีชนิดเป็น vec4 ที่มีชื่อว่า fragment_color

    ใน vertex shader 

        กำหนดค่าให้กับตัวแปร gl_Position ให้มีค่าเท่ากับการคูณค่าระหว่างเมทริกซ์ MVP กับ homogeneous coordinate ของ position โดย MVP 
        มีชนิดเป็น mat4() และมีค่าเท่ากับ

    mat4 MVP = mat4(1.81,     0,    0,    0,      

                       0,  2.41,    0,    0,      

                       0,     0,   -1,   -1,    

                    -1.0, -6.34, 8.14, 8.15);

        ให้เขียนโค้ดเพื่อสร้างเวกเตอร์ L ที่คำนวณมาจาก light_position - position และทำให้เป็นเวกเตอร์ 1 หน่วยด้วยฟังก์ชัน normalize()

        ให้กำหนดค่าให้กับตัวแปร smooth_color โดยหากค่า position.x < 0 ให้ค่า smooth_color มีค่าเป็น Kd1*max(dot(L, normal), 0) ไม่อย่างนั้นให้มีค่าเป็น Kd2*max(dot(L, normal), 0)

    ใน fragment shader 

        กำหนดค่าให้กับตัวแปร fragment_color ให้มีค่าเท่ากับ smooth_color

ฝึก GLSL เพิ่มเติม 

    จากเงื่อนไขที่ทดสอบ position.x < 0 ให้เปลี่ยนค่าคงที่ 0 เป็นค่าจากตัวแปร uniform แทน โดยให้ผู้ใช้สามารถปรับเปลี่ยนค่านี้ผ่าน UI widget 
    ได้
