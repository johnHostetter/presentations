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
                "Introduction & Background",
                "Past Work",
                BL(
                    items=[
                        "I: Translation",
                        "II: Self-Organization",
                    ]
                ),
                "Present Work",
                BL(
                    items=[
                        "III: Concurrent Optimization",
                    ]
                ),
                "Future Work",
            ]
        ),
    )


class DefenseMotivation(SlideShow):
    def __init__(self, **kwargs):
        super().__init__(
            slides=[
                dnn_pros_and_cons(),
                nfn_pros_and_cons(),
                get_proposal(),
                defense_outline(),
            ],
            **kwargs
        )


if __name__ == "__main__":
    DefenseMotivation().render()
