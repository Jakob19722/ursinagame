from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()
vsync = True
player = PlatformerController2d(texture = "img/sprites/pngegg.png",y=-1, scale_y=1,color=color.red)
ground = Entity(model='quad', y=-4, scale_x=16, collider='box', color=color.green)
Sky() 
Audio(sound_file_name="sounds/thisislife.mp3", pitch = 1, loop = True, autoplay = True)


app.run()