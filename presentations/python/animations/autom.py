from manim import *

class Automation(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Automatisation", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        code = Code(
            code='''import os\nfor f in os.listdir():\n    print("Renommage:", f)''',
            language="Python",
            background="window",
            insert_line_no=False,
            style="monokai",
        ).scale(0.7)
        self.play(Write(code))
        self.wait(1)

