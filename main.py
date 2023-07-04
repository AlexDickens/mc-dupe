from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


MineCraft = Ursina()

class Blocks(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            model = "cube",
            parent = scene,
            color = color.white,
            texture = "white_cube",
            position = position,
            highlight_color = color.lime
        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down": block = Blocks(position = self.position + mouse.normal)
            if key == "right mouse down": destroy(self)
                
        


for x in range(16):
    for z in range(16):
        blocks = Blocks(position = (x,  0 , z))


player = FirstPersonController()

MineCraft.run()