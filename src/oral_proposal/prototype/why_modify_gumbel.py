from manim import *

from manim_beamer.slides import SlideWithBlocks
from manim_beamer.blocks import AlertBlock, ExampleBlock, RemarkBlock

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def why_modify_gumbel() -> SlideWithBlocks:
    """
    Create a slide discussing why we need to modify the Gumbel-Max Trick.

    Returns:
        The slide with the issue, remark and proposed solution.
    """
    alert_block = AlertBlock(
        title="Suspected Issue",
        content="Naively applying Gumbel-Max Trick might not work.",
    )
    remark_block = RemarkBlock(
        title="Reason",
        content="It may violate ϵ-completeness by sampling poorly activated rules.",
    )
    example_block = ExampleBlock(
        title="Proposed Solution",
        content="Constrain the Gumbel-Max Trick to abide by it.",
    )
    return SlideWithBlocks(
        title="Constraining the Gumbel-Max Trick",
        subtitle=None,
        blocks=[alert_block, remark_block, example_block],
    )


if __name__ == "__main__":
    why_modify_gumbel().render()
