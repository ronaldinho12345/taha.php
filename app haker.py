from Ursina import *
taha = Ursina()
window.color = color.olive
ball = Entity(
model='sphere',
color=color.cyan,
z=-1,
scale='0.1',
collider='sphere'
)
table = Entity(
 model="cube",   
color=color.black,
scale=(2,1,3),
rotation=(90,0,0) 
)
camera.orthographic = True
camera.fov = 4
app.run()