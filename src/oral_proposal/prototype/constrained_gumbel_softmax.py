from manim import *

from manim_beamer.slides import SlideWithBlocks
from manim_beamer.lists import BulletedList as BL
from manim_beamer.blocks import AlertBlock, ExampleBlock, RemarkBlock

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def constrained_gumbel_softmax() -> SlideWithBlocks:
    """
    Create a slide discussing why we need to constrain the Gumbel-softmax.

    Returns:
        The slide with the issue, proposed solution, formula and remarks.
    """
    alert_block = AlertBlock(
        title="Suspected Issue",
        content="Gumbel-softmax may allow invalid selections to have non-zero probability\n"
        "as it approximates a categorical distribution.",
    )
    example_block = ExampleBlock(
        title="Proposed Solution",
        content="Constrain the Gumbel-softmax to ensure valid selections.",
    )
    remark_block = RemarkBlock(
        title="Remarks",
        content=BL(
            items=[
                "Constrained Gumbel-softmax distribution pushes invalid\n"
                "options to zero probability.",
                "Sum over linguistic term dimension (in denominator to\n"
                "sample and assign one term per variable for each fuzzy\n"
                "logic rules' premises.",
            ]
        ),
    )

    # Use the custom command in a LaTeX expression
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{amsmath}")  # for piecewise formula
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    # original_constrained_gumbel_formula = MathTex(
    #     r"\varphi(\tilde{\mathbf{I'}}) = \frac{"
    #     r"\exp{(\texttt{BoundSigmoid}(\tilde{\mathbf{I'}}))} \odot \mathbf{M'}}"
    #     r"{\sum_{j=1}^{\max_{i \in I_{\mathcal{C}}} ( | \mathcal{M}_{i} | )} "
    #     r"\exp{(\texttt{BoundSigmoid}(\tilde{\mathbf{I'}}))} \odot \mathbf{M'}}",
    #     color=BLACK, tex_template=myTemplate
    # )
    constrained_gumbel_formula = MathTex(
        r"\varphi(\tilde{\mathbf{I'}}) = \frac{"
        r"\exp{(\tilde{\mathbf{I'}})} \odot \mathbf{M'}}"
        r"{\sum_{j=1}^{\max_{i \in I_{\mathcal{C}}} ( | \mathcal{M}_{i} | )} "
        r"\exp{(\tilde{\mathbf{I'}})} \odot \mathbf{M'}}",
        color=BLACK, tex_template=myTemplate
    )
    ste_formula = MathTex(
        r"\mathbf{I} = \hat{\mathbf{I}'} - {{\varphi (\tilde{\mathbf{I}'})^{T}}_\texttt{detached}} + {\varphi (\tilde{\mathbf{I}'})^{T}}",
        color=BLACK,
    )
    # argmax_formula = MathTex(
    #     r"\hat{\mathbf{I}}_{i, u, j} = argmax_{j} \left( \varphi(\tilde{\mathbf{I}})_{i, u, j} \right)",
    #     color=BLACK,
    # )
    argmax_formula = MathTex(
        r"""
        \hat{\mathbf{I}}_{i, u, j} = 
        \begin{cases} 
            0 & \varphi(\tilde{\mathbf{I}})_{i, u, j} < \max_{j'}(\varphi(\tilde{\mathbf{I}})_{i, u, j'}) \\
            1 & \text{otherwise} \\
        \end{cases}
        """,
        color=BLACK,
        tex_template=myTemplate
    )
    return SlideWithBlocks(
        title="Constrained Gumbel-Softmax",
        subtitle=None,
        
        blocks=[
            alert_block,
            example_block,
            remark_block,
            constrained_gumbel_formula,
            Tex("followed by", color=BLACK),
            ste_formula,
            Tex("where ", color=BLACK),
            argmax_formula,

        ],
    )


if __name__ == "__main__":
    constrained_gumbel_softmax().render()
