from manim import *

class AI_ML(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Intelligence Artificielle", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        # Create a small neural network
        layers = [3, 5, 3]
        dots = []
        for i, n in enumerate(layers):
            layer = VGroup(*[Dot(radius=0.08, color="#FFD43B") for _ in range(n)])
            layer.arrange(DOWN, buff=0.4).shift(RIGHT * i * 1.2)
            dots.append(layer)

        for layer in dots:
            self.play(FadeIn(layer, shift=DOWN), run_time=0.5)

        # Connect layers
        lines = VGroup()
        for i in range(len(dots) - 1):
            for d1 in dots[i]:
                for d2 in dots[i + 1]:
                    lines.add(Line(d1.get_center(), d2.get_center(), stroke_opacity=0.3, color="#306998"))

        self.play(Create(lines, lag_ratio=0.01), run_time=2)
        self.wait(1)

