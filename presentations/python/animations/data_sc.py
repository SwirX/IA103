from manim import *

class DataScience(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Data Science", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        # Create bar chart
        bars = VGroup(*[
            Rectangle(width=0.3, height=h, color="#306998", fill_opacity=0.7)
            for h in [1, 2, 3.5, 2.5, 4]
        ])
        bars.arrange(RIGHT, buff=0.3).move_to(ORIGIN)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.2))
        self.wait(0.5)
        self.play(bars.animate.shift(LEFT*2).scale(0.7))

        # Line plot appears
        points = [(-2, -1), (-1, 1), (0, 0), (1, 2), (2, 3)]
        graph = VMobject(color="#FFD43B")
        graph.set_points_smoothly([*[np.array([x, y, 0]) for x, y in points]])
        self.play(Create(graph))
        self.wait(1)

