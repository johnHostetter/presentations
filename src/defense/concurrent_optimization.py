from manim import *

from manim_beamer.bibtex import BibTexManager
from manim_beamer.slides import SlideShow
from src.manim_presentation.utils import get_project_root
from src.oral_proposal.prototype.notation import get_notation

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

from manim import *

from manim_beamer.slides import SlideWithBlocks
from manim_beamer.blocks import AlertBlock, ExampleBlock
from manim_beamer.lists import AdvantagesList, DisadvantagesList

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def relax_links() -> SlideWithBlocks:
    """
    Create a slide discussing why we need to modify the Gumbel-Max Trick.

    Returns:
        The slide with the issue, remark and proposed solution.
    """
    alert_block = AlertBlock(
        title="Issue",
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex(r"NFN do not have real-numbered weight matrices", color=BLACK),
                ),
                VGroup(
                    Tex(
                        r"Matrix $\mathbf{I}$ is sparse, constrained \& binary",
                        color=BLACK,
                    ),
                ),
                VGroup(
                    Tex(r"Rules' premises cannot change", color=BLACK),
                ),
            ]
        ),
    )

    example_block = ExampleBlock(
        title="Proposed Solution",
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex(
                        r"Frame selection of premises as a "
                        r"categorical probability distribution",
                        color=BLACK,
                    ),
                ),
                VGroup(
                    Tex(
                        r"Use real-valued logits or raw non-normalized probabilities, $\tilde{\mathbf{I}}$",
                        color=BLACK,
                    ),
                ),
                VGroup(
                    Tex(
                        r"Differentiably sample rules' premises based on gradients",
                        color=BLACK,
                    ),
                ),
            ]
        ),
    )
    return SlideWithBlocks(
        title="Gradient-Based Neuroplastic Adaptation",
        subtitle=None,
        blocks=[alert_block, example_block],
        height_buffer=3.0,
    )


def constrained_gumbel_softmax() -> SlideWithBlocks:
    """
    Create a slide discussing why we need to constrain the Gumbel-softmax.

    Returns:
        The slide with the issue, proposed solution, formula and remarks.
    """
    bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")

    cite_kwargs = {
        "color": DARK_BLUE,
        "opacity": 0.0,
        "font_size": 32,
    }

    alert_block_1 = AlertBlock(
        title="Issue 1",
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex(
                        r"Stochastic process defined by discrete distribution",
                        color=BLACK,
                    ),
                ),
            ]
        ),
    )
    example_block_1 = ExampleBlock(
        title="Solution 1",
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex(
                        r"Reparameterization Trick: Sample from continuous distribution",
                        color=BLACK,
                    ),
                ),
            ]
        ),
    )
    alert_block_2 = AlertBlock(
        title="Issue 2",
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex(r"Require a sample from categorical distribution", color=BLACK),
                ),
            ]
        ),
    )
    example_block_2 = ExampleBlock(
        title="Solution 2",
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex(
                        r"Gumbel-Max Trick (GMT): Separate the deterministic and stochastic parts",
                        color=BLACK,
                    ),
                ),
            ]
        ),
    )
    alert_block_3 = AlertBlock(
        title="Issue 3",
        content=DisadvantagesList(
            items=[
                VGroup(
                    Tex(r"GMT samples with \texttt{argmax}", color=BLACK),
                ),
            ]
        ),
    )
    example_block_3 = ExampleBlock(
        title="Solution 3",
        content=AdvantagesList(
            items=[
                VGroup(
                    Tex(
                        r"Gumbel-Softmax: Differentiable approximation of \texttt{argmax}",
                        color=BLACK,
                    ),
                ),
            ]
        ),
    )

    # Use the custom command in a LaTeX expression
    myTemplate = TexTemplate()
    myTemplate.add_to_preamble(r"\usepackage{amsmath}")  # for piecewise formula
    myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
    myTemplate.add_to_preamble(r"\usepackage[cal=boondox]{mathalfa}")
    myTemplate.add_to_preamble(r"\usepackage{soul, xcolor}")
    myTemplate.add_to_preamble(
        r"\newcommand{\mathcolorbox}[2]{\fcolorbox{#1!90!black}{#1!10!white}{$\displaystyle #2$}}"
    )

    # original_constrained_gumbel_formula = MathTex(
    #     r"\varphi(\tilde{\mathbf{I}}') = \frac{"
    #     r"\exp{(\texttt{BoundSigmoid}(\tilde{\mathbf{I}}'))} \odot \mathbf{M}'}"
    #     r"{\sum_{j=1}^{\max_{i \in I_{\mathcal{C}}} ( | \mathcal{M}_{i} | )} "
    #     r"\exp{(\texttt{BoundSigmoid}(\tilde{\mathbf{I}}'))} \odot \mathbf{M}'}",
    #     color=BLACK, tex_template=myTemplate
    # )

    constrained_gumbel_formula = MathTex(
        r"\varphi(\tilde{\mathbf{I}}') = \frac{"
        r"\exp{(\tilde{\mathbf{I}}')} \odot \mathbf{M}'}"
        r"{\sum_{j=1}^{\max_{i \in I_{\mathcal{C}}} ( | \mathcal{M}_{i} | )} "
        r"\exp{(\tilde{\mathbf{I}}')} \odot \mathbf{M}'}",
        color=BLACK,
        tex_template=myTemplate,
    )
    constrained_gumbel_formula = VGroup(
        Tex("Constrained Gumbel-Softmax", color=BLACK, font_size=36),
        Brace(constrained_gumbel_formula, UP, buff=0.1, color=BLACK),
        constrained_gumbel_formula,
    ).arrange(DOWN, buff=0.1)

    constrained_gumbel_formula = VGroup(
        constrained_gumbel_formula,
        bib.slide_short_cite(
            "jang2017categoricalreparameterizationgumbelsoftmax", kwargs=cite_kwargs
        ),
    ).arrange(RIGHT, buff=0.5)

    noise_formula = MathTex(
        r"\tilde{\mathbf{I}}' = \frac{\tilde{\mathbf{I}} + \mathbf{N}}{\tau^2}",
        color=BLACK,
    )

    noise_formula = VGroup(
        Tex("Gumbel Noise", color=BLACK, font_size=36),
        Brace(noise_formula, UP, buff=0.1, color=BLACK),
        noise_formula,
    ).arrange(DOWN, buff=0.1)

    noise_formula = VGroup(
        noise_formula,
        bib.slide_short_cite(
            "jang2017categoricalreparameterizationgumbelsoftmax", kwargs=cite_kwargs
        ),
    ).arrange(RIGHT, buff=0.5)

    constrained_mask = MathTex(
        r"\mathbf{M}' = (\mathbf{M} \odot \mathbf{S}) > \theta", color=BLACK
    )

    constrained_mask = VGroup(
        Tex("Constrained Mask", color=BLACK, font_size=36),
        Brace(constrained_mask, UP, buff=0.1, color=BLACK),
        constrained_mask,
    ).arrange(DOWN, buff=0.1)

    ste_formula = MathTex(
        r"\mathbf{I} = "
        r"\big("
        r"\varphi (\tilde{\mathbf{I}}')"
        r" + {(\hat{\mathbf{I}}' - {\varphi (\tilde{\mathbf{I}}'))}_\texttt{detached}}"
        r"\big)^{T}",
        # r"\mathbf{I} = \hat{\mathbf{I}}' "
        # r"- {{\varphi (\tilde{\mathbf{I}}')^{T}}_\texttt{detached}} "
        # r"+ {\varphi (\tilde{\mathbf{I}}')^{T}}",
        color=BLACK,
    )
    ste_trick_cite = bib.slide_short_cite(
        "oord2018neuraldiscreterepresentationlearning"
    )
    ste_formula = VGroup(
        Tex("Straight-Through Estimator", color=BLACK, font_size=36),
        Brace(ste_formula, UP, buff=0.1, color=BLACK),
        ste_formula,
    ).arrange(DOWN, buff=0.1)
    # ste_brace = Brace(ste_formula, UP, buff=0.1, color=BLACK)
    # ste_labeled_brace = ste_brace.get_text("Straight-Through Estimator", buff=0.1, color=BLACK)
    ste_formula = VGroup(ste_formula, ste_trick_cite).arrange(RIGHT, buff=0.5)
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
        tex_template=myTemplate,
    )

    argmax_formula = VGroup(
        Tex("One-Hot Argmax", color=BLACK, font_size=36),
        Brace(argmax_formula, UP, buff=0.1, color=BLACK),
        argmax_formula,
    ).arrange(DOWN, buff=0.1)

    return SlideWithBlocks(
        title="Constrained Gumbel-Softmax",
        subtitle=None,
        blocks=[
            alert_block_1,
            example_block_1,
            alert_block_2,
            example_block_2,
            alert_block_3,
            example_block_3,
            VGroup(
                VGroup(
                    Tex(r"\textbf{(Eq. 1)}", color=BLACK),
                    constrained_gumbel_formula,
                ).arrange(RIGHT, buff=0.5),
                Tex("such that", color=BLACK),
                VGroup(
                    Tex(r"\textbf{(Eq. 2)}", color=BLACK),
                    noise_formula,
                    Tex(r"with $\tau \in \mathbb{R}_{>0}$", color=BLACK),
                    Tex("and", color=BLACK),
                    Tex(r"\textbf{(Eq. 3)}", color=BLACK),
                    constrained_mask,
                    Tex(r"for $\theta \in [0, 1]$", color=BLACK),
                ).arrange(RIGHT, buff=0.5),
                Tex("followed by", color=BLACK),
                VGroup(
                    Tex(r"\textbf{(Eq. 4)}", color=BLACK),
                    ste_formula,
                ).arrange(RIGHT, buff=0.5),
                Tex("where ", color=BLACK),
                VGroup(
                    Tex(r"\textbf{(Eq. 5)}", color=BLACK),
                    argmax_formula,
                ).arrange(RIGHT, buff=0.5),
            ).arrange(DOWN, buff=0.5),
        ],
    )


class CO(SlideShow):
    def __init__(self, **kwargs):
        super().__init__(
            slides=[
                # introduce necessary notation & formula
                get_notation(),
                # introduce the overall idea, make NFN more like DNN for flexibility
                relax_links(),
                # use gumbel max-trick to sample from a categorical distribution (the rules)
                # issue_with_logits(),
                # # how to avoid violating epsilon-completeness w/ gumbel max-trick
                # # why_modify_gumbel(),  # CUT - don't focus on negative results
                # # avoiding_invalid_selections(),  # CUT - don't focus on negative results
                # # introduce the gumbel max-trick formula
                # gumbel_noise(),
                # # bound the logits used for it to prevent numerical instability
                # # fix_numerical_stability(),  # NO LONGER NEEDED FOR DEFENSE
                # # constrain gumbel-softmax to avoid invalid rules that violate epsilon-completeness
                constrained_gumbel_softmax(),
                # # briefly mention epsilon-delayed update to premise layer
                # why_e_delayed(),
            ],
            **kwargs
        )


if __name__ == "__main__":
    CO().render()
