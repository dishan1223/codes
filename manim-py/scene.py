# basic shapes -> 
#   Circle()
#   Triangle()
#   Square()

# .set_fill() can be use to access some particular property of mobject

# there can be multiple classes to animate differect items

#self.play() functions =
#   Create(object) to create object to the scene
#   Transform(object1, object2) transforms object1 to object2
#   FadeOut(object) fade an object out

from manim import *

# manim -pql scene.py CreateCircle(name of the class)
class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # create a circle
        circle.set_fill(GREEN, opacity=0.5) # set color and transparency
        self.play(Create(circle)) # show circle to the scene after rendering it


# manim -pql scene.py SquareToCircle

class SquareToCircle(Scene):
    def construct(self):
        # create circle object and add style property
        circle = Circle() 
        circle.set_fill(RED, opacity=0.5)

        # create a square object and add style property
        square = Square()
        square.rotate(PI/4) # rotate square a certain ammount

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
