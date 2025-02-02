from manim import TexTemplate, BOLD, Tex, VGroup
from typer.colors import BLACK

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL


class TPE(SlideWithList):
    def __init__(self, **kwargs):
        title: str = "Tree Parzen Estimator (TPE)"
        subtitle: str = "Neural Architecture Search"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list = ItemizedList(
            items=[
                VGroup(
                    Tex(
                        r"Multi-objective Bayesian hyperparameter optimization",
                        color=BLACK,
                        tex_template=myTemplate,
                        font_size=42,
                    )
                ),
                VGroup(
                    Tex(
                        r"Optimize hyperparameters of DNN and NFN:",
                        color=BLACK,
                        tex_template=myTemplate,
                        font_size=42,
                    )
                ),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                r"Maximize the average evaluation performance",
                                color=BLACK,
                                tex_template=myTemplate,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex(
                                r"Minimize its corresponding standard deviation",
                                color=BLACK,
                                tex_template=myTemplate,
                                font_size=36,
                            )
                        ),
                        VGroup(
                            Tex(
                                r"Maximize the linear slope of the performance across all epochs",
                                color=BLACK,
                                tex_template=myTemplate,
                                font_size=36,
                            )
                        ),
                    ]
                ),
                VGroup(
                    Tex(
                        r"720 \& 300 trials per DOOM task for DNN and NFN, respectively",
                        color=BLACK,
                        tex_template=myTemplate,
                        font_size=42,
                    ),
                ),
            ],
        )

        super().__init__(
            **kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list
        )


if __name__ == "__main__":
    TPE().render()
