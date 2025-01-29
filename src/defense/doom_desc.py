from manim_slides import Slide
from manim import (
    config,
    BLACK,
    WHITE,
    ImageMobject,
    Group,
    Tex,
    RIGHT,
    DOWN,
    VGroup,
    FadeIn,
    FadeOut,
)

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class DOOMDesc(Slide):
    def construct(self):
        cover_art = ImageMobject(
            get_project_root() / "assets" / "images" / "doom_cover_art.jpg"
        ).scale(2)
        tex_str = r"""
        \textbf{DOOM (1993)}\\
        Developed \& published by id Software\\
        Written in C++, open-source, GPL licensed\\
        \vspace{0.5cm}
        First-person, vision-based perspective\\
        Semi-realistic, fast-paced gameplay\\
        Space marine fights humanoid zombies, demons, aliens\\
        """
        tex_desc = Tex(
            tex_str,
            color=BLACK,
            tex_environment="flushleft",
        ).scale(0.5)
        # more_tex_desc = Tex(
        #     more_tex_str,
        #     color=BLACK,
        #     tex_environment="flushleft",
        # ).scale(0.5)
        content = Group(VGroup(tex_desc).arrange(direction=DOWN), cover_art).arrange(
            direction=RIGHT
        )
        self.wait(1)
        self.next_slide()
        self.play(FadeIn(content))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(content))


if __name__ == "__main__":
    DOOMDesc().render()
