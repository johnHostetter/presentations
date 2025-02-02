from manim import *

from manim_beamer.bibtex import BibTexManager
from manim_beamer.slides import SlideWithBlocks
from manim_beamer.blocks import AlertBlock, ExampleBlock
from manim_beamer.lists import ItemizedList, AdvantagesList, DisadvantagesList
from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class Conclusion(SlideWithBlocks):
    """
    Create a slide with two blocks: one for the advantages and one for the disadvantages of
    deep neural networks (DNNs).

    Returns:
        The slide with the two blocks.
    """

    def __init__(self):
        example_block = ExampleBlock(
            title="Overall Contributions",
            content=AdvantagesList(
                items=[
                    VGroup(
                        Tex(
                            r"NFNs' structure \& parameters are designed according to gradient descent",
                            color=BLACK, font_size=42
                        )
                    ),
                    VGroup(
                        Tex(
                            "Can easily work online or offline with other neural networks",
                            color=BLACK, font_size=42
                        )
                    ),
                    VGroup(
                        Tex(
                            "Hierarchical NFNs are possible (as done here)", color=BLACK, font_size=42
                        )
                    ),
                    VGroup(
                        Tex("Recurrent NFNs are possible (future work)", color=BLACK, font_size=42)
                    ),
                    VGroup(
                        Tex("As well as the usual advantages of NFNs:", color=BLACK, font_size=42)
                    ),
                    ItemizedList(
                        items=[
                            VGroup(Tex("Transparent", color=BLACK, font_size=36)),
                            VGroup(
                                Tex(
                                    "Sample efficient (if initialized well)",
                                    color=BLACK,
                                    font_size=36,
                                )
                            ),
                            VGroup(
                                Tex(
                                    "Robust to missing values (not shown here)",
                                    color=BLACK,
                                    font_size=36,
                                )
                            ),
                        ]
                    ),
                ]
            ),
        )
        alert_block = AlertBlock(
            title="Future Work",
            content=DisadvantagesList(
                items=[
                    VGroup(Tex(r"Computationally expensive", color=BLACK, font_size=42)),
                    ItemizedList(
                        items=[
                            VGroup(
                                Tex(
                                    "Hadamard product performance bottleneck",
                                    color=BLACK,
                                    font_size=36,
                                ),
                            ),
                            VGroup(
                                Tex(
                                    "Large memory footprint", color=BLACK, font_size=36
                                ),
                            ),
                        ]
                    ),
                    VGroup(
                        Tex(r"Rule Simplification", color=BLACK, font_size=42)
                    ),
                    # "Removal of fuzzy sets or fuzzy logic rules is not explored",
                    ItemizedList(
                        items=[
                            VGroup(
                                Tex(
                                    "A plethora of possible solutions are already published",
                                    color=BLACK,
                                    font_size=36,
                                ),
                            ),
                            VGroup(
                                Tex(
                                    "Future work: explore these solutions",
                                    color=BLACK,
                                    font_size=36,
                                ),
                            ),
                        ]
                    ),
                ]
            ),
        )
        super().__init__(
            title="Conclusion",
            subtitle=None,
            blocks=[example_block, alert_block],
        )


if __name__ == "__main__":
    Conclusion().render()
