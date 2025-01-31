from manim import *

from manim_beamer.slides import SlideWithBlocks
from manim_beamer.lists import AdvantagesList, DisadvantagesList
from manim_beamer.blocks import AlertBlock, ExampleBlock, RemarkBlock

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def issue_with_logits() -> SlideWithBlocks:
    """
    Create a slide discussing why we need to modify the Gumbel-Max Trick.

    Returns:
        The slide with the issue, remark and proposed solution.
    """
    alert_block = AlertBlock(
        title="Issue",
        content=DisadvantagesList(
            items=["NFN cannot have real-numbered weight matrices."]
        ),
    )
    remark_block = RemarkBlock(
        title="Remark",
        content="The Gumbel Max Trick (GMT) allows us to differentiably sample from a\n"
        "categorical distribution.",
    )
    example_block = ExampleBlock(
        title="Proposed Solution",
        content=AdvantagesList(
            items=[
                "Use GMT to modify NFNs' structure.",
                VGroup(
                    MathTex(r"\tilde{\mathbf{I}}", color=BLACK),
                    Text(
                        " are logits or raw non-normalized probabilities.", color=BLACK
                    ),
                ),
                VGroup(
                    Text("Differentiably sample from ", color=BLACK),
                    MathTex(r"\tilde{\mathbf{I}}", color=BLACK),
                    Text(" to yield ", color=BLACK),
                    MathTex(r"\mathbf{I}.", color=BLACK),
                ),
            ]
        ),
    )
    return SlideWithBlocks(
        title="The Gumbel-Max Trick",
        subtitle=None,
        blocks=[alert_block, remark_block, example_block],
    )


if __name__ == "__main__":
    issue_with_logits().render()
