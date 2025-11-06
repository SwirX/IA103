from manim import *

class PythonInterpreter(Scene):
    def construct(self):
        self.camera.background_color = "#0A0F1C"

        source = Text("Code Python (main.py)", color="#FFD43B").to_edge(LEFT)
        interpreter = Text("Interpréteur Python", color="#306998").shift(RIGHT*2)
        bytecode = Text("Bytecode", color="#FFD43B").shift(RIGHT*4)
        output = Text("Résultat", color="#00FF00").to_edge(RIGHT)

        self.play(FadeIn(source))
        self.play(FadeIn(interpreter))
        self.play(FadeIn(bytecode))
        self.play(FadeIn(output))

        # Move arrows
        arrow1 = Arrow(source.get_right(), interpreter.get_left(), buff=0.1, color="#FFD43B")
        arrow2 = Arrow(interpreter.get_right(), bytecode.get_left(), buff=0.1, color="#FFD43B")
        arrow3 = Arrow(bytecode.get_right(), output.get_left(), buff=0.1, color="#FFD43B")

        self.play(Create(arrow1))
        self.play(Create(arrow2))
        self.play(Create(arrow3))

        # Animate code line moving
        code_line = Text('print("Bonjour")', color=WHITE).scale(0.7).next_to(source, DOWN)
        self.play(code_line.animate.move_to(output.get_bottom() + DOWN*0.5))
        self.wait(1)

