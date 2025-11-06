# manim -pql style_template.py
from manim import *

class PythonStyle(Scene):
    def construct(self):
        # Colors (Python-ish)
        PY_BLUE = "#306998"
        PY_YELLOW = "#FFD43B"
        BG = "#0A0F1C"

        self.camera.background_color = BG

        title = Text("Python", color=PY_YELLOW, font="Monospace").scale(2)
        glow_circle = Circle(color=PY_BLUE, stroke_width=8).surround(title).scale(1.3)
        self.play(Create(glow_circle), Write(title))
        self.play(glow_circle.animate.scale(1.5).fade(0.3))
        self.wait()

