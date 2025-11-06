from manim import *

class OtherDomains(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Autres Domaines", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        fields = ["CyberSécurité", "Robotique", "Finance", "Systèmes embarqués"]
        texts = VGroup(*[Text(f, color="#306998") for f in fields]).arrange(DOWN, buff=0.3)

        for t in texts:
            self.play(Write(t))
            self.wait(0.4)
        self.wait(1)

