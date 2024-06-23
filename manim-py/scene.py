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

# manim -pql scene.py CircleToTriangle 
class CircleToTriangle(Scene):
    def construct(self):
        # create circle object and add style property
        circle = Circle() 
        circle.set_fill(RED, opacity=0.5)

        # create a tirangle object and add style property
        triangle = Triangle()
        triangle.set_fill(RED, opacity=0.5)

        self.play(Create(circle))
        self.play(Transform(circle, triangle))
        self.play(FadeOut(circle))


# manim -pql scene.py SquareAndCircle
class SquareAndCircle(Scene):
    def construct(self):
        # create a circle and square object
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        square = Square()
        square.set_fill(BLUE, opacity=0.5)

        tri = Triangle()
        tri.set_fill(BLUE, opacity=0.5)
        
        c1 = Circle() 
        c1.set_fill(BLUE, opacity=1)
        c2 = Circle() 
        c2.set_fill(BLUE, opacity=1)

        #.next_to() function here takes square and places it at the RIGHT side of the circle
        #   buff is basically space between the two object

        square.next_to(circle, RIGHT, buff=0.5)
        tri.next_to(circle, LEFT, buff=0.5)
        c1.next_to(circle, UP, buff=0.5)
        c2.next_to(circle, DOWN, buff=0.5)
        self.play(Create(circle), Create(square), Create(tri), Create(c1),Create(c2)) # render the objects to the scene
