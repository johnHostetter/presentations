from manim import *
from manim_beamer.slides import SlideShow, SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

from src.oral_proposal.introduction.dnn import (
    pros_and_cons as dnn_pros_and_cons,
)
from src.oral_proposal.introduction.nfn import (
    pros_and_cons as nfn_pros_and_cons,
)
from src.oral_proposal.introduction.proposal import get_proposal

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def defense_outline() -> SlideWithList:
    """
    Create a slide with my proposed studies for the completion of my dissertation.

    Returns:
        The slide with a list of studies.
    """
    return SlideWithList(
        title="Outline",
        subtitle=None,
        width_buffer=12.0,
        beamer_list=ItemizedList(
            items=[
                VGroup(Tex("Introduction \& Background", color=BLACK, font_size=42)),
                VGroup(
                    Tex(
                        "Prior Research in Existing Construction Paradigms",
                        color=BLACK,
                        font_size=42,
                    ),
                ),
                BL(
                    items=[
                        VGroup(Tex("I: Translation", color=BLACK, font_size=36)),
                        VGroup(Tex("II: Self-Organization", color=BLACK, font_size=36)),
                    ]
                ),
                VGroup(
                    Tex(
                        "A New Construction Paradigm",
                        color=BLACK,
                        font_size=42,
                    ),
                ),
                BL(
                    items=[
                        VGroup(Tex("III: Concurrent Optimization", color=BLACK, font_size=36)),
                    ]
                ),
                VGroup(
                    Tex(
                        "Conclusion",
                        color=BLACK,
                        font_size=42,
                    ),
                ),
            ]
        ),
    )


class DefenseMotivation(SlideShow):
    def __init__(self, **kwargs):
        super().__init__(
            slides=[
                dnn_pros_and_cons(),
                nfn_pros_and_cons(),
                # get_proposal(),
                defense_outline(),
            ],
            **kwargs
        )


if __name__ == "__main__":
    DefenseMotivation().render()
