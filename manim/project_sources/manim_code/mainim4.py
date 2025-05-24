from manim import *

class Formula(Scene):
    def construct(self):
        # Heading
        heading = Text(
            "DECODING INEFFICIENCY RATIO (INEF_RATIO)", 
            font_size=40,
            weight=BOLD,
            t2c={"DECODING INEFFICIENCY RATIO (INEF_RATIO)": YELLOW}
        ).to_edge(UP)

        # Upper text
        text = Text(
            "This represents the minimum number of packets required to recover an FEC block divided by the number of source packets.\n\nTypically, the inef_ratio is equal to one in MDS (explained earlier) codes, while it is slightly higher in non-MDS codes.\n\nIt is calculated as follows:", 
            font_size=40, 
            t2c={"inef_ratio": BLUE, "MDS": BLUE}
        ).to_edge(UP)

        text.set_width(self.camera.frame_width - 0.5)

        # Formula
        formula = MathTex(
            "\\text{inef ratio} = \\frac{\\text{Number of Packets Required for Decoding}}{\\text{Number of source packets}}"
        ).set_color(BLUE).scale(1)

        # Arrange text and formula vertically
        group = VGroup(heading, text, formula).arrange(DOWN)

        # Animation
        self.play(Write(heading), run_time=2)
        self.play(Write(text), run_time=5)
        self.wait(1)
        self.play(Write(formula), run_time=3)
        self.wait(3)

