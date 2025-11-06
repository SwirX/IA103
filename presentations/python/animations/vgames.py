from manim import *

class GameDev(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Jeux Vidéo", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        sprite = Square(side_length=0.3, color="#FFD43B", fill_opacity=1).shift(DOWN*2)
        self.play(FadeIn(sprite))
        self.play(sprite.animate.shift(UP*2).rotate(PI/6))
        self.play(sprite.animate.shift(DOWN*2).rotate(-PI/6))
        self.wait(1)

