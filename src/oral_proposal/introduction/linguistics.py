from manim import *

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def define_linguistics() -> SlideWithList:
    """
    Create a slide defining what we mean by linguistics, such as linguistic terms and variables.

    Returns:
        The slide with definitions and examples.
    """
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    MathTex("\mathcal{T}")
    return SlideWithList(
        title="A Brief Tour of Linguistics",
        subtitle=None,
        beamer_list=ItemizedList(
            items=[
                VGroup(
                    Text("Linguistic terms, "),
                    MathTex(" \mathcal{M} "),
                    Text(
                        ", are constrained fuzzy sets w/ semantic meaning of some concept"
                    ),
                ),
                BL(
                    items=[
                        '"blue", "tall", "warm", "old", etc.',
                    ]
                ),
                VGroup(
                    Text("Linguistic variables, "),
                    MathTex(" \mathcal{C} "),
                    Text(", can take on values from a set of linguistic terms"),
                ),
                BL(
                    items=[
                        '"color"',
                        '"height"',
                        '"temperature", "age", etc.',
                    ]
                ),
                "Degree to which a linguistic term applies to a linguistic variable is calculated "
                "\nby an atomic fuzzy proposition",
                BL(
                    items=[
                        VGroup(
                            Text(
                                'Written as "',
                            ),
                            MathTex("x"),
                            Text(" is "),
                            MathTex("\mu"),
                            Text('" where '),
                            MathTex("\mu \in \mathcal{M}"),
                        ),
                        ItemizedList(
                            items=[
                                'e.g., "the sky is blue", "the temperature is hot", '
                                '\n"the person is tall", "the car is old", etc.',
                            ]
                        ),
                        "More complex (compound) propositions can be formed by combining atomic "
                        "\npropositions with logical operators (e.g., AND, OR, NOT, etc.)",
                        ItemizedList(
                            items=[
                                'e.g., "the sky is blue OR the temperature is hot", '
                                '\n"the person is tall AND the car is old", etc.'
                            ]
                        ),
                    ]
                ),
            ]
        ),
    )


class Background(SlideWithList):
    def __init__(self, **kwargs):
        title: str = "Fuzzy Set Theory & Fuzzy Logic"
        subtitle: str = "Selected Terminology"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        myTemplate.add_to_preamble(r"\usepackage[cal=boondox]{mathalfa}")

        beamer_list = ItemizedList(
            items=[
                VGroup(
                    Tex(
                        r"Linguistic terms, $\mathcal{M}$, are constrained fuzzy sets "
                        r"\\w/ semantic meaning of some concept ",
                        tex_template=myTemplate,
                        tex_environment="flushleft",
                        color=BLACK,
                    ),
                ),
                # BL(
                #     items=[
                #         VGroup(
                #             Tex(
                #                 r"``blue'', ``tall'', ``warm'', ``old'', etc.",
                #                 tex_template=myTemplate, tex_environment="flushleft", color=BLACK
                #             )
                #         ),
                #     ],
                # ),
                VGroup(
                    Tex(
                        r"Linguistic variables, $\mathcal{C}$, "
                        r"can take on values from a set of linguistic terms",
                        tex_template=myTemplate,
                        tex_environment="flushleft",
                        color=BLACK,
                    ),
                ),
                # BL(
                #     items=[
                #         VGroup(
                #             Tex(
                #                 r"``color'', ``height'', ``temperature'', ``age'', etc.",
                #                 tex_template=myTemplate, tex_environment="flushleft", color=BLACK
                #             )
                #         ),
                #     ],
                # ),
                VGroup(
                    Tex(
                        r"Degree to which a linguistic term applies to a linguistic variable "
                        r"\\is calculated by an atomic fuzzy proposition",
                        tex_template=myTemplate,
                        tex_environment="flushleft",
                        color=BLACK,
                    )
                ),
                BL(
                    items=[
                        VGroup(
                            Tex(
                                r"Written as ``$x$ is $\mu$'' "
                                r"(or $\mu(x)$) where $\mu \in \mathcal{M}$,",
                                tex_template=myTemplate,
                                tex_environment="flushleft",
                                color=BLACK,
                            ),
                        ),
                        # VGroup(
                        #     Tex(
                        #         r"e.g., ``the sky is blue'', ``the temperature is hot'', "
                        #         r"\\``the person is tall'', ``the car is old'', etc.",
                        #         tex_template=myTemplate, tex_environment="flushleft", color=BLACK
                        #     )
                        # ),
                    ],
                ),
                VGroup(
                    Tex(
                        r"More complex (compound) propositions can be formed by combining atomic ",
                        r"\\propositions with logical operators (e.g., AND ($\wedge$), OR ($\vee$), NOT ($\neg$))",
                        tex_template=myTemplate,
                        tex_environment="flushleft",
                        color=BLACK,
                    )
                ),
                # BL(
                #     items=[
                #         VGroup(Tex(
                #             r"e.g., ``the sky is blue OR the temperature is hot'', "
                #             r"\\``the person is tall AND the car is old'', etc.",
                #             tex_template=myTemplate, tex_environment="flushleft", color=BLACK
                #         ))
                #     ],
                # ),
                VGroup(
                    Tex(
                        r"Rules can be expressed as a set of fuzzy propositions, "
                        r"which can be\\combined to form a fuzzy rule base",
                        tex_template=myTemplate,
                        tex_environment="flushleft",
                        color=BLACK,
                    )
                ),
                # BL(
                #     items=[
                #         VGroup(Tex(
                #             r"e.g., ``IF the temperature is hot THEN the fan is on'', "
                #             r"\\``IF the person is tall AND the car is old THEN the person is wise'', etc.",
                #             tex_template=myTemplate, tex_environment="flushleft", color=BLACK
                #         ))
                #     ],
                # ),
            ],
        )

        super().__init__(
            **kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list
        )


if __name__ == "__main__":
    Background().render()
    # Example usage:
    # beamer_slide = define_linguistics()
    # beamer_slide.render()
