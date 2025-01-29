from manim_slides import Slide
from manim import (
    config,
    Tex,
    BLACK,
    WHITE,
    VGroup,
    DOWN,
    SVGMobject,
    Create,
    SurroundingRectangle,
)

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class QAndA(Slide):
    def construct(self):
        profile_pic = SVGMobject(
            get_project_root() / "assets" / "people" / "jwh_bw_high.svg",
            color=BLACK,
        ).scale(1.25)
        frame = SurroundingRectangle(profile_pic, color=BLACK, buff=0.1)
        name_and_email = (
            Tex(
                "John Wesley Hostetter",
                "jwhostet@ncsu.edu",
                color=BLACK,
            )
            .scale(0.5)
            .arrange(DOWN)
        )
        my_profile = VGroup(VGroup(profile_pic, frame), name_and_email).arrange(DOWN)

        thank_you_tex = Tex(
            "Thank you for your time and attention.",
            color=BLACK,
        ).scale(0.5)
        questions_tex = Tex(
            "Any questions?",
            color=BLACK,
        ).scale(0.5)
        tex_group = VGroup(thank_you_tex, questions_tex).arrange(DOWN)
        VGroup(my_profile, tex_group).arrange(buff=0.5)

        self.wait(1)
        self.next_slide()
        self.play(Create(my_profile, run_time=1), Create(tex_group, run_time=3))
        self.wait(1)


if __name__ == "__main__":
    c = QAndA()
    c.render()
