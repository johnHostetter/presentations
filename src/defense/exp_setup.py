from manim import TexTemplate, BOLD, Text, VGroup
from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL


class Setup(SlideWithList):
    def __init__(self, **kwargs):
        title: str = "Experimental Setup"
        # subtitle: str = "Experimental Setup"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list = ItemizedList(
            items=[
                VGroup(
                    Text(
                        "Details of the environment, actions, and rewards", weight=BOLD
                    )
                ),
                BL(
                    items=[
                        "Each environment state is a RGB24 image of size 640x480 resolution",
                        "Actions are all possible key presses and mouse movements",
                        "Reward is particular to the current task",
                        "Each image is preprocessed to a 84x84x3 tensor",
                    ],
                    default_m_object=Text,
                ),
                VGroup(Text("Experimental conditions", weight=BOLD)),
                BL(
                    items=[
                        "Deep Neural Network (DNN) vs. Neuro-Fuzzy Network (NFN)",
                        "10 Epochs; evaluated for 25 episodes at end of each epoch",
                        "NFN is hierarchical and interpretable",
                    ],
                    default_m_object=Text,
                ),
                VGroup(Text("Common mechanisms and processes", weight=BOLD)),
                BL(
                    items=[
                        "Both trained online by Dueling Double Deep Q-Learning",
                        "Both used Convolutional Neural Networks (CNNs)",
                        "4 CNNs (in-channels, out-channels, kernel size, stride) w/ no bias term in convolution:",
                        ItemizedList(
                            items=[
                                "(3, 8, 3, 2)",
                                "(8, 8, 3, 2)",
                                "(8, 8, 5, 1)",
                                "(8, 16, 7, 1)",
                            ]
                        ),
                        "Final input shape to the DNN or NFN is (16, 10, 10)",
                        "Adam optimization",
                    ]
                ),
            ],
            default_m_object=Text,
        )

        super().__init__(**kwargs, title=title, subtitle=None, beamer_list=beamer_list)


if __name__ == "__main__":
    Setup().render()
