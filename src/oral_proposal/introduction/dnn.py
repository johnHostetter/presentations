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


def pros_and_cons() -> SlideWithBlocks:
    """
    Create a slide with two blocks: one for the advantages and one for the disadvantages of
    deep neural networks (DNNs).

    Returns:
        The slide with the two blocks.
    """
    bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")

    example_block = ExampleBlock(
        title="Advantages of DNNs",
        content=AdvantagesList(
            items=[
                "Reliable",
                ItemizedList(
                    items=[
                        VGroup(
                            Tex("Assist students in learning", color=BLACK),
                            bib.slide_short_cite("abdelshiheed2023leveraging"),
                        ).arrange(RIGHT),
                        VGroup(
                            Tex("Predict septic shock", color=BLACK),
                            bib.slide_short_cite("dqn_septic_shock"),
                        ).arrange(RIGHT),
                        VGroup(
                            Tex("Able to solve complex games (e.g., Go)", color=BLACK),
                            bib.slide_short_cite("silver2016mastering"),
                        ).arrange(RIGHT),
                    ]
                ),
                "Flexible",
                ItemizedList(
                    items=[
                        VGroup(
                            Tex("Network morphism (i.e., neurogenesis)", color=BLACK),
                            bib.slide_short_cite("draelos_neurogenesis_2016"),
                            bib.slide_short_cite("maile_when_2022"),
                        ).arrange(RIGHT),
                    ]
                ),
                "Generalizable",
                ItemizedList(
                    items=[
                        VGroup(
                            Tex("Supervised learning", color=BLACK),
                            bib.slide_short_cite(
                                "bolat_interpreting_2020"
                            ),  # nfn paper that uses dnn
                        ).arrange(RIGHT),
                        VGroup(
                            Tex("Online reinforcement learning", color=BLACK),
                            bib.slide_short_cite("jaderberg_reinforcement_2016"),
                        ).arrange(RIGHT),
                        VGroup(
                            Tex("Offline reinforcement learning", color=BLACK),
                            bib.slide_short_cite("levine_offline_2020"),
                        ).arrange(RIGHT),
                        VGroup(Tex("and more...", color=BLACK)).arrange(RIGHT),
                    ],
                ),
            ]
        ),
        default_m_object=Tex,
    )

    alert_block = AlertBlock(
        title="Disadvantages of DNNs",
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex("Sample inefficient", color=BLACK),
                    bib.slide_short_cite("efficient_processing_of_dnns"),
                ).arrange(RIGHT),
                VGroup(
                    Tex("Black-box", color=BLACK),
                    bib.slide_short_cite("wang_explaining_2021"),
                ).arrange(RIGHT),
                # "Relies upon large quantities of data",
                # bib.slide_short_cite("efficient_processing_of_dnns"),
                # "Difficult to interpret (i.e., black-box)",
                # bib.slide_short_cite("wang_explaining_2021"),
            ]
        ),
    )
    return SlideWithBlocks(
        title="Deep Neural Networks (DNNs)",
        subtitle=None,
        blocks=[example_block, alert_block],
    )


if __name__ == "__main__":
    beamer_slide = pros_and_cons()
    beamer_slide.render()
