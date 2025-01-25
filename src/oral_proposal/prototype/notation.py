from manim import *

from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def get_notation() -> SlideWithList:
    """
    Create a slide discussing the notation that will be used.

    Returns:
        The slide describing the notation.
    """
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    return SlideWithList(
        title="Necessary Notation",
        subtitle=None,
        width_buffer=12.0,
        beamer_list=ItemizedList(
            items=[
                "Membership Matrix",
                BL(
                    items=[
                        VGroup(
                            Text("Let  ", color=BLACK),
                            MathTex(r"\boldsymbol{\mu}(\mathbf{x})", color=BLACK),
                            Text(" be the resulting membership matrix.", color=BLACK),
                        ),
                        VGroup(
                            Text("Shape of  ", color=BLACK),
                            MathTex(r"\boldsymbol{\mu}(\mathbf{x})", color=BLACK),
                            Text(" is ", color=BLACK),
                            VGroup(
                                MathTex(r"|I_{\mathcal{C}}|", color=BLACK),
                                Cross(color=BLACK, stroke_width=3).scale(
                                    scale_factor=0.1
                                ),
                                MathTex(r"\max_{i \in I_{\mathcal{C}}}(|\mathcal{M}_{i}|)", color=BLACK),
                            ),
                        ),
                    ]
                ),
                "Mask Matrix",
                BL(
                    items=[
                        VGroup(
                            Text("A binary mask matrix  ", color=BLACK),
                            MathTex(r"\mathbf{M}", color=BLACK),
                            Text(
                                " contains a 1 iff linguistic term exists at ",
                                color=BLACK,
                            ),
                            MathTex(r"i, j.", color=BLACK),
                        ),
                        VGroup(
                            Text("Shape of  ", color=BLACK),
                            MathTex(r"\mathbf{M}", color=BLACK),
                            Text(" is ", color=BLACK),
                            VGroup(
                                MathTex(r"|I_{\mathcal{C}}|", color=BLACK),
                                Cross(color=BLACK, stroke_width=3).scale(
                                    scale_factor=0.1
                                ),
                                MathTex(r"\max_{i \in I_{\mathcal{C}}}(|\mathcal{M}_{i}|)", color=BLACK),
                            ),
                        ),
                    ]
                ),
                "Premise Calculation",
                BL(
                    items=[
                        "Non-existing memberships are dropped by Hadamard product",
                        VGroup(MathTex(r"\boldsymbol{\mu}(\mathbf{x}) \odot \mathbf{M}", color=BLACK)),
                    ]
                ),
                "Rule Connection Matrix",
                BL(
                    items=[
                        VGroup(
                            Text("Let  ", color=BLACK),
                            MathTex(r"\mathbf{I}", color=BLACK),
                            Text(
                                " be the link matrix between premise and rule layer.",
                                color=BLACK,
                            ),
                        ),
                        VGroup(
                            Text("Shape of  ", color=BLACK),
                            MathTex(r"\mathbf{I}", color=BLACK),
                            Text(" is ", color=BLACK),
                            VGroup(
                                MathTex(r"|I_{\mathcal{C}}|", color=BLACK),
                                Cross(color=BLACK, stroke_width=3).scale(
                                    scale_factor=0.1
                                ),
                                MathTex(r"\max_{i \in I_{\mathcal{C}}}(|\mathcal{M}_{i}|)", color=BLACK),
                                Cross(color=BLACK, stroke_width=3).scale(
                                    scale_factor=0.1
                                ),
                                MathTex(r"|U|", color=BLACK),
                            ),
                        ),
                        VGroup(
                            Text("Entry at  ", color=BLACK),
                            MathTex(r"\mathbf{I}_{i, j, u}", color=BLACK),
                            Text(" is 0 or 1 iff the ", color=BLACK),
                            MathTex(r"j^{th}", color=BLACK),
                            Text(" term of ", color=BLACK),
                            MathTex(r"i^{th}", color=BLACK),
                            Text(" variable is in the premise of rule ", color=BLACK),
                            MathTex(r"u.", color=BLACK),
                        ),
                    ]
                ),
            ]
        ),
    )


if __name__ == "__main__":
    get_notation().render()
