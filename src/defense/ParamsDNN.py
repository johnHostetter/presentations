from manim import *

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class ParamsDNN(SlideWithList):  # TODO: enable height of the slide to be adjusted
    def __init__(self, **kwargs):
        title: str = "Deep Neural Networks (DNNs)"
        subtitle: str = "Available Hyperparameters for TPE"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        myTemplate.add_to_preamble(r"\usepackage[cal=boondox]{mathalfa}")

        beamer_list = ItemizedList(
            items=[
                VGroup(Tex(r"\textbf{Environment:}", color=BLACK, font_size=42)),
                BL(
                    items=[
                        VGroup(
                            Tex("Number of frames skipped: 4, 8, or 12", color=BLACK, font_size=36)
                        ),
                    ],
                ),
                VGroup(Tex(r"\textbf{Algorithm:}", color=BLACK, font_size=42)),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                r"Learning rate, $\eta$: [1e-5, 1e-3]",
                                color=BLACK,
                                font_size=36,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Batch size (in experience replay), $|\mathbf{X}|$: "
                                r"8, 16, 24, 32, 40, 48, 56, 64",
                                color=BLACK,
                                font_size=36,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Memory size (in experience replay), Rep. Memory: "
                                r"10k, 20k, 30k, 40k, 50k",
                                color=BLACK,
                                font_size=36,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Discount factor, $\gamma$: [0.9, 0.99]",
                                color=BLACK,
                                font_size=36,
                                tex_template=myTemplate,
                            ),
                        ),
                    ]
                ),
                VGroup(Tex(r"\textbf{Architecture:}", color=BLACK, font_size=42)),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                r"Number of hidden neurons, $|\mathcal{N}|$: "
                                r"128, 256, 384, 512",
                                color=BLACK,
                                font_size=36,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Activation function, $\mathcal{h}_{n}$: ",
                                color=BLACK,
                                font_size=36,
                                tex_template=myTemplate,
                            ),
                        ),
                        ItemizedList(
                            items=[
                                VGroup(
                                    Tex(
                                        "ELU, PReLU, ReLU, ReLU6, RReLU, LeakyReLU",
                                        color=BLACK,
                                        font_size=36,
                                        tex_template=myTemplate,
                                    )
                                ),
                                VGroup(
                                    Tex(
                                        "SELU, CELU, GELU, SiLU, Mish",
                                        color=BLACK,
                                        font_size=36,
                                        tex_template=myTemplate,
                                    )
                                ),
                                VGroup(
                                    Tex(
                                        "Hardshrink, Hardtanh, Hardsigmoid, Hardswish",
                                        color=BLACK,
                                        font_size=36,
                                        tex_template=myTemplate,
                                    )
                                ),
                                VGroup(
                                    Tex(
                                        "Softplus, Softshrink, Softsign, LogSigmoid",
                                        color=BLACK,
                                        font_size=36,
                                        tex_template=myTemplate,
                                    )
                                ),
                                VGroup(
                                    Tex(
                                        "Tanh, Tanhshrink, Sigmoid",
                                        color=BLACK,
                                        font_size=36,
                                        tex_template=myTemplate,
                                    )
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )

        super().__init__(
            **kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list
        )


if __name__ == "__main__":
    ParamsDNN().render()
