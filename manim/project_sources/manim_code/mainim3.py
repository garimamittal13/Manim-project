
from manim import *

class Formula(Scene):
    def construct(self):
        # Heading
        heading = Text(
            "ENCODING/DECODING TIMES AND BANDWIDTH", 
            font_size=40,
            weight=BOLD,
            t2c={"ENCODING/DECODING TIMES AND BANDWIDTH": YELLOW}
        ).to_edge(UP)

        # Upper text
        text = Text(
            "Measuring the time needed to encode/decode an FEC block of a certain erasure code class (RS, LDPC) is useful for computing\nthe achievable bandwidth in a real-time streaming system and the suitability of such codes for\nresource-constrained wireless terminals. This bandwidth is calculated as follows:\n", 
            font_size=29, 
            t2c={"FEC": BLUE}
        ).to_edge(UP)

        text.set_width(self.camera.frame_width - 0.5)

        # Formula
        formula = MathTex(
            "BW = \\frac{n \\cdot \\text{pkt size (in bits)}}{\\text{time}}"
        ).set_color(BLUE).scale(1.5)

        # Arrange text and formula vertically
        group = VGroup(heading, text, formula).arrange(DOWN)

        # Animation
        self.play(Write(heading), run_time=2)
        self.play(Write(text), run_time=5)
        self.wait(1)
        self.play(Write(formula), run_time=3)
        self.wait(3)