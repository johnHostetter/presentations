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
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list=ItemizedList(
            items=[
                VGroup(Text("Environment", weight=BOLD)),
                BL(
                    items=[
                        "Number of frames skipped: (chosen by DNN)",
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
                                "[1e-4, 1e-3]"
                            ),
                        ),
                        VGroup(
                            Text("Batch size (used in experience replay), "),
                            MathTex("|\mathbf{X}|:", tex_template=myTemplate),
                            Text(
                                "(chosen by DNN)"
                            ),
                        ),
                        VGroup(
                            Text("Memory size (used in experience replay), Rep. Memory: (chosen by DNN)"),
                        ),
                        VGroup(
                            Text("Discount factor, "),
                            MathTex("\gamma:", tex_template=myTemplate),
                            Text(
                                "(chosen by DNN)"
                            ),
                        ),
                    ]
                ),
                VGroup(Text("Architecture", weight=BOLD)),
                BL(
                    items=[
                        VGroup(
                            Text("Number of fuzzy logic rules, "),
                            MathTex("|U|:", tex_template=myTemplate),
                            Text(
                                "64, 128, 192, 256"
                            ),
                        ),
                        "Sampling of fuzzy logic rules: STE or GMT",
                        VGroup(
                            Text("Gumbel temperature, "),
                            MathTex(r"\tau:", tex_template=myTemplate),
                            Text(
                                "[0.25, 1.25]"
                            ),
                        ),
                        VGroup(
                            Text("Percentile threshold, "),
                            MathTex(r"\theta:", tex_template=myTemplate),
                            Text(
                                "0.0 (disabled) or 0.1 (slightly enabled)"
                            ),
                        ),
                        VGroup(
                            Text("Retain sampled Gumbel noise, "),
                            MathTex(r"\mathbf{N}:", tex_template=myTemplate),
                            Text(
                                "after ___ batches: 1, 32, 64, 128, 256"
                            ),
                        ),
                        VGroup(
                            Text("Required membership degree, "),
                            MathTex(r"\epsilon:", tex_template=myTemplate),
                            Text(
                                "[0.1, 0.5]"
                            ),
                        ),
                        VGroup(
                            Text("Number of batches to delay new fuzzy sets, "),
                            MathTex(r"+\mu:", tex_template=myTemplate),
                            Text(
                                "1 (add immediately), 3, 5"
                            ),
                        ),
                        VGroup(
                            Text("Preliminary calculation of fuzzy rules' applicability, "),
                            MathTex(r"w_{u}:", tex_template=myTemplate),
                            Text(
                                "Sum (standard) or Mean (Cui et al., 2021)"
                            ),
                        ),
                        VGroup(
                            Text("Activation of fuzzy logic rule, "),
                            MathTex(r"\overline{w}_{u}':", tex_template=myTemplate),
                            Tex(
                                r"\texttt{softmax}"
                            ),
                            Text("or"),
                            Tex(
                                r"\texttt{1.5-entmax}"
                            ),
                        ),
                        VGroup(
                            Text("Enable certainty factors, "),
                            MathTex(r"CF:", tex_template=myTemplate),
                            Text(
                                "False or True"
                            ),
                        ),
                        VGroup(
                            Text("Enable layer normalization, "),
                            MathTex(r"LN:", tex_template=myTemplate),
                            Text(
                                "False or True"
                            ),
                        ),
                    ],
                    default_m_object=Text
                ),
            ],
            default_m_object=Text
        )

        super().__init__(**kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list)


if __name__ == "__main__":
    ParamsNFN().render()