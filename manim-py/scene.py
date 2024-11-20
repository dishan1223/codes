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

class WheelRotationWithExplanation(Scene):
    def construct(self):
        # Parameters
        radius = 2  # This represents 5m in your example (scaled for visualization)
        circumference = 2 * PI * radius

        # Create a circle (the wheel)
        wheel = Circle(radius=radius, color=BLUE)
        wheel.set_fill(BLUE, opacity=0.1)

        # Create a point P at the top of the wheel (initial position)
        point_p = Dot(wheel.point_at_angle(0), color=RED)

        # Create a line from the center of the wheel to point P
        radius_line = Line(wheel.get_center(), wheel.point_at_angle(0), color=WHITE)

        # Display the circle and point P initially
        self.play(Create(wheel), Create(point_p), Create(radius_line))

        # Add the explanation text for the radius and circumference
        equation_text = MathTex(r"C = 2 \pi r", font_size=36).to_edge(UP)
        radius_text = MathTex(r"r = 5\ m", font_size=32).next_to(equation_text, DOWN)
        self.play(Write(equation_text), Write(radius_text))

        # Wait for a moment to let the user read the initial state
        self.wait(1)

        # Show that the total distance covered by the wheel after 360 degrees
        distance_text = MathTex(f"C = {circumference:.2f}\ m", font_size=32).to_edge(DOWN)
        self.play(Write(distance_text))

        # Animate the rotation of the wheel and point P moving along the circumference
        self.play(Rotate(wheel, angle=PI * 2, about_point=wheel.get_center(), run_time=5, rate_func=linear))

        # Remove old text, and show the distance again after rotation
        self.play(FadeOut(distance_text), FadeOut(radius_text), FadeOut(equation_text))

        # Visualizing the final position of point P
        new_position_text = MathTex(f"Point P has rotated 360°", font_size=32).to_edge(UP)
        self.play(Write(new_position_text))

        # Create an arc representing the rotation (the path point P followed)
        arc_path = Arc(radius=radius, angle=PI * 2, color=WHITE)
        self.play(Create(arc_path))

        # Highlight the total distance covered
        total_distance_text = MathTex(f"Total Distance Covered = {circumference:.2f}\ m", font_size=32).next_to(arc_path, DOWN)
        self.play(Write(total_distance_text))

        # Final visualization: rotation of the wheel, point moving, and updating the distance
        self.wait(2)

        # Clean up and exit
        self.play(FadeOut(new_position_text), FadeOut(total_distance_text), FadeOut(arc_path))
        self.wait(1)


#manim -pql scene.py WheelRotation

class WheelRotation(Scene):
    def construct(self):
        # Parameters
        radius = 2  # Setting the radius as 2 for visualization (which represents 5m in your example)
        circumference = 2 * PI * radius
        
        # Create a circle (the wheel)
        wheel = Circle(radius=radius, color=BLUE)

        # Create a point P at the top of the wheel (initial position)
        point_p = Dot(wheel.point_at_angle(0), color=RED)

        # Add the wheel and the point P to the scene
        self.play(Create(wheel), Create(point_p))
        
        # Distance text to display the circumference
        distance_text = MathTex(f"Distance = {circumference:.2f}m").to_edge(UP)
        self.play(Write(distance_text))

        # Add a line to visualize the path (this will be redrawn as the wheel rotates)
        path_line = Line(wheel.get_center(), wheel.point_at_angle(0), color=WHITE)
        self.play(Create(path_line))

        # Animation for the point to move along the circumference
        self.play(MoveAlongPath(point_p, wheel), run_time=4, rate_func=linear)
        
        # Highlight the distance as the point moves
        moving_distance_text = MathTex(f"Distance = {circumference:.2f}m").next_to(path_line, DOWN)
        self.play(Write(moving_distance_text))

        # Final state after the full 360-degree rotation
        self.wait(1)


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

        text.next_to(s,DOWN,buff=0.5)

        self.play(Create(s))
        self.play(Write(text),run_time=1)

# manim -pql scene.py MoveAround        
class MoveAround(Scene):
    def construct(self):
        square = Square(color=BLUE, fill_opacity=1)
        
        self.play(Create(square))
        self.play(square.animate.shift(LEFT))
        self.play(square.animate.set_fill(ORANGE))
        self.play(square.animate.scale(0.3))
        self.play(square.animate.rotate(0.4))


#manim -pql circle_rotation.py CircleRotation

class CircleRotation(Scene):
    def construct(self):
        # Define circle parameters
        circle_radius = 5
        circle = Circle(radius=circle_radius, color=BLUE)
        circle.move_to(ORIGIN)
        
        # Point P on the circle
        point_p = circle.point_at_angle(PI / 4)  # Point P at 45 degrees
        dot_p = Dot(point_p, color=RED)
        label_p = MathTex("P", color=RED).next_to(dot_p, UP)
        
        # Point P' after 180-degree rotation
        point_p_prime = circle.point_at_angle(PI / 4 + PI)  # 180 degrees from P
        dot_p_prime = Dot(point_p_prime, color=GREEN)
        label_p_prime = MathTex("P'", color=GREEN).next_to(dot_p_prime, DOWN)
        
        # Draw circle and points
        self.play(Create(circle))
        self.play(FadeIn(dot_p, label_p))
        self.play(FadeIn(dot_p_prime, label_p_prime))
        
        # Draw line between P and P'
        line = Line(point_p, point_p_prime, color=YELLOW)
        self.play(Create(line))
        
        # Add distance text
        distance = 2 * circle_radius  # Distance between P and P'
        distance_text = MathTex(f"Distance = {distance}\\,m").to_edge(DOWN)
        self.play(Write(distance_text))
        
        # Wait and hold the scene
        self.wait()

