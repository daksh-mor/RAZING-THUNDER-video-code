from functools import reduce
from math import pi
import math
from os import write
from re import U
from manim import *
from numpy import right_shift



class write1(Scene):
    def construct(self):

        w = Text('Welcome').set_color_by_gradient(RED,BLUE,GREEN).scale(2.5)
        self.play(FadeIn(w),run_time=1)
        self.remove(w)
        t = Text('To').set_color(RED)
        self.play(FadeIn(t.scale(3.5)),run_time=0.5)
        self.remove(t)
        m = Text('my').set_color(GREEN)
        self.play(FadeIn(m.scale(3.5)),run_time=0.5)
        self.remove(m)
        c = Text('Channel').set_color(BLUE)
        self.play(FadeIn(c.scale(3.5)),run_time=0.5)
        self.remove(c)
        name = Text('RAZING THUNDER').set_color(PURPLE_C)
        self.play(Write(name.scale(1.5)), run_time = 0.5 )
        self.wait(1.5)
        self.play(Uncreate(name),run_time = 1.5)
        tex1 = MathTex('{(x)}^{(x^{40})}' , '=' , '{(\sqrt[7]{5})}^{(\sqrt[7]{5})}' ).scale(3).to_edge(UP).set_color_by_gradient(RED,BLUE,GREEN)
        self.play(Write(tex1),run_time = 2.5 )
        tex2 = Tex('Find $x^{ 35 }$').scale(4).next_to(tex1,DOWN*7)
        self.play(Write(tex2),run_time = 2 )
        framebox = SurroundingRectangle(tex2,buff=0.4)
        self.play(Create(framebox),run_time=1.7)
        self.wait(1.5)
        self.play(FadeOut(tex1,tex2),run_time = 1.7 )
class write2(Scene):
    # config.background_color = WHITE
    # config["background_color"] = WHITE
    def construct(self):
        
        text1 = Text('How to approach such questions?').set_color_by_gradient(RED,BLUE,GREEN).to_edge(UP).scale(1.3)
        text2 = Tex('1- Do not try to find out $x^{35}$').set_color(GREY_BROWN).scale(2).next_to(text1,DOWN*4)
        text3 = Tex('instead Try to find $x$').set_color(WHITE).scale(2).next_to(text2,DOWN*4)
        text4 = Text('RHS(Right hand side) seems to be some sort of same').set_color(YELLOW).scale(0.9)
        text5 = Text('So we will try to make LHS also same').set_color(ORANGE)
        self.play(Write(text1),run_time = 2)
        self.wait(1.5)
        self.play(Write(text2),run_time = 2)
        self.wait(1.5)
        self.play(Write(text3),run_time = 2)
        self.wait(1.5)
        self.remove(text2,text3)
        self.wait(1.5)
        self.play(Indicate(text1))
        self.wait(1.5)
        self.play(Write(text4.next_to(text1,DOWN*5)),run_time = 2.1)
        self.wait(1.5)
        self.play(Write(text5.next_to(text4,DOWN*5)),run_time= 2.2)
        self.wait(1.5)
        self.play(FadeOut(text4))
        self.wait(1.5)
        self.play(FadeOut(text5))
        self.wait(1.5)
        self.play(Uncreate(text1))
        self.wait(2)
class write3(Scene):
    # config.background_color = WHITE
    # config["background_color"] = WHITE
    def construct(self):
        self.wait(0.1)
        tex1 = MathTex('{(x)}^{(x^{40})}' , '=' , '{(\sqrt[7]{5})}^{(\sqrt[7]{5})}' ).to_edge(UP,buff=1).shift(LEFT*2).scale(2.2)
        self.play(Write(tex1),run_time = 2)
        self.wait(1.5)
        text = Text('Raising to power 40 on both sides').set_color(RED).next_to(tex1,DOWN,buff=1)
        self.play(GrowFromCenter(text),run_time = 1.5,rate_functions=there_and_back_with_pause)
        self.wait(1.5) 
        self.play(Indicate(text))
        self.wait(1.5)
        self.play(Uncreate(text))
        self.wait(1.5)
        tex2 = MathTex("(x)^{ { (x^{40}) }^{ 40 } } = { (\sqrt[7]{ 5 }) }^{ { (\sqrt[7]{5}) }^{ 40 } }").next_to(tex1,DOWN,buff=1).set_color(BLUE).scale(1.8)
        self.play(TransformFromCopy(tex1,tex2),run_time = 2.1)
        self.wait(1.5)
        line = Line().set_color(GREY_BROWN)
        self.play(Create(line.next_to(tex1,RIGHT).rotate(PI/2)),run_time = 2)
        self.wait(1.5)
        tex3 = MathTex("{ (x) }^{ {(a)}^b } = x^{a \cdot b}").set_color(GREEN)
        self.play(Write(tex3.next_to(tex1,RIGHT,buff=1.5)))
        self.wait(1.5)
        tex4 = MathTex("x^{ (40 \cdot x^{ 40 }) } = { (\sqrt[7]{ 5 }) }^{ { 40 \cdot (\sqrt[7]{5}) } }").next_to(tex2,DOWN,buff=1).set_color(LIGHT_PINK)
        self.play(Indicate(tex3))
        self.wait(1.5)
        self.play(TransformFromCopy(tex2,tex4.scale(2)),run_time=2)
        self.wait(1.5)
        text2 = MathTex("40 = 8\cdot5").next_to(tex3,DOWN,buff=1)
        
        self.play(FadeOut(tex1))
        self.wait(1.5)
        self.play(tex2.animate(run_time=1).shift(UP*2.5))
        self.wait(1.5)
        self.play(tex4.animate(run_time=1).shift(UP*2.5))
        self.wait(1.5)
        self.play(Create(text2),run_time = 1.5)
        self.wait(1.5)
        self.remove(tex4)
        tex5 = MathTex("x^{ (40 \cdot x^{ 40 }) }" , "=" ,"{ (\sqrt[7]{ 5 }) }^{ (8) \cdot (5 \cdot \sqrt[7]{5})  }").next_to(tex2,DOWN,buff=1).set_color(LIGHT_PINK).scale(1.8)
        self.add(tex5)
        self.play(Indicate(text2))
        self.play(ReplacementTransform(text2,tex5))
        self.wait(1.5)
        framebox = SurroundingRectangle(tex5[2],buff=0.5)
        # tex5.shift(RIGHT*0.3)
        self.play(Create(framebox),run_time = 1.5)
        self.wait(1.5)
        self.play(Indicate(tex3,scale_factor=2),run_time = 2.2)
        self.wait(1.5)
        self.play(Uncreate(framebox))
        self.wait(1.5)
        tex6 = MathTex("{(x^{ 40 })}^{(x^{ 40 })} }" , "=" ,"{ \left(\sqrt[7]{5}^8\\right) }^{ (5 \cdot 5^{1/7})  }").next_to(tex5,DOWN,buff=1).set_color(ORANGE).scale(1.8)
        text3 = MathTex("\sqrt[n]{ x } = x^{ \\frac { 1 }{ n } }").next_to(tex3,DOWN,buff=1).scale(1.5)
        self.play(Write(text3),run_time = 1.6)
        self.wait(1.5)
        
        text4 = MathTex("\sqrt[7]{ 5 }=5^{ \\frac{ 1 }{ 7 } } ").next_to(text3,DOWN,buff=1)
        self.play(Indicate(tex3))
        self.wait(1.5)
        self.play(Write(tex6),run_time = 1.7)
        self.wait(1.5)
        self.play(Write(text4))
        self.wait(1.5)
        self.play(Indicate(text4))
        self.wait(1.5)
        self.play(Indicate(tex6[2]))
        self.wait(1.5)
        self.play(Uncreate(text4))
        self.wait(1.5)
        text5 = MathTex("x^a \cdot x^b=x^{ a+b } ").next_to(text3,DOWN,buff=1)
        self.play(Write(text5),run_time = 1.4)
        self.wait(1.5)
        text6 = MathTex("5\cdot5^{\\frac{1}{7}}=5^{\\frac{8}{7}}").next_to(text5,DOWN,buff=1)
        self.play(Write(text6))
        
        
        self.play(FadeOut(tex2))
        # self.remove(tex4)
        self.remove(tex5)
        self.remove(text2)
        # self.play(text.animate(run_time=5).shift(UP*5))
        self.play(tex6.to_edge(UL).animate(run_time=4))
        self.play(Indicate(text6))
        self.wait(1.5)
        self.play(Indicate(tex6[2]))
        self.wait(1.5)
        tex7 = MathTex("{(x^{ 40 })}^{(x^{ 40 })} }" , "=" ,"{ \left(\sqrt[7]{5}^8\\right) }^{ \left(5^{\\frac{8}{7}}\\right)  }").next_to(tex6,DOWN,buff=1).set_color(BLUE_B).scale(1.8)
        self.play(TransformFromCopy(tex6,tex7),run_time = 2)
        self.wait(1.5)
        self.play(Indicate(tex7[2]))
        self.wait(1.5)
        self.play(Uncreate(text6))       
        self.wait(1.5)
        tex8 = MathTex("{(x^{ 40 })}^{(x^{ 40 })} }" , "=" ,"{ \left(\sqrt[7]{5}^8\\right) }^{ \left(\sqrt[7]{5}^8\\right)  }").next_to(tex7,DOWN,buff=1).set_color(PINK).scale(1.8)
        self.play(Indicate(text3),run_time = 2)
        self.wait(1.5)
        self.play(Indicate(tex7[2]))
        self.wait(1.5)
        self.play(Transform(tex7,tex8))
        self.wait(1.5)
        self.play(FadeOut(tex6))
        self.wait(1.5)
        self.play(FadeOut(tex7))
        self.wait(1.5)
        self.play(tex8.to_edge(UL).animate(run_time=3))
        self.wait(1.5)
        text7 = Text("By comparing both sides").next_to(tex8,DOWN,buff=1).scale(1.4).set_color_by_gradient(RED,BLUE)
        self.play(Create(text7),run_time = 1.8 )
        self.wait(1.5)
        self.play(Uncreate(text7))
        self.wait(1.5)
        tex9 = MathTex("(x^{ 40 })" , "=" , "\left(\sqrt[7]{ 5 }^8\\right)").next_to(tex8,DOWN,buff=1).scale(2)
        self.play(Write(tex9),run_time = 2)
        self.wait(1.5)
        text8 = Text("rooting(by 40) on both sides").next_to(tex9,DOWN,buff=1)
        self.play(Write(text8),run_time = 2)
        self.wait(1.5)
        self.play(Uncreate(text8))
        self.wait(1.5)
        tex10 = MathTex("x" , "=" , "5^{ \\frac{ 8 } { 7 } \cdot \\frac { 1 } { 40 }}").next_to(tex9,DOWN,buff=1).set_color(RED)
        self.play(Create(tex10),run_time = 2)
        self.wait(1.5)
        text8 = Tex("we have to find $x^{ 35 }$").next_to(tex10,DOWN,buff=1)
        self.play(Write(text8),run_time = 2)
        self.wait(1.5)
        self.play(Uncreate(text8))
        self.wait(1.5)
        tex11 = MathTex("x^{ 35 }" , "=" , "5^{ \\frac{ 8 } { 7 } \cdot \\frac { 1 } { 40 } \cdot 35 } ").next_to(tex10,DOWN).set_color(BLUE).scale(1.1)
        self.play(Write(tex11),run_time = 1.9)
        self.wait(1.5)
        text11 = Tex("Hence $x = 5$").to_edge(UP).set_color_by_gradient(RED,BLUE,GREEN).scale(2)
        self.play(FadeOut(tex8))
        self.wait(1.5)
        self.play(Indicate(tex11[2]),run_time = 2)
        self.wait(1.5)
        self.play(Create(text11),run_time = 2)
        self.wait(2)
        self.clear()
class write4(Scene):
    # config.background_color = WHITE
    # config["background_color"] = WHITE
    def construct(self):
        self.add(Tex(
            """
            Bonus Question 

            $3^{27^x}={27^3}^x$

            See previous video for solution
            """
        ).scale(2))
        self.wait(7)
        self.clear()
        self.add(Text(
            """
            Discord Link in description

            [homework help server]

            comment of if you have such questions
            """
        ))
        self.wait(7)
        self.clear()
        end = Tex("Thanks for watching").scale(3).to_edge(UP).set_color_by_gradient(RED,BLUE,GREEN)
        self.play(Create(end),run_time = 20 )
        self.wait(7)
class write5(Scene):
    # config.background_color = WHITE
    # config["background_color"] = WHITE
    def construct(self):
        self.add(Text(
            """
            Should I add my own voice

            or is it understandable without it?

                                         -commment
            """
        ).scale(1))
        self.wait(3)