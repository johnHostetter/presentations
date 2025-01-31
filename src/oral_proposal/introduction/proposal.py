from typing import Type

from manim import *

from manim_beamer.bibtex import BibTexManager
from manim_beamer.slides import SlideWithBlocks
from manim_beamer.blocks import AlertBlock, ExampleBlock, Block
from manim_beamer.lists import AdvantagesList, DisadvantagesList
from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def get_proposal() -> SlideWithBlocks:
    """
    Create a slide with two blocks: one for the advantages and one for the disadvantages of
    deep neural networks (DNNs).

    Returns:
        The slide with the two blocks.
    """
    bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")

    kwargs = {
        "color": DARK_BLUE,
        "opacity": 0.0,
        "font_size": 30,
    }

    alert_block_1 = AlertBlock(
        title=None,
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex("Difficult \& expensive to design", color=BLACK)
                ),
            ]
        ),
    )
    example_block_1 = ExampleBlock(
        title=None,
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex("Data-driven construction", color=BLACK),
                    bib.slide_short_cite("hostetter2023leveraging", abbrev=True, kwargs=kwargs),
                    bib.slide_short_cite("hostetter2023latent", abbrev=True, kwargs=kwargs),
                ).arrange(RIGHT, buff=0.1),
            ]
        ),
    )
    alert_block_2 = AlertBlock(
        title=None,
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex("Unable to readily adapt to changes", color=BLACK),
                )
            ]
        ),
    )
    example_block_2 = ExampleBlock(
        title=None,
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex("Capable of adding new knowledge just in time", color=BLACK),
                    bib.slide_short_cite("hostetter2023self", abbrev=True, kwargs=kwargs),
                ),
            ]
        ),
    )
    alert_block_3 = AlertBlock(
        title=None,
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex("NFN research is often specific to a certain task", color=BLACK),
                )
            ]
        ),
    )

    example_block_3 = ExampleBlock(
        title=None,
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex(
                        "A task-independent solution (i.e., gradient-based learning)",
                        color=BLACK
                    ),
                    Tex("$[$This Dissertation$]$", **kwargs)
                ).arrange(RIGHT, buff=0.1),
            ]
        ),
    )

    # gather all the blocks together
    blocks: List[Type[Block]] = [
        alert_block_1,
        example_block_1,
        alert_block_2,
        example_block_2,
        alert_block_3,
        example_block_3,
    ]

    return SlideWithBlocks(
        title="Overall Proposal",
        subtitle="Address each major disadvantage of NFNs",
        blocks=blocks,
    )


def pad_block_text_with_spacing(blocks):
    # get the max length of the text content (assuming only first item is used) in each block
    max_len = max([len(block.content.items[0]) for block in blocks])
    for block in blocks:
        curr_len = len(block.content.items[0])
        # pad the content with spaces to make them all the same length
        if curr_len < max_len:
            block.content.items[0] += " " * (max_len - curr_len)

    return blocks


if __name__ == "__main__":
    beamer_slide = get_proposal()
    beamer_slide.render()
