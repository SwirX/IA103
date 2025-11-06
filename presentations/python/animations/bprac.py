from manim import *

class PythonBestPractices(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"
        title = Text("Bonnes pratiques en Python", color="#FFD43B").to_edge(UP)
        self.play(Write(title))

        snippets = [
            'age = 10  # nom clair',
            'if age >= 18:\n    print("Majeur")',
            'import math\nimport random',
            'def addition(a, b):\n    """Retourne la somme."""\n    return a + b',
            'def saluer(nom):\n    print(f"Bonjour {nom}!")',
            'print(addition(2, 3))',
            '# Suivre PEP8 pour style cohérent'
        ]

        snippet_objs = VGroup(*[Code(code_string=s, language="Python", background="window").scale(0.5) for s in snippets])
        snippet_objs.arrange(DOWN, buff=0.3).shift(DOWN*0.5)

        for snip in snippet_objs:
            self.play(FadeIn(snip, shift=UP))
            self.wait(0.5)
        self.wait(1)

