from manim import *
from math import *

class EulersFormula(Scene):
    """A scene for the Eulers formula animation.
    
    In Manim, a Scene is a fundamental building block for creating animations. Every animation must be contained within a Scene subclass. The Scene class provides the canvas and basic infrastructure needed for rendering animations.
    """
    def construct(self):
        """A construct method to define what happenes within your scene. 
        
        REQUIRED for every scene & Manim will automatically call it when rendering an animation.
        """
        self.wait() # from manim source code DEFAULT_WAIT_TIME = 1.0
        self.play(
            Write(
                title := Title("Eulers formula")
                .add_background_rectangle(color=BLACK, opacity=1)
                .to_edge(UP)
            )
        )

        self.play(
            Create(
                formula := MathTex(r"e^{i\theta} = cos\theta + i\times sin\theta") # raw string for proper LaTeX rendering
                .next_to(title, DOWN)
                .add_background_rectangle(color=BLACK, opacity=1)
            )
        )
        
        # When you add a Mobject to the scene (either with Scene.add or Scene.play), Manim adds that Mobject to a list called Scene.mobjects in the order in which they are added in the code, and by default, to all Mobjects they are assigned a z_index = 0.
        
        self.play(
            DrawBorderThenFill(
                cpl := ComplexPlane()
                .set_style(
                    stroke_width=1.2,
                    stroke_opacity=0.8,
                    background_stroke_width=0.7,
                    background_stroke_opacity=0.4,
                )
                .set_z_index(-2) # placing the plane below all else
                .add_coordinates()
            )
        )

        self.play(Create(ucirc := Circle(radius=1).set_z_index(-1)))
        origin_before_scaling = cpl.c2p(0, 0)

        self.play(
            VGroup(cpl, ucirc).animate.scale(1.7),
            ShrinkToCenter(VGroup(title, formula)),
        )

        self.play(VGroup(cpl, ucirc).animate.shift(origin_before_scaling - cpl.c2p(0, 0))) # fixing the shift that occurs with scaling to align the center of the scaled objects with ORIGIN ( from manim source code ORIGIN: Vector3D = np.array((0.0, 0.0, 0.0)) )

        k = ValueTracker(0)

        e = always_redraw(
            lambda: Dot(cpl.n2p(cos(v := k.get_value()) + sin(v) * 1j), color=WHITE),
        )

        vec = always_redraw(lambda: Line(ORIGIN, e, stroke_width=2.3))

        ang = always_redraw(
            lambda: Angle(
                Line(ORIGIN, Point().set_x(1).set_y(0)), # creating a horizontal line to mesure the angle between `vec` and the real axis
                vec,
                radius=0.5,
                color=WHITE,
                stroke_width=1.75
            )
        )

        e_lbl = always_redraw(
            lambda: MathTex(rf"e^{{ i{k.get_value():.3f} }}").next_to(e) # {{ }} for proper display of the power of e inside an f string within MathTex
        )

        self.play(Create(VGroup(e, vec, ang)), Write(e_lbl))
        self.wait()

        self.play(k.animate.set_value(pi / 4), run_time=3)
        self.wait(1.5)

        eq_lbl = always_redraw(
            lambda: VGroup( # dividing the equation label into separate vectors to color certain parts of it in accordance with the animation
                MathTex(rf"{cos(v := k.get_value()):.3f}").set_color(YELLOW_D),
                MathTex(r"+ i\times ("),
                MathTex(rf"{sin(v):.3f}").set_color(TEAL_D),
                MathTex(r")"),
            )
            .arrange_submobjects(RIGHT, buff=0.1)
            .to_corner(UL)
        )

        sp = always_redraw(lambda: Dot(color=TEAL_D).set_y(e.get_y()))
        cp = always_redraw(lambda: Dot(color=YELLOW_D).set_x(e.get_x()))

        sine = always_redraw(lambda: Line(e, sp, stroke_color=TEAL_B, stroke_width=2.7))

        cosine = always_redraw(
            lambda: Line(e, cp, stroke_color=YELLOW_B, stroke_width=2.7)
        )

        self.play(Create(eq_lbl), Uncreate(ang))
        self.play(Create(VGroup(sp, sine)), run_time=1)
        self.play(Create(VGroup(cp, cosine)), run_time=1)
        self.play(k.animate.set_value(pi * 9 / 4), run_time=12) # setting k to nine fourth of pi in order to return e to its starting point

        self.play(Create(ang))
        self.wait(2)

        self.play(Uncreate(eq_lbl))
        self.play(Uncreate(VGroup(sine, sp, cosine, cp, ang)), run_time=2)
        self.play(Uncreate(VGroup(vec, e_lbl, e)), run_time=1.2)
        self.wait()

        self.play(VGroup(ucirc, cpl).animate.scale(0.58))
        self.wait(1.5)

        self.play(Uncreate(ucirc))
        self.play(FadeOut(cpl))
        self.wait(0.5)

        self.play(
            Write(
                the_end := Title(
                    "Mathematics is the gate and key to the sciences",
                    include_underline=False,
                ).center()
            )
        )
        self.wait(2.5)
        self.play(ShrinkToCenter(the_end))