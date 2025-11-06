from manim import *

class PythonIntro(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"

        # Keywords
        keywords = ["Simple", "Polyvalent", "Demandé", "Communauté"]
        icons = ["📘", "🌐", "📈", "👥"]
        vgroup = VGroup()
        for i, word in enumerate(keywords):
            txt = Text(word, color="#FFD43B", font="Monospace").scale(1.2)
            txt.shift(UP*1.5 - RIGHT*3 + RIGHT*i*2)
            vgroup.add(txt)
        self.play(LaggedStart(*[Write(t) for t in vgroup], lag_ratio=0.3))

        # Transform into icons
        icon_objs = VGroup(*[Text(ic, font_size=60) for ic in icons])
        icon_objs.arrange(RIGHT, buff=2).to_edge(DOWN)
        self.play(Transform(vgroup, icon_objs))
        self.wait(1)

