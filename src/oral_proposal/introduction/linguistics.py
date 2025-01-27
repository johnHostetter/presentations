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
        title: str = "Fuzzy Set Theory"
        subtitle: str = "Selected Terminology"

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        beamer_list=ItemizedList(
            items=[
                VGroup(
                    Text("Linguistic terms, "),
                    MathTex(" \mathcal{M} ", tex_template=myTemplate),
                    Text(
                        ", are constrained fuzzy sets w/ semantic meaning of some concept"
                    ),
                ),
                BL(
                    items=[
                        '"blue", "tall", "warm", "old", etc.',
                    ],
                    default_m_object=Text
                ),
                VGroup(
                    Text("Linguistic variables, "),
                    MathTex(" \mathcal{C} ", tex_template=myTemplate),
                    Text(", can take on values from a set of linguistic terms"),
                ),
                BL(
                    items=[
                        '"color"',
                        '"height"',
                        '"temperature", "age", etc.',
                    ],
                    default_m_object=Text
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
                            MathTex("\mu", tex_template=myTemplate),
                            Text(r'" where '),
                            MathTex("\mu \in \mathcal{M}", tex_template=myTemplate),
                        ),
                        ItemizedList(
                            items=[
                                'e.g., "the sky is blue", "the temperature is hot", '
                                '\n"the person is tall", "the car is old", etc.',
                            ],
                            default_m_object=Text
                        ),
                        "More complex (compound) propositions can be formed by combining atomic "
                        "\npropositions with logical operators (e.g., AND, OR, NOT, etc.)",
                        ItemizedList(
                            items=[
                                'e.g., "the sky is blue OR the temperature is hot", '
                                '\n"the person is tall AND the car is old", etc.'
                            ],
                            default_m_object=Text
                        ),
                    ],
                    default_m_object=Text
                )
            ],
            default_m_object=Text
        )

        super().__init__(**kwargs, title=title, subtitle=subtitle, beamer_list=beamer_list)


if __name__ == "__main__":
    Background().render()
    # Example usage:
    # beamer_slide = define_linguistics()
    # beamer_slide.render()
