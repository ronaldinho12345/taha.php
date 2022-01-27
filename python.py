from ursina import *
app=ursina()
cube=Entity(model='cube',color=color.yellow,rotation=(45),texture='linear gradient')
class Game(Button):  
    def __init__(selfposition=[0,0,]):
      super().__init__(
        parent=scane,
        position=position,
        model='cube',
        origin_y=5,
        texture='white_cube',
       higlight_color=color.red  
     )
def input(selfkey):
    if key=='left mouse down':
        biuld=Game(postion=self.postion+mouse.normal)
    if key=='right mouse down':
        destroy(self)
        for z in range(8):
            for x in range(8):
                rako=Game[position(x,o,y)]
app.run()
