from manim import *
class S1(Scene):
    def construct(self):
        question = MathTex("1^2","-","2^2","+","3^2","-","4^2","\dotsb"," 99^2","-","100^2").to_edge(UP).scale(1.5)
        self.play(Write(question),run_time = 2)
        self.wait()
        text1 = Text("Try it yourself").next_to(question,DOWN,buff=1).set_color(BLUE)
        self.play(Create(text1),run_time = 1.5)
        self.wait(3)
        hint = Tex("Hint : $a^2-b^2 = (a-b)(a+b)$").next_to(text1,DOWN,buff=1).scale(1.2).set_color(GREEN)
        self.play(Write(hint),run_time = 1.5)
        self.wait(2)
        loading = Text("-").scale(100).next_to(hint,DOWN,buff=2)
        self.play(Write(loading),run_time = 3.5)
        self.wait(2)
class S2(Scene):
    def construct(self):
        text1 = Text("How to approach ?").scale(1.7).to_edge(UP)
        self.play(Write(text1),run_time = 1.5)
        self.wait(1.5)
        tex1 = Tex(
            """
            Instead of 100 numbers try to find \n
            the pattren with less numbers \n
            i.e ,  Solve this first \n
            \n
            $1^2-2^2+3^2-4^2$
            """
        ).next_to(text1,DOWN,buff=1).scale(1.35).set_color(RED)
        self.play(Write(tex1),run_time= 3)
        self.wait(2)
        self.add(Text("We will solve this question with 3 methods*").next_to(tex1,DOWN,buff=1).set_color(BLUE))
        self.wait(2)
        self.play(*map(FadeOut, self.mobjects),run_time = 1.5)
        self.wait(1.5)
class S3(Scene):
    def construct(self):
        text = Text("Property used :-").to_edge(UP).scale(2)
        self.play(Write(text),run_time= 1.5)
        self.wait(2)
        property1 = MathTex("a^2-b^2" , "=","(a-b)\cdot(a+b)").next_to(text,DOWN,buff=1).set_color(TEAL).scale(1.7)
        self.play(Create(property1),run_time = 1.5)
        self.wait(1.5)
        property2 = Tex("Sum of the first $n$ natural nunbers = $n\cdot\left(\\frac{n+1}{2}\\right)$ ").next_to(property1,DOWN,buff=1).set_color(GOLD).scale(1.3)
        self.play(Create(property2),run_time = 1.5)
        self.wait(2)
class S4(Scene):
    def construct(self):
        text1 = Text("Lets try to \nfind the pattren").scale(2.5).set_color_by_gradient(RED,BLUE,GREEN)
        self.play(Write(text1),run_time = 2)
        self.wait(3)
        self.play(FadeOut(text1))
        self.wait(2)
        question = MathTex("1^2-2^2","+","3^2-4^2").scale(2).to_edge(UP)
        self.play(Write(question),run_time = 2)
        self.wait(2) 
        brace1 = Brace(question[0],direction=DOWN)
        self.play(GrowFromCenter(brace1))
        self.wait()
        property1 = MathTex("a^2-b^2" , "=","(a-b)\cdot(a+b)").next_to(brace1,DOWN,buff=1).set_color(TEAL).scale(1.7).shift(RIGHT*3)
        self.play(Write(property1),run_time = 2)
        self.wait(2)
        ques2 = MathTex("1^2-2^2","=","(1-2)","(1+2)").scale(2).next_to(property1,DOWN,buff=1).set_color(MAROON_E).shift(RIGHT*0.5)
        self.play(Write(ques2),run_time = 2)
        self.wait(2)
        self.play(FadeOut(ques2[:2]),FadeOut(property1),run_time = 1.5)
        self.wait()
        self.play(ques2[2:].animate(run_time = 1.5).shift(UP*2.7+LEFT*7.5))
        self.wait(2)
        brace2 = Brace(question[2],direction=DOWN)
        brace2_text = brace2.get_text("(3 - 4)","(3 + 4)").scale(2).set_color(PURPLE_E).shift(DOWN*0.2,RIGHT*1.5)
        self.play(GrowFromCenter(brace2),FadeIn(brace2_text),run_time = 3)
        self.wait(2)    
        self.play(question[1].animate(run_time = 1.5).shift(DOWN*1.5))
        self.wait()
        brace3 = Brace(ques2[2],direction=DOWN)
        brace3_tex = brace3.get_tex("-1").scale(1.5).set_color(ORANGE)
        brace4 = Brace(question[2],direction=DOWN,buff=2)
        brace4_tex = brace4.get_tex("-1").scale(1.5).set_color(ORANGE)
        self.play(GrowFromCenter(brace3),GrowFromCenter(brace4),FadeIn(brace3_tex),FadeIn(brace4_tex),run_time = 3)
        self.wait(3)
        ques3 = MathTex("(-1)","\cdot","(1+2)","+","(-1)","\cdot","(3+4)").scale(1.7).set_color(GREEN_E).next_to(brace3_tex,DOWN,buff=0.5).shift(RIGHT*4)
        self.play(Write(ques3),run_time = 2)
        self.wait(1.5)
        text2 = Text("Taking (-1) common :-").scale(2).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(2)
        self.play(Uncreate(text2))
        self.wait(1.5)
        ques4 = MathTex("(-1)\cdot(1+2+3+4)").move_to(ques3).scale(2)
        self.play(ReplacementTransform(ques3,ques4),run_time= 2.5)
        self.wait(2)
        property2 = Tex("Sum of the first $n$ natural nunbers = $n\cdot\left(\\frac{n+1}{2}\\right)$ ").to_edge(DOWN).set_color(GOLD).scale(1.3)
        self.play(Create(property2),run_time = 1.5)
        self.wait(2)
        self.play(Uncreate(property2))
        self.wait(1.5)
        ques5 = MathTex("(-1)\cdot{\left(\\frac{4 \cdot 5}{2}\\right)}").move_to(ques4).scale(2).shift(DOWN).set_color(PINK)
        self.play(ReplacementTransform(ques4,ques5),run_time= 3)
        self.wait(2)
        ques6 = MathTex("=>","(-1)\cdot(10)").next_to(ques4).scale(1.5).set_color(BLUE_E).shift(RIGHT)
        self.play(Write(ques6),run_time = 2)
        self.wait(1.5)
class S5(Scene):
    def construct(self):
        text1 = Text("Now lets do the same \nthing with 100 numbers").scale(2)
        self.play(GrowFromCenter(text1),run_time = 2.5)
        self.wait(2.5)
        self.play(Uncreate(text1))
        self.wait()
        question = MathTex("1^2","-","2^2","+","3^2","-","4^2","\dotsb"," 99^2","-","100^2").to_edge(UP).scale(1.5)
        self.play(Write(question),run_time = 2)
        self.wait()
        brace1 = Brace(question[:3],direction=DOWN)
        brace1_tex = brace1.get_tex("(-1)(1+2)").scale(1).set_color(RED_B).shift(LEFT*0.5)
        self.play(GrowFromCenter(brace1),FadeIn(brace1_tex),run_time = 3)
        self.wait(2)
        brace2 = Brace(question[4:7],direction=DOWN)
        brace2_tex = brace2.get_tex("(-1)(3+4)").scale(1).set_color(GREEN_B)
        self.play(GrowFromCenter(brace2),FadeIn(brace2_tex),run_time = 3)
        self.wait(2)
        brace3 = Brace(question[8:],direction=DOWN)
        brace3_tex = brace3.get_tex("(-1)(99+100)").scale(1).set_color(BLUE_B)
        self.play(GrowFromCenter(brace3),FadeIn(brace3_tex),run_time = 3)
        self.wait(2)
        extra = Tex("$+$").scale(1).next_to(brace1_tex,RIGHT,buff=1).shift(LEFT*0.3)
        extra2 = MathTex("+ \dotsb +").scale(0.5).next_to(brace2_tex,RIGHT,buff=1).shift(LEFT*0.7)
        self.play(FadeIn(extra),FadeIn(extra2),run_time = 2.5)
        self.wait(2.5)
        text2 = Text("Taking (-1) common").scale(2).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(2)
        self.play(Uncreate(text2))
        self.wait(1.5)
        ques2 = MathTex("(-1)(1+2+3+4 \dotsb 99+100)").next_to(brace3_tex,DOWN,buff=1).set_color(TEAL_A).scale(1.9).shift(LEFT*3.5)
        self.play(DrawBorderThenFill(ques2),run_time = 3)
        self.wait(3)
        text2 = Text("By using the sum of \nn natural numbers formula \nHere n=100").scale(1).to_edge(DOWN)
        self.play(Write(text2))
        self.wait(2)
        self.play(Uncreate(text2))
        self.wait()
        ques3 = MathTex("(-1)\cdot{\left(\\frac{ 100\cdot 101}{2}\\right)}").move_to(ques2).set_color(GOLD_A).scale(2).shift(DOWN)
        self.play(ReplacementTransform(ques2,ques3),run_time = 3)
        self.wait(3)
        ques4 = MathTex("(-1)\cdot{\left(50 \cdot 101\\right)}").move_to(ques3).set_color(YELLOW_A).scale(2)
        self.play(ReplacementTransform(ques3,ques4),run_time = 2)
        self.wait(2)
        ques5 = MathTex("(-1)\cdot{\left(5050\\right)}").move_to(ques4).set_color(BLUE_A).scale(2)
        self.play(ReplacementTransform(ques4,ques5),run_time = 1)
        self.wait(2)
        ques6 = MathTex("-5050").move_to(ques5).set_color(PURPLE_B).scale(2)
        self.play(ReplacementTransform(ques5,ques6),run_time = 1)
        self.wait(2)
        self.play(ShowCreation(ques6))
        self.add(Text("Answer").to_edge(DOWN).set_color_by_gradient(RED,BLUE,GREEN))
        self.wait(3)
class S6(Scene):
    def construct(self):
        self.add(Text("Method 2").set_color_by_gradient(RED,BLUE,GREEN).scale(1.5).to_edge(UP))
        self.wait(20)
class S7(Scene):
    def construct(self):
        self.add(Text("Method 3").set_color_by_gradient(RED,BLUE,GREEN).scale(1.5).to_edge(UP))
        self.wait(20)
class S8(Scene):
    def construct(self):
        self.add(Tex(
            """
            Bonus question :-\n
            $2^2-3^2+4^2-5^2+ \dotsb +49^2-50^2$\n
            comment the answer
            """
        ).scale(1.5).set_color(BLUE_B))
        self.wait(7)
class S9(Scene):
    def construct(self):
        tex = Tex(
            """
            $1^2-2^2+3^2-4^2\dotsb$
            \n
            $\dotsb97^2-98^2+99^2-100^2$
            """
        ).scale(2.3).set_color_by_gradient(RED,BLUE,GREEN).shift(UP)
        self.add(tex)
        self.add(SurroundingRectangle(tex))
        self.add(Text("=> ? ").scale(2.5).next_to(tex,DOWN,buff=1))