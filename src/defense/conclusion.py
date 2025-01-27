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
            title="Concurrent Optimization of NFNs",
            content=AdvantagesList(
                items=[
                    "NFNs can be designed according to gradient descent",
                    "This works online or offline",
                    "Can easily work with other neural networks",
                    "Hierarchical NFNs are possible (as shown here)",
                    "Recurrent NFNs are possible (future work)",
                    "As well as the usual advantages of NFNs:",
                    ItemizedList(
                        items=[
                            'Transparent',
                            "Sample efficient (if initialized well)",
                            "Robust to missing values (not shown here)",
                        ]
                    ),
                ]
            ),
        )
        alert_block = AlertBlock(
            title="Current Limitations",
            content=DisadvantagesList(
                items=[
                    "Computationally expensive",
                    ItemizedList(
                        items=[
                            "Hadamard product performance bottleneck",
                            "Large memory footprint",
                        ]
                    ),
                    "Removal of fuzzy sets or fuzzy logic rules is not explored",
                    ItemizedList(
                        items=[
                            "A plethora of possible solutions are already published",
                            "Future work: explore these solutions",
                        ]
                    )
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