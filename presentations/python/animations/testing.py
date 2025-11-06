from manim import * 
class code(Scene):
    def construct(self):
        code_snippet = '''
            for i in range(0, 4):
                for j in range(i+1, 4):
                    print(i, j)
        '''
        code = Code(
            code_string=code_snippet,
            tab_width=4,
            background="window",
            language="Python",
            ).scale(1.25) 
        self.play(Write(code))
        self.wait(3)
        code.code_string = 'import math'
        self.play(Write(code))
        self.wait(3)
