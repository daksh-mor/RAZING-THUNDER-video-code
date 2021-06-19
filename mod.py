from manim import *
import functools
config.background_color = DARKER_GREY
config["background_color"] = DARKER_GREY
Text = functools.partial(Text, font="Alsina")
config.tex_template = TexFontTemplates.comfortaa

class S1(Scene):
	def construct(self):
		text = Text("Finding Last digit \nof any number").scale(3).set_color(BLUE_A)
		self.play(Write(text),run_time = 1.5)
		self.wait(1.5)
		self.play(FadeOut(text))
		r = Text("Recognizing Patterns").scale(2.5).to_edge(UP)
		self.play(Create(r))
		self.wait()
		self.play(r.animate.shift(UP*6),run_time = 1.5)
		self.wait()
		tex = MathTex(r"2^1 \ = \ 2 \\ 2^2 \ = \  4 \\ 2^3 \ = \ 8 \\ 2^4 \ = \ 16 \\ 2^5 \ = \ 32 \\ 2^6 \ = \ 64 \\ 2^7 \ = \ 128 \\ 2^8 \ = \ 256 \\ 2^9 \ = \  ? ").scale(2.5).set_color(YELLOW_D).shift(DOWN*2)
		self.play(AddTextWordByWord(tex),run_time = 5)
		self.wait(3)
		b1 = Brace(tex,direction=RIGHT)
		b1_tex = b1.get_text(
			"""
			See the Pattern \n
			2,4,8,6\n
			so whats the \n
			next last digit = 2
			"""
			).scale(1)
		self.play(tex.animate.shift(LEFT*3.5),GrowFromCenter(b1_tex),FadeIn(b1),b1_tex.animate.shift(LEFT*2),b1.animate.shift(LEFT*2),run_time = 1.5)
		self.wait(5)
		self.play(*map(FadeOut, self.mobjects),run_time=1.5)
		self.wait()
		text2 = Text("therefore cyclicity of 2 = 4").scale(2).set_color(GREEN).to_edge(UP).shift(UP*7)
		self.play(Write(text2))
		self.wait()
		tex2 = Tex(
			"""
			Example Last Digit of $2^{ 37 }$\n
			\n
			37 gives remainder = 1 when\n
			 \n
			divided by 4 
			 \n
			= $2^1 = 2$\n
			\n
			Therefore last digit = 2
			"""
			).scale(2).set_color_by_gradient(RED,GREEN,BLUE)
		self.play(Create(tex2),run_time = 2.5)
		self.wait(5)
		self.play(*map(FadeOut, self.mobjects),run_time=1.5)
		self.wait()
		tex3 = Tex(
			"""
			Cyclicity of all numbers :-\n
			$1 = 1$\n
			$2 = 4$\n
			$3 = 4$\n
			$4 = 2$\n
			$5 = 1$\n
			$6 = 1$\n
			$7 = 4$\n
			$8 = 4$\n
			$9 = 2$\n
			$10 = 1$
			"""
			).scale(2).set_color(BLUE_C).shift(UP*2)
		self.play(Write(tex3),run_time=2.5)
		self.wait(2.5)
		tex4 = MathTex("example \ =\ 7^{ 77 }").set_color(GREEN).scale(2).next_to(tex3,DOWN,buff=1)
		self.play(Write(tex4),run_time=1)
		self.wait()
		tex5 = MathTex("7^1 \ = \ 7").next_to(tex4,DOWN,buff=1).scale(2).set_color(RED)
		self.play(Write(tex5),run_time=1)
		self.wait()
		tex7 = Tex("Bonus = \nlast digit of $5^{ 55 }$").next_to(tex5,DOWN,buff=1).set_color(GOLD).scale(2)
		self.play(Write(tex7))
		self.wait(3)
