from manim import *

class IndentationAnimation(Scene):
    def construct(self):
        # Define the incorrectly indented code
        wrong_code_str = """def calculate_sum(a, b):
    result = a + b
        return result
    print("Sum:", calculate_sum(5, 3))
"""

        # Define the correctly indented code
        correct_code_str = """def calculate_sum(a, b):
    result = a + b
    return result
print("Sum:", calculate_sum(5, 3))
"""

        # Create Code objects for both versions
        wrong_code = Code(
            code_string=wrong_code_str,
            tab_width=4,
            background="window",
            language="python"
        )
        correct_code = Code(
            code_string=correct_code_str,
            tab_width=4,
            background="window",
            language="python"
        )

        # Step 1: Display the wrong code
        self.play(Create(wrong_code))
        self.wait(2)

        # Step 2: Highlight incorrect indentation lines in red
        code_lines = wrong_code.submobjects[1]  # VGroup of code lines
        error_line_indices = [2, 3]  # Lines with incorrect indentation (0-based indexing)
        for idx in error_line_indices:
            self.play(
                code_lines[idx].animate.set_color(RED).set_opacity(0.9),
                run_time=0.5
            )
        self.wait(2)

        # Step 3: Morph to the correct code
        self.play(Transform(wrong_code, correct_code))
        self.wait(2)

        # Step 4: Fade out the correct code
        self.play(FadeOut(correct_code))
        self.wait(1)
