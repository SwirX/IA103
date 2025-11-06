from manim import *

class PythonFeatures(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"

        title = Text("Caractéristiques de Python", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        features = [
            "Lisible → indentation & syntaxe claire",
            "Interprété → code exécuté ligne par ligne",
            "Haut-niveau → gestion mémoire automatique",
            "Typage dynamique → flexible",
            "Extensible → modules en C/C++",
            "Bibliothèques riches → 'batteries incluses'"
        ]
        feature_texts = VGroup(*[Text(f, font_size=24, t2c={"→": "#FFD43B"}) for f in features])
        feature_texts.arrange(DOWN, buff=0.5).shift(DOWN*0.5)

        for f in feature_texts:
            self.play(FadeIn(f, shift=LEFT))
            self.wait(0.3)
        self.wait(1)

