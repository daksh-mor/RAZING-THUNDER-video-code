from itertools import groupby
from manim import *
class S1(Scene):
    def construct(self):
        t1 = Text("How to approach ?").scale(2).to_edge(UP)
        self.play(GrowFromCenter(t1),run_time = 2.5)
        self.wait(2.5)
        t2 = Tex("Observing the last $3$ digits of powers of $5$").next_to(t1,DOWN,buff=1).set_color(RED_B).scale(1)
        self.play(Write(t2),run_time = 2.5)
        self.wait(5)
        t3 = Tex("""
        try to find last three digit of $5^5$ then \n 
        $5^{5^5} \dotsb$ , instead of $5^{5^{5^{5^{5}}}}$
        """).next_to(t2,DOWN,buff=1).scale(1).set_submobject_colors_by_gradient(BLUE,GREEN)
        self.play(Write(t3),run_time = 2.5)
        self.wait(5)   
class S2(Scene):
    def construct(self):
        t1 = Text("Let us observe the pattern : -").scale(1.5).to_edge(UP).set_color_by_gradient(RED,BLUE,GREEN)
        eqn = VGroup(*[
            MathTex("5^{}={}".format(i,5**i))for i in range(1,7)
        ]).arrange(DOWN).scale(1.35)
        eqn.shift(LEFT*3+DOWN)
        self.play(FadeIn(t1),Write(eqn),run_time = 2.5,rate_func = linear)
        self.wait(2.5)
        t2 = Text("""
        We care about the \n
        last three digits only
        """).to_edge(RIGHT).set_color(YELLOW)
        self.play(Write(t2),FadeOut(eqn[:2]),run_time = 2.5)
        self.wait(2.5)
        self.play(FadeOut(t2),eqn[2::].animate.shift(UP*2),run_time = 2.5)
        self.wait(2.5)
        t3 = Tex("So we can conclude that $5^{\\text{odd}}$ \\\ ends with $125$ and \\\ $5^{\\text{even}}$ ends with $625$",slant=BOLD,line_spacing=2.5).to_edge(RIGHT).set_color(GOLD)
        self.play(eqn[2:].animate.shift(LEFT),Write(t3),Indicate(eqn[2:]),run_time= 5)
        self.wait(5)
        t4 = Text("This can be proved with finite/mathematical induction").to_edge(DOWN,buff=0.5).set_color(TEAL_A).scale(0.75)
        r = BackgroundRectangle(t4,color=GREY_E)
        self.play(Create(t4),FadeIn(r),run_time=2.5)
        self.wait(2.5)
class S3(Scene):
    def construct(self):
        t1 = Tex("Proof by ","Finite Induction : -").scale(1).to_edge(UP).set_color_by_tex("Finite Induction",YELLOW)
        self.play(Write(t1))
        self.wait()
        t2 = Text("If a statement holds true for \nn = 0 (base case) , and \nalso true for inductive step (n+1)\nthen it is true for all natural numbers\ngrater than n where n is base case",line_spacing=1.5).next_to(t1,DOWN,buff=0.5).scale(0.95).set_color_by_gradient(RED,BLUE,GREEN)
        self.play(AddTextLetterByLetter(t2),run_time = 7.5)
        self.wait(2.5)
        self.play(*map(FadeOut, self.mobjects))
        t3 = Text("Form here , we can use\nfinite induction to prove\nthat for all natural numbers\nx such that x > 2",line_spacing=2).to_edge(UP,buff=0.1).set_color(GOLD_A).scale(0.75)
        t4 = MathTex("5^x \equiv 125 (mod \ 1000)", "\\\ 5^x \equiv 625 (mod \ 1000)",line_spacing = 2).next_to(t3,DOWN,buff=1.25).set_color_by_tex("2",YELLOW).shift(LEFT).scale(1.5)
        self.play(FadeIn(t3),run_time = 3.5)
        self.wait(3.5)
        b1 = Brace(t4[0],direction=RIGHT)
        b1_tex = b1.get_text("if x is odd").set_color(PURPLE)
        b2 = Brace(t4[1],direction=RIGHT)
        b2_tex = b2.get_text("if x is even").set_color(PURPLE)
        self.play(Write(t4),GrowFromCenter(b1_tex),GrowFromCenter(b2_tex),FadeIn(b1),FadeIn(b2),run_time = 5)
        self.wait(5)
class S4(Scene):
    def construct(self):
        t1 = MathTex("5^{\\text{any number}} \ = \ ","5 \ (\\text{last digit})").to_edge(UP).scale(1.5).set_color(GREEN)
        self.play(Write(t1),run_time = 2.5)
        self.wait(5)
        t2 = Text("odd").scale(1.5).move_to(t1[1]).set_color(BLUE)
        self.play(Transform(t1[1],t2),run_time = 2)
        self.wait()
        t3 = MathTex("5^","{5^{5^{5^{5}}}}").scale(2.5)
        self.play(Write(t3),rum_time = 2)
        self.wait()
        b = Brace(t3[1],direction=RIGHT,buff=0.75)
        b_tex = b.get_tex("\\rightarrow ", "\ odd").set_color(YELLOW)
        self.play(FadeIn(b),GrowFromCenter(b_tex),run_time = 2)
        self.wait()
        self.play(FadeOut(t3[1]),FadeOut(b),FadeOut(b_tex[0]),b_tex[1].animate.move_to(t3[1]),run_time = 2.5)
        self.wait(2.5)
        t4 = Tex("last three digit = $125$").next_to(t3,DOWN,buff=1).set_color_by_gradient(RED,BLUE,GREEN)
        self.play(Create(t4))
        self.wait(3)
        self.play(*map(FadeOut, self.mobjects))