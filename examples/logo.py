from manim import *

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class PySoftLogo(MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # background = ImageMobject("background.png").scale(2).set_color("#FFFFFF")
        # self.add(background)

    def construct(self):
        # load the PySoft logo as a manim SVGMobject
        logo = SVGMobject(
            get_project_root() / "assets" / "logo" / "bolder_italicized_vector_icon.svg"
        )
        introduction = (
            Text("Powered by", font="TeX Gyre Termes").scale(0.7).next_to(logo, UP)
        )
        introduction.set_color("#000000")
        # introduction.set_stroke(width=1.0)  # uncomment to add a stroke to the text
        introduction.set_fill("#FFFFFF")
        self.play(Write(introduction), run_time=3)

        # add the logo to the scene
        self.play(Create(logo, run_time=2))
        self.wait(3)
        self.play(FadeOut(Group(introduction, logo), run_time=2))
        self.wait(2)


if __name__ == "__main__":
    c = PySoftLogo()
    c.render()
