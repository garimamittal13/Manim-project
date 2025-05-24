from manim import *

class Formula(Scene):
    def construct(self):
        # Heading
        heading = Text(
            "REDUNDANCY RATIO", 
            font_size=40,
            weight=BOLD,
            t2c={"REDUNDANCY RATIO": RED}
        ).to_edge(UP)

        # Upper text
        text = Text(
            "The ratio n/k is usually referred to as the stretch factor of a code with error.\n\nThe stretch factor quantifies the amount of redundancy with respect to the source data.", 
            font_size=36, 
            t2c={"n/k": BLUE, "stretch factor": BLUE, "source": BLUE}
        ).to_edge(UP)

        text.set_width(self.camera.frame_width - 0.5)

        # Formula
        formula = MathTex(
            "\\text{Redundancy ratio} = \\frac{n}{k}"
        ).set_color(RED).scale(1)

        # Arrange text and formula vertically
        group = VGroup(heading, text, formula).arrange(DOWN)

        # Animation
        self.play(Write(heading), run_time=2)
        self.play(Write(text), run_time=5)
        self.wait(1)
        self.play(Write(formula), run_time=3)
        self.wait(3)