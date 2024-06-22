#code execution
# manim -pql scene.py CreateCircle(name of the class)

# .set_fill() can be use to access some particular property of mobject

# there can be multiple classes to animate differect items

from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(GREEN, opacity=0.5) # set color and transparency
        self.play(Create(circle)) # show circle to the scene after rendering it
