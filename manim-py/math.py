# to the MathTex or Tex user need to have Latex installed


from manim import *

class MathEquations(Scene):
    def construct(self):
        # MathTex or Tex for math equations
        equation = Text("E = mc²") # r means its a row string for latex
        
        # postion it to the center/ origin
        equation.move_to(ORIGIN)

        self.play(Write(equation))
        self.wait(2)

