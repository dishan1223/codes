#code execution
# manim -pql scene.py createCircle(name of the class)

from manim import *

class createCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(GREEN, opacity=0.5) # set color and transparency
        self.play(Create(circle)) # show circle to the scene after rendering it
