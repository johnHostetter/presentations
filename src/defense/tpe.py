from manim import TexTemplate, BOLD, Text, VGroup
from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL


class TPE(SlideWithList):
    def __init__(self, **kwargs):
        title: str = "Tree Parzen Estimator"
        subtitle: str = "A Multi-Objective Hyperparameter Search"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list = ItemizedList(
            items=[
                "The Tree Parzen Estimator (TPE) is a Bayesian optimization algorithm",
                "It is used for hyperparameter optimization",
                "TPE is capable of multi-objective optimization",
                # "It is based on the Parzen Window technique",
                # "TPE uses a tree-structured Parzen estimator to model the objective function",
                "TPE is used here to optimize the hyperparameters of the DNN and NFN",
                "The multi-objective optimization does the following:",
                BL(
                    items=[
                        "Maximize the average evaluation performance",
                        "Minimize its corresponding standard deviation",
                        "Maximize the linear slope of the performance across all epochs",
                    ],
                    default_m_object=Text,
                ),
                "720 & 300 trials per DOOM task for DNN and NFN, respectively",
            ],
            default_m_object=Text,
        )

        super().__init__(
            **kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list
        )


if __name__ == "__main__":
    TPE().render()
