from manim import TexTemplate, Tex, VGroup, BLACK, RIGHT, DARK_BLUE

from manim_beamer.bibtex import BibTexManager
from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL
from src.manim_presentation.utils import get_project_root


class Setup(SlideWithList):  # TODO: enable height of the slide to be adjusted
    def __init__(self, **kwargs):
        title: str = "Experimental Setup"
        # subtitle: str = "Experimental Setup"
        bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")

        cite_kwargs = {
            "color": DARK_BLUE,
            "opacity": 0.0,
            "font_size": 32,
        }

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list = ItemizedList(
            items=[
                VGroup(
                    Tex(
                        r"\textbf{Details of the environment:}",
                        color=BLACK,
                        font_size=42,
                    )
                ),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                r"\textit{States:} RGB24 640x480 images",
                                # "Each environment state is a RGB24 image of size 640x480 resolution",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex(
                                r"\textit{Note:} Images preprocessed to 84x84x3",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex(
                                r"\textit{Actions:} All possible key presses",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex(
                                r"\textit{Rewards:} Determined by current task",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                    ],
                ),
                VGroup(
                    Tex(r"\textbf{Experimental conditions:}", color=BLACK, font_size=42)
                ),
                BL(
                    items=[
                        VGroup(Tex("DNN vs. NFN", color=BLACK, font_size=36)),
                        VGroup(
                            Tex(
                                "10 Epochs; evaluated for 25 episodes at end of each epoch",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        # VGroup(
                        #     Tex("NFN is hierarchical and interpretable", color=BLACK)
                        # ),
                    ],
                ),
                VGroup(
                    Tex(
                        r"\textbf{Common mechanisms and processes:}",
                        color=BLACK,
                        font_size=42,
                    )
                ),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                "Both trained online by Dueling DDQL",
                                # "Both trained online by Dueling Double Deep Q-Learning",
                                color=BLACK,
                                font_size=36,
                            ),
                            bib.slide_short_cite(
                                "wang2016duelingnetworkarchitecturesdeep",
                                kwargs=cite_kwargs,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "Both used Convolutional Neural Networks (CNNs)",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex(
                                "4 CNNs (in-channels, out-channels, kernel size, stride) w/ no bias:",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        ItemizedList(
                            items=[
                                VGroup(
                                    Tex(
                                        "$[1]$ (3, 8, 3, 2)", color=BLACK, font_size=30
                                    ),
                                    Tex(
                                        "$[2]$ (8, 8, 3, 2)", color=BLACK, font_size=30
                                    ),
                                    Tex(
                                        "$[3]$ (8, 8, 5, 1)", color=BLACK, font_size=30
                                    ),
                                    Tex(
                                        "$[4]$ (8, 16, 7, 1)", color=BLACK, font_size=30
                                    ),
                                ).arrange(RIGHT),
                            ]
                        ),
                        VGroup(
                            Tex(
                                "Final input shape to the DNN or NFN is (16, 10, 10)",
                                color=BLACK,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex("Adam", color=BLACK, font_size=36),
                            bib.slide_short_cite("adam_optimizer", kwargs=cite_kwargs),
                        ).arrange(RIGHT, buff=0.1),
                    ]
                ),
            ],
        )

        super().__init__(**kwargs, title=title, subtitle=None, beamer_list=beamer_list)


if __name__ == "__main__":
    Setup().render()
