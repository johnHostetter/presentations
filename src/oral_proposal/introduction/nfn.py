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
        title="Advantages",
        content=AdvantagesList(
            items=[
                VGroup(Tex(r"\textbf{Powerful}", color=BLACK, font_size=42)),
                ItemizedList(
                    items=[
                        VGroup(
                            Tex("Same theoretical guarantees as DNNs", color=BLACK, font_size=36),
                            bib.slide_short_cite(
                                "wang_mendel_universal_function_approx"
                            ),
                            # 1992
                            bib.slide_short_cite(
                                "wang_universal_function_approx"
                            ),  # 1992
                            bib.slide_short_cite(
                                "kosko_universal_function_approx"
                            ),  # 1994
                            bib.slide_short_cite("ying_necessary_1994"),  # SISO FIS
                            bib.slide_short_cite("zeng_approximation_1995"),  # MIMO FIS
                            bib.slide_short_cite("figueiredo_design_1999"),  # NFNs
                        ).arrange(RIGHT),
                    ]
                ),
                VGroup(
                    Tex(r"\textbf{Transparent}", color=BLACK, font_size=42),
                ),
                ItemizedList(
                    items=[
                        VGroup(
                            # Tex(
                            #     "Historically designed by human experts (i.e., ``expert-designed'')",
                            #     color=BLACK,
                            # ),
                            Tex(
                                "Linguistic IF-THEN rules",
                                color=BLACK,
                                font_size=36,
                            ),
                            bib.slide_short_cite("lee_supervised_1992"),
                            bib.slide_short_cite("elkan_paradoxical_1994"),
                            bib.slide_short_cite("buckley_neural_1995"),
                            bib.slide_short_cite("chen_fuzzy_1995"),
                        ).arrange(RIGHT),
                    ]
                ),
                VGroup(
                    Tex(r"\textbf{Sample efficient}", color=BLACK, font_size=42),
                ),
                ItemizedList(
                    items=[
                        VGroup(
                            Tex(
                                "A priori knowledge as linguistic rules",
                                color=BLACK,
                                font_size=36,
                            ),
                            bib.slide_short_cite("berenji_learning_1992"),
                        ).arrange(RIGHT),
                    ]
                ),
            ]
        ),
    )
    alert_block = AlertBlock(
        title="Challenges",
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex("Human labor", color=BLACK, font_size=42),
                    bib.slide_short_cite("lee_flc_12"),
                    bib.slide_short_cite("klir_yuan"),
                ).arrange(RIGHT),
                # "Difficult & expensive to design",
                # bib.slide_short_cite("lee_flc_12"),
                # ItemizedList(
                #     items=[
                #         "Subconscious decision-making hard to articulate",
                #         "Requires domain expertise",
                #         "Time-consuming",
                #     ]
                # ),
                VGroup(
                    Tex("Complex mechanisms used to add new knowledge", color=BLACK, font_size=42),
                    bib.slide_short_cite("chen_self-organizing_1993"),
                    bib.slide_short_cite("zhou_pseudo_1996"),
                    bib.slide_short_cite("er_online_2004"),
                ).arrange(RIGHT),
                # "Unable to readily adapt to changes (e.g., add new knowledge)",
                # bib.slide_short_cite("klir_yuan"),
                # ItemizedList(
                #     items=[
                #         "Self-organizing NFNs may achieve this but with restrictions",
                #         bib.slide_short_cite("chen_self-organizing_1993"),
                #         bib.slide_short_cite("zhou_pseudo_1996"),
                #         bib.slide_short_cite("er_online_2004"),
                #     ]
                # ),
                VGroup(
                    Tex(
                        "Data-driven methods often specific to a certain task",
                        color=BLACK,
                        font_size=42,
                    ),
                    bib.slide_short_cite("aghaeipoor_mokblmoms_2019"),
                    bib.slide_short_cite("zhou_reinforcement_2009"),
                ),
                # "NFN research is often specific to a certain task",
                # ItemizedList(
                #     items=[
                #         "(e.g., supervised or reinforcement learning)",
                #         bib.slide_short_cite("aghaeipoor_mokblmoms_2019"),
                #         bib.slide_short_cite("zhou_reinforcement_2009"),
                #     ]
                # ),
            ]
        ),
    )
    kwargs = {
        "color": DARK_BLUE,
        "opacity": 0.0,
        "font_size": 30,
    }
    remark_block = ExampleBlock(
        title="Solutions",
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex("Data-driven construction", color=BLACK, font_size=42),
                    bib.slide_short_cite("hostetter2023leveraging", abbrev=True),
                    bib.slide_short_cite("hostetter2023latent", abbrev=True),
                ).arrange(RIGHT, buff=0.1),
                VGroup(
                    Tex("Capable of adding new knowledge just in time", color=BLACK, font_size=42),
                    bib.slide_short_cite("hostetter2023self", abbrev=True),
                ),
                VGroup(
                    Tex(
                        "Task-independent (i.e., gradient-based learning)",
                        color=BLACK,
                        font_size=42,
                    ),
                    Tex("$[$This Dissertation$]$", **kwargs),
                ).arrange(RIGHT, buff=0.1),
            ]
        ),
    )

    return SlideWithBlocks(
        title="Neuro-Fuzzy Networks (NFNs)",
        subtitle=None,
        blocks=[example_block, alert_block, remark_block],
    )


if __name__ == "__main__":
    pros_and_cons().render()
