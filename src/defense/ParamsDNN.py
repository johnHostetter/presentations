from manim import *

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

class ParamsDNN(SlideWithList):
    def __init__(self, **kwargs):
        title: str = "Deep Neural Networks (DNNs)"
        subtitle: str = "Available Hyperparameters for TPE"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list=ItemizedList(
            items=[
                VGroup(Text("Environment", weight=BOLD)),
                BL(
                    items=[
                        "Number of frames skipped: 4, 8 or 12",
                    ],
                    default_m_object=Text
                ),
                VGroup(Text("Algorithm", weight=BOLD)),
                BL(
                    items=[
                        VGroup(
                            Text("Learning rate, "),
                            MathTex("\eta:", tex_template=myTemplate),
                            Text(
                                "[1e-5, 1e-3]"
                            ),
                        ),
                        VGroup(
                            Text("Batch size (used in experience replay), "),
                            MathTex("|\mathbf{X}|:", tex_template=myTemplate),
                            Text(
                                "8, 16, 24, 32, 40, 48, 56, 64"
                            ),
                        ),
                        VGroup(
                            Text("Memory size (used in experience replay), Rep. Memory: 10k, 20k, 30k, 40k, 50k"),
                        ),
                        VGroup(
                            Text("Discount factor, "),
                            MathTex("\gamma:", tex_template=myTemplate),
                            Text(
                                "[0.9, 0.99]"
                            ),
                        ),
                    ]
                ),
                VGroup(Text("Architecture", weight=BOLD)),
                BL(
                    items=[
                        VGroup(
                            Text("Number of hidden neurons, "),
                            MathTex("|\mathcal{N}|:", tex_template=myTemplate),
                            Text(
                                "128, 256, 384, 512"
                            ),
                        ),
                        "Activation function: ",
                        ItemizedList(
                            items=[
                                "ELU, PReLU, ReLU, ReLU6, RReLU, LeakyReLU",
                                "SELU, CELU, GELU, SiLU, Mish",
                                "Hardshrink, Hardtanh, Hardsigmoid, Hardswish",
                                "Softplus, Softshrink, Softsign, LogSigmoid",
                                "Tanh, Tanhshrink, Sigmoid",
                            ],
                            default_m_object=Text
                        )
                    ],
                    default_m_object=Text
                ),
            ],
            default_m_object=Text
        )

        super().__init__(**kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list)


if __name__ == "__main__":
    ParamsDNN().render()