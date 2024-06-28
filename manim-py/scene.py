# basic shapes -> 
#   Circle()
#   Triangle()
#   Square()

# .set_fill() can be use to access some particular property of mobject
# .set_stroke(color=BLACK,width=2) this is an example to get a custom colored border for object
# with obj1.next_to() , objects can be places UP,DOWN,LEFT,RIGHT relative to obj1

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
        circle = Circle().set_fill(RED, opactiy=0.5) 

        # create a square object and add style property
        square = Square().rotate(PI/4) #rotate square a certain amount

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

# manim -pql scene.py CircleToTriangle 
class CircleToTriangle(Scene):
    def construct(self):
        # create circle object and add style property
        circle = Circle().set_fill(RED, opacity=0.5) 

        # create a tirangle object and add style property
        triangle = Triangle().set_fill(RED, opacity=0.5)

        self.play(Create(circle))
        self.play(Transform(circle, triangle))
        self.play(FadeOut(circle))


# manim -pql scene.py SquareAndCircle
class SquareAndCircle(Scene):
    def construct(self):
        # create a circle and square object
        circle = Circle().set_fill(PINK, opacity=0.5)
        
        square = Square().set_fill(BLUE, opacity=0.5)

        tri = Triangle().set_fill(BLUE, opacity=0.5)
        
        c1 = Circle().set_fill(BLUE, opacity=1) 
        c2 = Circle().set_fill(BLUE, opacity=1) 

        #.next_to() function here takes square and places it at the RIGHT side of the circle
        #   buff is basically space between the two object

        square.next_to(circle, RIGHT, buff=0.5)
        tri.next_to(circle, LEFT, buff=0.5)
        c1.next_to(circle, UP, buff=0.5)
        c2.next_to(circle, DOWN, buff=0.5)
        self.play(Create(circle), Create(square), Create(tri), Create(c1),Create(c2)) # render the objects to the scene

# Using .animate syntax to animate methods

# manim -pql scene.py AnimatedSquareToCircle
class AnimatedSquareToCircle(Scene):
    def construct(self):
        square = Square().set_stroke(color=BLUE, width=2)
        circle = Circle().set_stroke(color=BLUE, width=2)
        
        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square,circle)) # this method transforms one object to another
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        ) # color the circle at the end

# manim -pql scene.py SquareToCircleToTriangle 
class SquareToCircleToTriangle(Scene):
    def construct(self):
        square = Square().set_fill(BLUE, opacity=0.5).set_stroke(color=BLUE, width=2)
        circle = Circle().set_fill(PINK, opacity=0.5).set_stroke(color=PINK, width=2)
        triangle = Triangle().set_fill(BLUE, opacity=0.5).set_stroke(color=BLUE, width=2)

        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(PINK, opacity=0.5))
        self.play(Transform(square, triangle))
        self.play(square.animate.set_fill(BLUE, opacity=0.5))
        # self.wait(seconds) to wait a certain amount of time after the animation is finished
        self.wait(2)

# manim -pql scene.py DifferentRotations
class DifferentRotations(Scene):
    def construct(self):
        l_square = Square().set_fill(BLUE, opacity=0.7).shift(2*LEFT)
        r_square = Square().set_fill(GREEN, opacity=0.7).shift(2*RIGHT)

        self.play(
            l_square.animate.rotate(PI),
            Rotate(r_square, angle=PI),
            run_time=2
        )
        self.wait(2)

# manim -pql scene.py Transformations
class Transformations(Scene):
    def construct(self):
        c = Circle().set_fill(PINK, opacity=1).set_stroke(color=PINK, width=2)
        s = Square().set_fill(BLUE, opacity=1).set_stroke(color=BLUE, width=2)
        t = Triangle().set_fill(RED, opacity=1).set_stroke(color=RED, width=2)
        
        self.add(c)
        self.wait(2)
        for shape in [s,t]:
            self.play(Transform(c,shape))
            self.wait(1)

# manim -pql scene.py TextTest
class TextTest(Scene):
    def construct(self):
        text = Text("HELLO, WORLD!")

        self.play(Write(text), run_time=4)
        self.wait(2)
        self.remove(text)

# manim -pql scene.py TextInsideCircle
class TextInsideCircle(Scene):
    def construct(self):
        c = Circle(radius=2).set_fill(PINK, opacity=0.5).set_stroke(color=PINK,width=2)
        text = Text("hello world", font_size=26)
    
        text.move_to(c.get_center())

        self.play(Create(c))
        self.play(Write(text),run_time=2)

        self.wait(2)

class SquareWithText(Scene):
    def construct(self):
        s = Square().set_fill(BLUE,opacity=0.5)
        text = Text("Square")

        text.next_to(s,DOWN)

        self.play(Create(s))
        self.play(Write(text),run_time=1)
        


