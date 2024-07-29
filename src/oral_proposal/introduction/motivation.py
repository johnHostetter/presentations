from manim import *

from manim_beamer.slides import SlideShow
from src.oral_proposal.introduction.dnn import (
    pros_and_cons as dnn_pros_and_cons,
)
from src.oral_proposal.introduction.nfn import (
    pros_and_cons as nfn_pros_and_cons,
)
from src.oral_proposal.introduction.proposal import get_proposal
from src.oral_proposal.introduction.outline import get_outline

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class Motivation(SlideShow):
    def __init__(self, **kwargs):
        super().__init__(
            slides=[
                dnn_pros_and_cons(),
                nfn_pros_and_cons(),
                get_proposal(),
                get_outline(),
            ],
            **kwargs
        )


if __name__ == "__main__":
    Motivation().render()
