from manim import *

class NumberBlocksExtended(Scene):
    def construct(self):
        # Create a gradient background
        background = Rectangle(width=config.frame_width, height=config.frame_height)
        background.set_fill(color=[BLACK, BLACK], opacity=1)

        background.add_updater(
            lambda bg, dt: bg.become(
                Rectangle(width=config.frame_width, height=config.frame_height)
                .set_fill(color=[BLACK, BLACK], opacity=1)
                .shift(0.1 * dt * UP)  # Slow upward shift
            )
        )
        self.add(background)  # Add dynamic background to the scene

        # Create number blocks
        blocks = [Square(side_length=1, fill_color=BLUE_E, fill_opacity=1) for _ in range(4)]
        numbers = [Text(str(num), color=WHITE, font_size=36) for num in [2, 4, 3, 1]]
        indices = [Text(str(index), color=WHITE, font_size=24) for index in range(1, 5)]
        ab = [Text(str(index), color=WHITE, font_size=24) for index in range(5, 7)]
        
        # Position blocks and numbers
        positions = [3*LEFT + 1*UP, 1*LEFT + 1*UP, 1*RIGHT + 1*UP, 3*RIGHT + 1*UP]
        for block, number, position in zip(blocks, numbers, positions):
            block.move_to(position)
            number.move_to(position)
            

        # Fade in each block one by one
        for block, number in zip(blocks, numbers):
            self.play(FadeIn(block, shift=DOWN, scale=0.5), runtime=0.5)
            self.play(Write(number), runtime=0.5)

        # Transition: Shift all blocks to the left
        self.play(*[block.animate.shift(2 * LEFT) for block in blocks],
                  *[number.animate.shift(2 * LEFT) for number in numbers],
                  run_time=1)

        # Adding new blocks with question marks
        question_blocks = [Square(side_length=1, fill_color=LOGO_BLACK, fill_opacity=1) for _ in range(2)]
        question_marks = [Text("?", color=WHITE, font_size=36) for _ in range(2)]
        question_positions = [3*RIGHT + 1*UP, 5*RIGHT + 1*UP]

        for block, mark, position in zip(question_blocks, question_marks, question_positions):
            block.move_to(position)
            mark.move_to(position)
            self.add(block, mark)

        # Adding curly bracket and label
        brace = BraceBetweenPoints(
            question_blocks[0].get_corner(DOWN+LEFT), 
            question_blocks[1].get_corner(DOWN+RIGHT), 
            DOWN,
            buff=SMALL_BUFF  # Add a small buffer to lower the brace
        )
        k_label = Text("k = 2", color=WHITE, font_size=36).next_to(brace, DOWN, buff=SMALL_BUFF)

        # Show new elements
        self.play(
            *[FadeIn(block, shift=DOWN, scale=0.5) for block in question_blocks],
            *[Write(mark) for mark in question_marks],
            GrowFromCenter(brace),
            Write(k_label),
            run_time=1
        )
        
        for index, block in zip(indices, blocks):
            index.move_to(block.get_center() + UP*1.1)
            self.play(FadeIn(index, shift=DOWN*0.5), runtime=0.2)

        for index, block in zip(ab, question_blocks):
            index.move_to(block.get_center() + UP*1.1)
            self.play(FadeIn(index, shift=DOWN*0.5), runtime=0.2)
            
        label1 = [Text(f"m{i}", color=WHITE, font_size=24) for i in range(1, 5)]
        label2 = [Text(f"m{i}", color=WHITE, font_size=24) for i in range(5, 7)]
        for label, index, block in zip(label1, indices, blocks):
            label.move_to(block.get_center() + UP*1.1)
            #self.play(ReplacementTransform(index, label), run_time=0.5)
        for label, index, block in zip(label2, ab, question_blocks):
            label.move_to(block.get_center() + UP*1.1)
            #self.play(ReplacementTransform(index, label), run_time=0.5)
        self.play(
            *[ReplacementTransform(index, label) for index, label in zip(indices, label1)],
            *[ReplacementTransform(index, label) for index, label in zip(ab, label2)],
            run_time=0.5
        )
        
        brace_top = BraceBetweenPoints(blocks[0].get_corner(UP+LEFT), question_blocks[-1].get_corner(UP+RIGHT), UP, buff=LARGE_BUFF)
        text_above_brace = Text("p > m(i)", color=WHITE, font_size=24).next_to(brace_top, UP, buff=SMALL_BUFF)
        
        # Animate the appearance of the top brace and text
        self.play(GrowFromCenter(brace_top), run_time=1)
        self.play(Write(text_above_brace), run_time=1)
        
        self.play(FadeOut(brace_top), FadeOut(text_above_brace), FadeOut(brace), FadeOut(k_label), run_time = 1)

        # Vertical transition of all blocks to the right and then down
        total_blocks = blocks + question_blocks
        total_numbers = numbers + question_marks
        total_labels = label1 + label2
        target_position = 3 * (UP+RIGHT)  # Top of the vertical stack
        vertical_spacing = 1.2  # Space between blocks vertically

        # Calculate new positions and animate transition
        animations = []
        for i, (block, number, label) in enumerate(zip(total_blocks, total_numbers, total_labels)):
            # Calculate new vertical positions for blocks, numbers, and labels
            new_pos = target_position + i * DOWN * vertical_spacing
            animations.append(block.animate.move_to(new_pos))
            animations.append(number.animate.move_to(new_pos))
            animations.append(FadeOut(label, run_time=1.0))
            
        self.play(*animations, run_time=2)
        function_texts = [
            f"f({i}) = m{i+1}" for i in range(len(total_blocks))
        ]
        function_labels = [
            Text(text, color=WHITE, font_size=24) for text in function_texts
        ]

        # Position blocks initially off-screen to the right
        for block, number in zip(total_blocks, total_numbers):
            block.shift(2 * RIGHT)
            number.move_to(block.get_center())
            self.add(block, number)

        # Transition blocks from right to left into their positions
        target_x = 4 * LEFT  # Final x position for the right-most block
        target_y = 3 * UP  # Starting y position
        for i, (block, number, label) in enumerate(zip(total_blocks, total_numbers, function_labels)):
            new_position = target_x + target_y + (i * DOWN * 1.2)
            self.play(
                block.animate.move_to(new_position),
                number.animate.move_to(new_position),
                run_time=0.5
            )
            # Position the function labels to the left of blocks
            label.next_to(block, LEFT)
            self.play(FadeIn(label), run_time=0.5)
            
            
        # Define points
        axes = Axes(
            x_range=[0, 6, 1],  # x goes from 0 to 6
            y_range=[0, 5, 1],  # y goes from 0 to 5
            x_length=8,  # Length of the x axis
            y_length=6,  # Length of the y axis
            axis_config={"color": WHITE}
        )
        
        # Define points relative to the axes scale
        points = [
            axes.c2p(0, 2),
            axes.c2p(1, 4),
            axes.c2p(2, 3),
            axes.c2p(3, 1),
            axes.c2p(4, 0),
            axes.c2p(5, 2)
        ]

        # Create dots for each point
        dots = VGroup(*[Dot(point=point, radius=0.1, color=GREEN) for point in points])

        # Labels for each dot
        labels = VGroup(*[Text(f"({int(p[0])}, {int(p[1])})", font_size=24).next_to(dot, UP) for dot, p in zip(dots[:4], [(0, 2), (1, 4), (2, 3), (3, 1)])])
        function_label1 = VGroup(*[Text(f"({int(p[0])}, f({int(p[0])}))", font_size=24).next_to(dot, DOWN) for dot, p in zip(dots[4:], [(4, 0), (5, 2)])])
        
        # Combine all labels for convenience
        all_labels = VGroup(*labels, *function_label1)
        
        # Connect dots with a smooth curve
        curve = VMobject(color=GREEN)
        curve.set_points_smoothly([dot.get_center() for dot in dots])

        # Create labels for axes
        x_label = Text("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y").next_to(axes.y_axis.get_end(), UP)

        # Grouping all graph components
        graph = VGroup(axes, curve, dots, all_labels, x_label, y_label)
        graph.move_to(RIGHT * 2)  # Center the graph on the right side of the screen

        # Adding all components to the scene
        self.play(FadeIn(axes, shift=DOWN), run_time=1)
        #self.play(FadeIn(graph), run_time=1)

        # Draw curve smoothly from start to end
        self.play(Create(curve, run_time=2))

        # Gradually show dots and their labels
        for dot, label in zip(dots, all_labels):
            self.play(
                FadeIn(dot, scale=0.5),  # Fade in and grow effect for dots
                Write(label),            # Write labels one by one
                run_time=1
            )

        # Finally, show the axis labels
        self.play(
            Write(x_label),
            Write(y_label)
        )

        # Smoothly fade out the entire graph
        self.play(FadeOut(graph), run_time=1)
        
        for label in function_labels:
            self.play(FadeOut(label), run_time=0.5)
            
        target_x = 5 * LEFT  # Final x position for the right-most block
        target_y = 3 * UP  # Starting y position
        for i, (block, number, label) in enumerate(zip(total_blocks, total_numbers, function_labels)):
            new_position = target_x + target_y + (i * DOWN * 1.2)
            self.play(
                block.animate.move_to(new_position),
                number.animate.move_to(new_position),
                run_time=0.5
            )
        missing_blocks = [total_blocks[1], total_blocks[4]]  # Indices for f(2) and f(4)
        for block in missing_blocks:
            self.play(block.animate.set_fill(BLACK, opacity=0.5), run_time=0.5)
        
        axes = Axes(
            x_range=[0, 6, 1],  # x goes from 0 to 6
            y_range=[0, 5, 1],  # y goes from 0 to 5
            x_length=8,  # Length of the x axis
            y_length=6,  # Length of the y axis
            axis_config={"color": WHITE}
        )
        
        # Define points relative to the axes scale
        points = [
            axes.c2p(0, 2),
            axes.c2p(1, 4),
            axes.c2p(2, 3),
            axes.c2p(3, 1),
            axes.c2p(4, 0),
            axes.c2p(5, 2)
        ]
        
        points2 = [
            axes.c2p(0, 2),
            axes.c2p(2, 3),
            axes.c2p(3, 1),
            axes.c2p(5, 2)
        ]

        # Create dots for each point
        dots = VGroup(*[Dot(point=point, radius=0.1, color=GREEN) for point in points])

        # Labels for each dot
        #labels = VGroup(*[Text(f"({int(p[0])}, {int(p[1])})", font_size=24).next_to(dot, UP) for dot, p in zip(dots[:3], [(0, 2), (2, 3), (3, 1)])])
        labels = VGroup(*[Text(f"({int(p[0])}, {int(p[1])})", font_size=24).next_to(dot, UP) for dot, p in [(dots[0],(0,2)),(dots[2],(2,3)),(dots[3],(3,1))]])
        function_label1 = VGroup(*[Text(f"({int(p[0])}, f({int(p[0])}))", font_size=24).next_to(dot, DOWN) for dot, p in zip(dots[5:], [(5, 2)])])
        
        # Combine all labels for convenience
        all_labels = VGroup(*labels, *function_label1)
        
        # Connect dots with a smooth curve
        curve = VMobject(color=GREEN)
        curve.set_points_smoothly([dot.get_center() for dot in dots])

        # Create labels for axes
        x_label = Text("x").next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y").next_to(axes.y_axis.get_end(), UP)

        # Grouping all graph components
        graph = VGroup(axes, curve, dots, all_labels, x_label, y_label)
        graph.move_to(RIGHT * 2)  # Center the graph on the right side of the screen
        
        self.play(FadeIn(axes, shift=DOWN), run_time=1)
        #self.play(FadeIn(graph), run_time=1)

        # Draw curve smoothly from start to end
        self.play(Create(curve, run_time=2))

        # Gradually show dots and their labels
        for dot, label in zip(dots, all_labels):
            self.play(
                FadeIn(dot, scale=0.5),  # Fade in and grow effect for dots
                Write(label),            # Write labels one by one
                run_time=1
            )

        # Finally, show the axis labels
        self.play(
            Write(x_label),
            Write(y_label)
        )
        target_point1 = axes.c2p(1, 4)
        horizontal_start1 = axes.c2p(0, 4)
        vertical_start1 = axes.c2p(1, 0)
        
        target_point2 = axes.c2p(4, 0)
        horizontal_start2 = axes.c2p(0, 0)
        vertical_start2 = axes.c2p(4, 0)

        # Create horizontal and vertical lines to the target point
        horizontal_line1 = Line(horizontal_start1, target_point1, color=BLUE, stroke_width=4)
        vertical_line1 = Line(vertical_start1, target_point1, color=RED, stroke_width=4)
        
        horizontal_line2 = Line(horizontal_start2, target_point2, color=BLUE, stroke_width=4)
        vertical_line2 = Line(vertical_start2, target_point2, color=RED, stroke_width=4)

        # Play the animation for drawing lines
        self.play(Create(horizontal_line1), run_time=1)
        self.play(Create(vertical_line1), run_time=1)

        # Create a dot at the intersection point
        dot1 = Dot(target_point1, color=YELLOW, radius=0.1)

        # Label for the dot
        label1 = Text(f"(1, 4)", font_size=24).next_to(dot1, UP)

        # Display the dot and its label
        self.play(FadeIn(dot1), Write(label1), run_time=1)
        self.wait(1)

        self.play(Create(horizontal_line2), run_time=1)
        self.play(Create(vertical_line2), run_time=1)

        # Create a dot at the intersection point
        dot2 = Dot(target_point2, color=YELLOW, radius=0.1)

        # Label for the dot
        label2 = Text(f"(4, 0)", font_size=24).next_to(dot2, UP)

        # Display the dot and its label
        self.play(FadeIn(dot2), Write(label2), run_time=1)
        self.wait(1)
        
        self.play(Unwrite(label2), Unwrite(label1), FadeOut(dot1), FadeOut(dot2), Uncreate(horizontal_line1), Uncreate(horizontal_line2), Uncreate(vertical_line1), Uncreate(vertical_line2), FadeOut(graph))
        for block, number in zip(total_blocks, total_numbers):
            self.play(FadeOut(number), FadeOut(block))
        # Animation of the lines tracing the graph and forming a rectangle with the axes
        
        self.wait(1)
        
          # Create the number boxes
        numbers = [2, 4, 3, 1]
        boxes = VGroup(*[self.create_number_box(num) for num in numbers])
        boxes.arrange(RIGHT, buff=0.5).to_edge(UP, buff=1)

        # Display the boxes
        self.play(LaggedStart(*[Create(box) for box in boxes], lag_ratio=0.5))
        self.wait(1)

        # Equation Text
        equation = MarkupText(
            "f(x) = 2x<sup>3</sup> + 2 mod 5",
            font_size=36,
            color=WHITE
        )
        equation.next_to(boxes, DOWN)

        # Display the equation
        self.play(Write(equation))
        self.wait(2)
        
            # Values of the function for x = 0, 1, 2, 3, 4, 5
        x_values = list(range(6))
        function_texts = VGroup()
        results_texts = VGroup()

        for x in x_values:
            # Calculate function value
            fx = 2 * x**3 + 2
            function_text = Text(f"f({x}) = {fx}", font_size=24)
            if function_texts:
                function_text.next_to(function_texts[-1], DOWN)
            else:
                function_text.next_to(equation, DOWN, buff=0.5)
            function_texts.add(function_text)

        # Display all function values
        self.play(LaggedStart(*[Write(txt) for txt in function_texts], lag_ratio=0.5))
        self.wait(1)

        # Calculate and display the modulo operation
        for x, ft in zip(x_values, function_texts):
            fx = 2 * x**3 + 2
            fx_mod_5 = fx % 5
            result_text = Text(f"f({x}) = {fx_mod_5} (mod 5)", font_size=24).move_to(ft)

            # Transformation to modulo results
            self.play(Transform(ft, result_text))
            results_texts.add(result_text)
        
        self.wait(2)

    def create_number_box(self, num):
        # Helper function to create a square with a number inside
        box = Square(side_length=1, fill_color=BLUE_E, fill_opacity=1)
        text = Text(str(num), color=WHITE, font_size=36)
        group = VGroup(box, text)
        text.move_to(box.get_center())
        return group

