from manim import *

class WebDev(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Développement Web", color="#FFD43B").to_edge(UP)

        rects = VGroup(
            Rectangle(width=4, height=2, color="#306998").shift(UP*0.5),
            Rectangle(width=3.5, height=1.5, color="#FFD43B").shift(DOWN*0.8)
        )
        flask = Text("Flask", color="#fff").scale(0.8).next_to(rects[0], DOWN, buff=0.3)
        django = Text("Django", color="#fff").scale(0.8).next_to(rects[1], UP, buff=0.3)

        self.play(Write(title))
        self.play(Create(rects[0]))
        self.play(Create(rects[1]))
        self.play(Write(flask), Write(django))
        self.wait(1)
        self.play(FadeOut(VGroup(title, rects, flask, django)))

