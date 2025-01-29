from manim import *

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class ParamsNFN(SlideWithList):
    def __init__(self, **kwargs):
        title: str = "Neuro-Fuzzy Networks (NFNs)"
        subtitle: str = "Available Hyperparameters for TPE"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{soul, color}")
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        myTemplate.add_to_preamble(r"\usepackage[cal=boondox]{mathalfa}")

        beamer_list = ItemizedList(
            items=[
                VGroup(Tex(r"\textbf{Environment:}", color=BLACK)),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                "Number of frames skipped: (chosen by DNN)", color=BLACK
                            )
                        ),
                    ],
                ),
                VGroup(Tex(r"\textbf{Algorithm:}", color=BLACK)),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                "Learning rate, $\eta$: [1e-4, 1e-3]",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "Batch size (in experience replay), $|\mathbf{X}|$: "
                                "(chosen by DNN)",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "Memory size (in experience replay), Rep. Memory: (chosen by DNN)",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "Discount factor, $\gamma$: (chosen by DNN)",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                    ]
                ),
                VGroup(Tex(r"\textbf{Architecture}", color=BLACK)),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                "Number of fuzzy logic rules, $|U|$: 64, 128, 192, 256",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "\hl{Sampling of fuzzy logic rules: STE or GMT}",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Gumbel temperature, $\tau$: [0.25, 1.25]",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Percentile threshold, $\theta$: "
                                r"0.0 (disabled) or 0.1 (slightly enabled)",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Retain sampled Gumbel noise, $\mathbf{N}$: "
                                r"after \rule{1cm}{0.4pt} batches: "
                                "1, 32, 64, 128, 256",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "Required membership degree, $\epsilon$: [0.1, 0.5]",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "Number of batches to delay new fuzzy sets, $+\mu$: "
                                "1 (add immediately), 3, 5",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "\hl{Premise aggregation, $w_{u}$: "
                                "Sum (standard) or Mean (Cui et al., 2021)}",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"\hl{Activation of fuzzy logic rule, $\overline{w}_{u}'$: "
                                r"\texttt{softmax} or \texttt{1.5-entmax}}",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                r"Enable certainty factors, CF: False or True",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                        VGroup(
                            Tex(
                                "\hl{Enable layer normalization, LN: False or True}",
                                color=BLACK,
                                tex_template=myTemplate,
                            ),
                        ),
                    ],
                ),
            ],
        )

        super().__init__(
            **kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list
        )


if __name__ == "__main__":
    ParamsNFN().render()
