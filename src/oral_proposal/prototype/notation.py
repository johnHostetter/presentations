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
        beamer_list=BL(
            items=[
                VGroup(
                    Tex(
                        r"Membership Matrix, $\boldsymbol{\mu}(\mathbf{x})$",
                        color=BLACK, font_size=42
                    )
                ),
                # VGroup(Tex(r"\textbf{Membership Matrix:}", color=BLACK)),
                # BL(
                #     items=[
                #         VGroup(
                #             Tex(
                #                 r"Let $\boldsymbol{\mu}(\mathbf{x})$ be the "
                #                 r"resulting membership matrix",
                #                 color=BLACK,
                #             ),
                #         ),
                #         # VGroup(
                #         #     Text("Shape of  ", color=BLACK),
                #         #     MathTex(r"\boldsymbol{\mu}(\mathbf{x})", color=BLACK),
                #         #     Text(" is ", color=BLACK),
                #         #     VGroup(
                #         #         MathTex(r"|I_{\mathcal{C}}|", color=BLACK),
                #         #         Cross(color=BLACK, stroke_width=3).scale(
                #         #             scale_factor=0.1
                #         #         ),
                #         #         MathTex(
                #         #             r"\max_{i \in I_{\mathcal{C}}}(|\mathcal{M}_{i}|)",
                #         #             color=BLACK,
                #         #         ),
                #         #     ),
                #         # ),
                #     ]
                # ),
                # VGroup(Tex(r"\textbf{Mask Matrix:}", color=BLACK)),
                VGroup(Tex(r"Mask Matrix, $\mathbf{M}$", color=BLACK, font_size=42)),
                # BL(
                #     items=[
                #         VGroup(
                #             Tex(
                #                 r"A binary mask matrix, $\mathbf{M}$, contains a 1 "
                #                 r"iff linguistic term exists at $i$, $j$",
                #                 color=BLACK,
                #             ),
                #         ),
                #         # VGroup(
                #         #     Text("Shape of  ", color=BLACK),
                #         #     MathTex(r"\mathbf{M}", color=BLACK),
                #         #     Text(" is ", color=BLACK),
                #         #     VGroup(
                #         #         MathTex(r"|I_{\mathcal{C}}|", color=BLACK),
                #         #         Cross(color=BLACK, stroke_width=3).scale(
                #         #             scale_factor=0.1
                #         #         ),
                #         #         MathTex(
                #         #             r"\max_{i \in I_{\mathcal{C}}}(|\mathcal{M}_{i}|)",
                #         #             color=BLACK,
                #         #         ),
                #         #     ),
                #         # ),
                #     ]
                # ),
                VGroup(
                    Tex(
                        r"Premise Calculation, $\boldsymbol{\mu}(\mathbf{x}) \odot \mathbf{M}$",
                        color=BLACK, font_size=42
                    )
                ),
                # VGroup(Tex(r"\textbf{Premise Calculation:}", color=BLACK)),
                # BL(
                #     items=[
                #         VGroup(
                #             Tex(
                #                 r"Non-existing memberships are dropped by Hadamard "
                #                 r"product, $\boldsymbol{\mu}(\mathbf{x}) \odot \mathbf{M}$",
                #                 color=BLACK,
                #             )
                #         ),
                #     ]
                # ),
                VGroup(Tex(r"Rule Connection Matrix, $\mathbf{I}$", color=BLACK, font_size=42)),
                # VGroup(Tex(r"\textbf{Rule Connection Matrix:}", color=BLACK)),
                ItemizedList(
                    items=[
                        # VGroup(
                        #     Tex(
                        #         r"Let $\mathbf{I}$ be the link matrix between premise and rule layer",
                        #         color=BLACK,
                        #     ),
                        # ),
                        # VGroup(
                        #     Text("Shape of  ", color=BLACK),
                        #     MathTex(r"\mathbf{I}", color=BLACK),
                        #     Text(" is ", color=BLACK),
                        #     VGroup(
                        #         MathTex(r"|I_{\mathcal{C}}|", color=BLACK),
                        #         Cross(color=BLACK, stroke_width=3).scale(
                        #             scale_factor=0.1
                        #         ),
                        #         MathTex(
                        #             r"\max_{i \in I_{\mathcal{C}}}(|\mathcal{M}_{i}|)",
                        #             color=BLACK,
                        #         ),
                        #         Cross(color=BLACK, stroke_width=3).scale(
                        #             scale_factor=0.1
                        #         ),
                        #         MathTex(r"|U|", color=BLACK),
                        #     ),
                        # ),
                        VGroup(
                            Tex(
                                r"$\mathbf{I}_{i, j, u} = 1$ iff the $j^{th}$ "
                                r"term of $i^{th}$ variable is in rule $u$",
                                color=BLACK,
                                font_size=36,
                            ),
                        ),
                    ]
                ),
            ]
        ),
        adjust_by_height=True,
    )


if __name__ == "__main__":
    get_notation().render()
