from manim import *
class S1(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        text = Text(
            """
            Which Background color 

            Should I use ?

            Black or White

            (any feedback would be appreciated)
            """
        )
        self.play(Create(text.set_color(BLACK)),run_time = 3)
        self.wait(1.5)
class S2(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        text1 = Text("Welcome").set_color(BLACK)
        text2 = Text("To").set_color(DARKER_GRAY)
        text3 = Text(
        """
        Razing Thunder's 
              
                Channel
        """
        ).set_color(DARK_GREY)
        self.play(Write(text1.scale(2)))
        self.wait()
        self.remove(text1)
        self.play(Write(text2.scale(2)))
        self.wait()
        self.remove(text2)
        self.play(Write(text3.scale(2)))
        self.wait()
class S3(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        text = Tex("Simplify " , "the expression :-").to_edge(UP,buff=1).set_color(DARK_GREY).scale(1.8)
        self.play(Create(text),run_time = 1.5)
        self.wait()
        question = MathTex("{3","^x","+","63", "\\over","21","^{ x-2 }" ,"+","7","^{ x-1 }}").set_color(BLACK).scale(3).next_to(text,DOWN,buff=2)
        self.play(Write(question),run_time=2)
        self.wait()
        self.play(Indicate(text[0]),run_time = 1)
        self.wait()
class S4(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        text = Text("How to approach ?").to_edge(UP).scale(1.5).set_color(BLACK)
        self.play(Create(text),run_time = 2 )
        self.wait()
        text2 = Text(
            """
            There are 4 total numbers

            in which 2 are compostie

            so we can further break down them     
            """
            ).set_color(DARK_GREY)
        self.play(Write(text2),run_time = 3)
        self.wait(2)
        question = MathTex("{3","^x","+","63", "\\over","21","^{ x-2 }" ,"+","7","^{ x-1 }}").set_color(RED_E).to_edge(DOWN)
        self.play(Create(question),run_time = 1.4)
        self.wait()
        extra1 = Text("composite numbers").set_color(BLUE_E).to_edge(DR).scale(0.5)
        self.play(Indicate(question[3],color=YELLOW_E,scale_factor=2),Indicate(question[5],color=YELLOW_E,scale_factor=2),Create(extra1),run_time=3)
        self.wait(2)
        self.remove(extra1)
        text3 = Text(
            """
            We should simplify numerator 

            and denominator separately
            """
        ).set_color(TEAL_E)
        self.remove(text2)
        self.play(Write(text3),run_time = 3)
        self.wait(3)
class S5(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        question = MathTex("{3","^x","+","63", "\\over","21","^{ x-2 }" ,"+","7","^{ x-1 }}").set_color(RED_E).to_edge(UL)
        self.play(DrawBorderThenFill(question),run_time = 1.6)
        self.wait(1.5)
        self.play(question[5::].animate(run_time=1.5).shift(RIGHT*7+UP))
        self.wait(1.5)
        ques2 = MathTex("{(7 \cdot 3)}^{ x-2 }" ,"+","7","^{ x-1 }}").set_color(BLUE_D).move_to(question[5::])
        self.play(ReplacementTransform(question[5::],ques2),run_time = 3)
        self.wait(1.5)
        property1 = MathTex("{(a \cdot b)}^x = a^x \cdot b^x")
        self.play(Create(property1.set_color(BLACK).scale(1.5)),run_time = 1.5)
        self.wait(1.5)
        self.play(Uncreate(property1))
        self.wait(0.5)
        ques3 = MathTex("7^{ x-2 }"," \cdot ","3^{ x-2 }" ,"+","7","^{ x-1 }}").set_color(DARK_GREY).next_to(ques2,DOWN,buff=1)
        self.play(TransformFromCopy(ques2,ques3),run_time = 1.7)
        self.wait()
        property2 = Tex("Taking $7^{ x-2 }$ common")
        self.play(Create(property2.set_color(PURPLE_E).scale(1.5)),run_time = 1.5)
        self.wait(1.5)
        self.play(Uncreate(property2))
        self.wait(0.5)
        ques4 = MathTex("7^{ x-2 }"," \cdot ","\left[3^{ x-2 }" ,"+","{7","^{ x-1 }","\over","7^{ x-2 }}\\right]").set_color(BLACK).next_to(ques3,DOWN,buff=1)
        self.play(TransformFromCopy(ques3,ques4),run_time = 2)
        self.wait()
        property3 = MathTex("{x^a \over x^b} = x^{ a-b }").shift(DOWN*2)
        self.play(Create(property3.set_color(BLACK).scale(1)),run_time = 1.5)
        self.wait(1.5)
        self.play(Uncreate(property3))
        self.wait(1.5)
        property4 = MathTex("{7","^{ x-1 }","\over","7^{ x-2 }}","=7^{ x-1-(x-2)}=7^1").shift(DOWN*3)
        self.play(Write(property4.set_color(BLACK).scale(1.5)),run_time = 5)
        self.wait(3)
        self.play(Indicate(property4[4],color=YELLOW_E),run_time = 1.5)
        self.wait()
        self.play(Uncreate(property4))
        self.wait(2)
        ques5 = MathTex("7^{ x-2 }"," \cdot ","\left[3^{ x-2 }" ,"+","7\\right]").set_color(BLACK).next_to(ques3,DOWN,buff=1)
        self.play(ReplacementTransform(ques4,ques5),run_time = 2.5)
        self.wait(2.5)
        final = MathTex("21","^{ x-2 }" ,"+","7","^{ x-1 }" ,"="," 7^{ x-2 }"," \cdot ","\left[3^{ x-2 }" ,"+","7\\right]")
        self.play(Write(final.set_color_by_gradient(RED_E,BLUE_E).scale(1).to_edge(DOWN)),run_time = 3)
        self.wait(2)
        self.play(final[6::].animate(run_time = 4).shift(UP*5.5+LEFT*6.8))
        self.wait(2)
        self.play(*map(FadeOut, self.mobjects),run_time = 3)
        self.wait(2)
class S6(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        question = MathTex("{3","^x","+","63", "\\over" ," 7^{ x-2 }"," \cdot ","\left[3^{ x-2 }" ,"+","7\\right]").set_color(GOLD_E).to_edge(UL)
        self.play(Write(question),run_time= 1.5)
        self.wait()
        self.play(question[:4].animate(run_time=1.5).shift(RIGHT*6.8))
        self.wait(1.5)
        ques2 = MathTex("3","^x","+","7 \cdot 9").set_color(MAROON_E).move_to(question[:4]).scale(2)
        ques3 = MathTex("3","^x","+","3^2 \cdot 7").set_color(MAROON_E).move_to(question[:4]).scale(2)
        self.play(ReplacementTransform(question[:4],ques2),run_time= 1.6)
        self.wait(1.5)
        self.play(ReplacementTransform(ques2,ques3),run_time= 1.6)
        self.wait(1.5)
        extra1 = Tex("Take $3^2$ common")
        self.play(Create(extra1.set_color(BLACK).scale(2).to_edge(DOWN,buff=1)),run_time = 1.5)
        self.wait(1.5)
        self.play(Uncreate(extra1))
        self.wait()
        ques4 = MathTex("3^2","\left({3^x \over 3^2}","+","7 \\right)").set_color(PURPLE_E).next_to(ques3,DOWN,buff=2).scale(2)
        self.play(Write(ques4),run_time= 1.7)
        self.wait(3)
        property3 = MathTex("{x^a \over x^b} = x^{ a-b }").to_edge(DOWN)
        self.play(Create(property3.set_color(BLACK).scale(2)),run_time = 1.5)
        self.wait(1.5)
        self.play(Uncreate(property3))
        self.wait(1.5)
        ques5 = MathTex("\left(3^{ x-2 }+7\\right)").set_color(PURPLE_E).move_to(ques4[1::]).scale(2)
        self.play(ReplacementTransform(ques4[1::],ques5),run_time = 1.5)
        self.wait(3)
        self.play(ques4.animate(run_time = 2).shift(LEFT*7+UP*3.2).scale(0.5))
        self.wait(1.5)
        line = Line().rotate(PI/9).move_to(ques4[1:]).set_color(BLACK)
        line2 = Line().rotate(PI/9).move_to(question[7:]).set_color(BLACK)
        self.wait()
        self.play(Create(VGroup(line,line2),run_time=2))
        self.wait(3)
        self.play(*map(FadeOut, self.mobjects),run_time = 3)
        self.wait()
class S7(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        question = MathTex("3^2","\over","7","^{ x-2 }").scale(3).to_edge(UP,buff=1).set_color(GREEN_E)
        self.play(Create(question),run_time = 2)
        self.wait(2)
        property3 = MathTex("{x^a \over x^b} = x^{ a-b }").to_edge(DOWN)
        self.play(Create(property3.set_color(BLACK).scale(2)),run_time = 1.5)
        self.wait(2)
        self.play(Indicate(question[2:],color=YELLOW_E))
        self.wait(2)
        self.play(Uncreate(property3))
        self.wait(2)
        ques2 = MathTex("3^2","\over","{7^x","\over","7^2}").scale(3).to_edge(UP,buff=1).set_color(GREEN_E)
        self.play(ReplacementTransform(question,ques2),run_time = 2.5)
        self.wait(2.5)
        ques3 = MathTex("3^2 \cdot 7^2","\over","7^x").scale(3).to_edge(UP,buff=1).set_color(GREEN_E)
        self.play(ReplacementTransform(ques2,ques3),run_time = 2.5)
        self.wait(2.5)
        ques4 = MathTex("9 \cdot 49","\over","7^x").scale(3).to_edge(UP,buff=1).set_color(GREEN_E)
        self.play(ReplacementTransform(ques3,ques4),run_time = 2.5)
        self.wait(2.5)
        ques5 = MathTex("441","\over","7^x").scale(3).to_edge(UP,buff=1).set_color(GREEN_E)
        self.play(ReplacementTransform(ques4,ques5),run_time = 2.5)
        self.wait(2.5)
        framebox = SurroundingRectangle(ques5,color=GOLD_E,buff=0.8)
        self.play(Create(framebox),run_time = 1.5)
        self.wait()
        self.add(Text("Answer").set_color_by_gradient(RED_E,BLUE_E,GREEN_E).scale(2).to_edge(DOWN))
        self.wait(2)
        self.play(*map(FadeOut, self.mobjects),run_time = 3)
        self.wait()
class S8(Scene):
    config.background_color = WHITE
    config["background_color"] = WHITE
    def construct(self):
        self.add(Tex(
           '''
           Bonus Problem :-

           Find the last digit of $39^{ 101 }$
           ''' 
        ).scale(2).set_color_by_gradient(BLACK,BLUE_E))
        self.wait(5)
        self.play(*map(FadeOut, self.mobjects),run_time = 2)
        self.wait(3)
        self.add(Text(
           """
           Contact me,if you have any such questions

           Through Discord,Gmail or in comments

           Source code in description

           [Link in description of all things]
           """ 
        ).scale(1).set_color_by_gradient(BLUE_E,DARK_GREY,BLACK))
        self.wait(5)
        self.play(*map(FadeOut, self.mobjects),run_time = 3)
        self.wait(2)