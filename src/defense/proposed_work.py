from manim import *

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class Proposal(SlideWithList):
    """
    Create a slide with my proposed studies for the completion of my dissertation.

    Returns:
        The slide with a list of studies.
    """

    def __init__(self):
        myTemplate = TexTemplate()
        # myTemplate.add_to_preamble(r"\usepackage{soul, color}")
        # myTemplate.add_to_preamble(r"\usepackage{xcolor}")
        # myTemplate.add_to_preamble(r"\definecolor{darkseagreen}{rgb}{0.56, 0.74, 0.56}")
        # myTemplate.add_to_preamble(r"\newcommand\highlight[2]{\colorbox{#1}{\textcolor{#2}{#3}}}")
        # myTemplate.add_to_preamble(r"\newcommand\rev[1]{\highlight{yellow}{red}{#1}}")

        super().__init__(
            title="Proposed Work",
            subtitle=None,
            beamer_list=BL(
                items=[
                    VGroup(
                        Tex(
                            # r"\textbf{\colorbox{darkseagreen}{\strut Computer vision}:}",
                            # r"\sethlcolor{cyan} \hl{\textbf{Computer vision:}}",
                            r"\textbf{Computer Vision:}",
                            color=BLACK,
                            font_size=42,
                            tex_environment="flushleft",
                            tex_template=myTemplate,
                        ),
                    ),
                    ItemizedList(
                        items=[
                            VGroup(
                                Tex(
                                    "Shown in the video game called DOOM",
                                    color=BLACK,
                                    font_size=36,
                                    tex_environment="flushleft",
                                )
                            ),
                        ]
                    ),
                    VGroup(
                        Tex(
                            r"\textbf{Hierarchical NFN:}",
                            color=BLACK,
                            font_size=42,
                            tex_environment="flushleft",
                        )
                    ),
                    ItemizedList(
                        items=[
                            VGroup(
                                Tex(
                                    "Tested in this dissertation",
                                    color=BLACK,
                                    font_size=36,
                                    tex_environment="flushleft",
                                )
                            )
                        ]
                    ),
                    VGroup(
                        Tex(
                            r"\textbf{Neural Architecture Search:}",
                            color=BLACK,
                            font_size=42,
                            tex_environment="flushleft",
                        )
                    ),
                    ItemizedList(
                        items=[
                            VGroup(
                                Tex(
                                    "Explored the impact of different possible configurations",
                                    color=BLACK,
                                    font_size=36,
                                    tex_environment="flushleft",
                                ),
                            ),
                        ]
                    ),
                    VGroup(
                        Tex(
                            r"\textbf{Left for Future Work:}",
                            color=BLACK,
                            font_size=42,
                            tex_environment="flushleft",
                        )
                    ),
                    ItemizedList(
                        items=[
                            VGroup(
                                Tex(
                                    r"Prove universal approximation property",
                                    color=BLACK,
                                    font_size=36,
                                    tex_environment="flushleft",
                                ),
                            ),
                            VGroup(
                                Tex(
                                    "Applications in e-learning or healthcare",
                                    color=BLACK,
                                    font_size=36,
                                    tex_environment="flushleft",
                                )
                            ),
                        ]
                    ),
                ]
            ),
        )


if __name__ == "__main__":
    Proposal().render()
