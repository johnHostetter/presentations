from manim import *
from manim_slides import Slide
from pyrr.rectangle import height

from manim_beamer.bibtex import BibTexManager
from manim_beamer.slides import SlideWithList, SlideWithBlocks

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


def high_dim_trick() -> SlideWithList:
    """
    Create a slide discussing how to use the Gumbel-Max Trick.

    Returns:
        The slide describing how Gumbel noise is used to add stochasticity.
    """
    bibtex_manager = BibTexManager(
        path=get_project_root() / "oral_proposal" / "ref.bib"
    )
    return SlideWithBlocks(
        title="High-Dimensional Inference",
        subtitle=bibtex_manager.cite_entry(
            bibtex_manager["cui_curse_2021"], num_of_words=8
        ),
        blocks=[
            Text("GaussianNoExp", color=BLACK, slant=ITALIC),
            VGroup(
                MathTex(
                    r"""
                    \mu_{i, j}(x_{i}) = -\Bigg(
                    \frac{(x_{i} - \texttt{c}_{i, j})^2}
                    {2\sigma_{i, j}^2}
                    \Bigg)
                    """,
                    color=BLACK,
                ),
            ),
        ],
    )


class CurseOfDimensionality(Slide, MovingCameraScene):
    def __init__(self):
        super().__init__()
        # self.add(Text("Curse of Dimensionality", color=BLACK, slant=ITALIC))
        self.bibtex_manager = BibTexManager(
            path=get_project_root() / "oral_proposal" / "ref.bib"
        )
        self.play_indicate: bool = False
        self.play_substitute: bool = False

    def construct(self):
        self.camera.frame.save_state()
        citation: str = self.bibtex_manager.cite_entry(
            self.bibtex_manager["cui_curse_2021"], num_of_words=8
        )

        citation_tex = Tex(citation, color=DARK_BLUE).to_edge(UP).scale(0.75)
        # group: VGroup = VGroup(citation_tex)

        self.play(Create(citation_tex))
        self.wait(1)
        self.next_slide()

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        # the following line is needed to use the mathcal font
        myTemplate.add_to_preamble(r"\usepackage[cal=boondox]{mathalfa}")

        fuzzy_logic_rule_activation_in_tsk = (
            r"\prod\limits_{i \in I_{\mathcal{C}}} \mathcal{m}_{u}(i)(x_{i})"
        )
        # weighed_fuzzy_rule_in_tsk = r"\mathcal{g}_{u} \big(" + fuzzy_logic_rule_activation_in_tsk + r"\big )"
        limit_tsk = r"\sum\limits_{u \in U}"
        # tsk_formula = MathTex(
        #     r"\mathfrak{F}_{\text{TSK}}(\mathbf{x}) = "
        #     r"\frac{"
        #     rf"{limit_tsk}"
        #     rf"{weighed_fuzzy_rule_in_tsk}"
        #     # r"\mathcal{g}_{u}"
        #     # r"\big("
        #     # r"\prod\limits_{i \in I_{\mathcal{C}}}"
        #     # r"\mathcal{m}_{u}(i)(x_{i})"
        #     # r"\big )"
        #     r"}"
        #     r"{"
        #     rf"{limit_tsk}"
        #     r"\big("
        #     rf"{fuzzy_logic_rule_activation_in_tsk}"
        #     r"\big )"
        #     r"}",
        #     color=BLACK,
        #     tex_template=myTemplate,  # IMPORTANT
        #     # substrings_to_isolate=fuzzy_logic_rule_activation_in_tsk,
        # ).next_to(citation_tex, DOWN)
        tsk_function_tex = MathTex(
            r"\mathfrak{F}_{\text{TSK}}(\mathbf{x}) = ",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        ).next_to(citation_tex, DOWN)
        tsk_formula = MathTex(
            # r"\mathfrak{F}_{\text{TSK}}(\mathbf{x})",
            # r"=",
            rf"{limit_tsk}",
            r"\mathcal{g}_{u} \Big(",
            rf"{fuzzy_logic_rule_activation_in_tsk}",
            r"\Big )",
            r"\over",
            rf"{limit_tsk}",
            rf"{fuzzy_logic_rule_activation_in_tsk}",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        )
        tsk_all = (
            VGroup(Tex(r"\textbf{(Eq. 1)}", color=BLACK), tsk_function_tex, tsk_formula)
            .arrange(RIGHT)
            .next_to(citation_tex, DOWN)
        )

        # tsk_formula[4].set_color(GREEN)
        # tsk_formula[-1].set_color(GREEN)
        # group.add(tsk_formula)

        tsk_all_1 = MathTex(
            r"\mathfrak{F}_{\text{TSK}}(\mathbf{x}) = \frac{"
            r"\sum\limits_{u \in U} \mathcal{g}_{u}"
            r"\Big("
            r"\prod\limits_{i \in I_{\mathcal{C}}} \exp \big("
            r"-\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2} "
            r"\big )"
            r"\Big )"
            r"}{"
            r"\sum\limits_{u \in U}"
            r"\Big("
            r"\prod\limits_{i \in I_{\mathcal{C}}} \exp \big("
            r"-\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2} "
            r"\big )"
            r"\Big )"
            r"}",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        )

        tsk_all_1 = VGroup(Tex(r"\textbf{(Eq. 2)}", color=BLACK), tsk_all_1).arrange(RIGHT).next_to(tsk_all, DOWN)

        if self.play_substitute:
            # only need a portion of the formula since it will substitute the previous one
            gaussian_tsk_formula = MathTex(
                # r"\mathfrak{F}_{\text{TSK}}(\mathbf{x}) = \frac{"
                # r"\sum\limits_{u \in U} \mathcal{g}_{u}"
                # r"\Big("
                r"\exp \big("
                r"- \sum\limits_{i \in I_{\mathcal{C}}}"
                r"\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2} "
                r"\big )"
                # r"\Big )"
                # r"}{"
                # r"\sum\limits_{u \in U}"
                # r"\Big("
                # r"\exp \big(- \sum\limits_{i \in I_{\mathcal{C}}}"
                # r"\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2} "
                # r"\big )"
                # r"\Big )"
                r"}",
                color=BLACK,
                tex_template=myTemplate,  # IMPORTANT
            ).move_to(tsk_all.get_center())
        else:
            gaussian_tsk_formula = MathTex(
                r"\mathfrak{F}_{\text{TSK}}(\mathbf{x}) = \frac{"
                r"\sum\limits_{u \in U} \mathcal{g}_{u}"
                r"\Big("
                r"\exp \big("
                r"- \sum\limits_{i \in I_{\mathcal{C}}}"
                r"\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2} "
                r"\big )"
                r"\Big )"
                r"}{"
                r"\sum\limits_{u \in U}"
                r"\Big("
                r"\exp \big(- \sum\limits_{i \in I_{\mathcal{C}}}"
                r"\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2} "
                r"\big )"
                r"\Big )"
                r"}",
                color=BLACK,
                tex_template=myTemplate,  # IMPORTANT
            )
        # group.add(gaussian_tsk_formula)
            gaussian_tsk_formula = VGroup(
                Tex(r"\textbf{(Eq. 3)}", color=BLACK
            ), gaussian_tsk_formula).arrange(RIGHT).next_to(tsk_all_1, DOWN)

        concise_tsk_formula = MathTex(
            r"\mathfrak{F}_{\text{TSK}}(\mathbf{x}) = \sum\limits_{u \in U} \mathcal{g}_{u}(\mathbf{x}) \overline{w}_{u}(\mathbf{x})",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        ).move_to(tsk_all.get_center())

        if not self.play_substitute:
            # if we are not playing the substitution animation,
            # we need to reference the lowest formula
            concise_tsk_formula = VGroup(Tex(r"\textbf{(Eq. 4)}", color=BLACK), concise_tsk_formula).arrange(RIGHT)
            concise_tsk_formula.next_to(gaussian_tsk_formula, DOWN)

        where_tex = (
            Tex("where", color=BLACK)
            .next_to(concise_tsk_formula, DOWN)
            .align_to(concise_tsk_formula, LEFT)
        )
        softmax_formula = MathTex(
            r"\overline{w}_{u}(\mathbf{x}) = \frac{\exp \big ("
            r"{w}_{u}(\mathbf{x})"
            r"\big)"
            r"}{\sum_{u}^{U} \exp \big({w}_{u}(\mathbf{x})\big)}",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        )
        softmax_formula = VGroup(Tex(r"\textbf{(Eq. 5)}", color=BLACK), softmax_formula).arrange(RIGHT)
        brace = Brace(softmax_formula, DOWN, color=DARK_BLUE)
        softmax_lbl = Tex(r"\texttt{softmax}", color=DARK_BLUE).next_to(brace, DOWN)
        labeled_brace = VGroup(brace, softmax_lbl)
        such_that_tex = (
            Tex("such that", color=BLACK)
            .next_to(softmax_formula, DOWN)
            .align_to(softmax_formula, LEFT)
        )
        weight_sum_term_formula = MathTex(
            r"{w}_{u}(\mathbf{x}) = -\sum_{i \in I_{\mathcal{C}}}"
            r"\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2}",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        )
        weight_sum_term_formula = VGroup(
            Tex(r"\textbf{(Eq. 6)}", color=BLACK), weight_sum_term_formula
        ).arrange(RIGHT)
        or_tex: Tex = Tex("or", color=BLACK)
        weight_mean_term_formula = MathTex(
            r"{w}_{u}(\mathbf{x}) = -\frac{1}{|\mathcal{C}|} \sum_{i \in I_{\mathcal{C}}}"
            r"\frac{({x}_{i} - {c}_{i, j, u}) ^ 2}{2\sigma_{i, j, u} ^ 2}",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        )
        weight_mean_term_formula = VGroup(
            Tex(r"\textbf{(Eq. 7)}", color=BLACK), weight_mean_term_formula
        ).arrange(RIGHT)
        weight_term_formulas = VGroup(
            weight_sum_term_formula, or_tex, weight_mean_term_formula
        ).arrange()
        group_items = [
            tsk_all,
            tsk_all_1,
            gaussian_tsk_formula,
            concise_tsk_formula,
            where_tex,
            softmax_formula,
            labeled_brace,
            such_that_tex,
            weight_term_formulas,
        ]
        if self.play_substitute:
            group_items.insert(0, gaussian_tsk_formula)
        group: Group = Group(*group_items)
        group.arrange(DOWN, buff=0.5, center=False, aligned_edge=LEFT)

        softmax_common_trick_formula = MathTex(
            r"\overline{w}_{u}(\mathbf{x}) = \frac{\exp \big ("
            r"{w}_{u}(\mathbf{x}) - \max{w}_{u}(\mathbf{x})"
            r"\big)"
            r"}{\sum_{u}^{U} \exp \big({w}_{u}(\mathbf{x}) - \max{w}_{u}(\mathbf{x}) \big)}",
            color=BLACK,
            tex_template=myTemplate,  # IMPORTANT
        )
        softmax_common_trick_formula = VGroup(
            Tex(r"\textbf{(Eq. 5)}", color=BLACK),
            softmax_common_trick_formula,
        ).arrange(RIGHT).move_to(softmax_formula.get_center())
        group.add(softmax_common_trick_formula)

        annotation_table = Table(
            [
                ["Neuro-Fuzzy Network"],
                ["Input Vector"],
                ["Set of Universal Identifiers for Fuzzy Rules"],
                ["Set of Condition Attributes"],
                ["Index Set of Condition Attributes"],
                ["$i^{th}$ condition attribute"],
                ["$j^{th}$ fuzzy set (i.e., linguistic term)"],
                ["$u^{th}$ fuzzy rule"],
                ["Function to Retrieve Fuzzy Rule's Premises"],
                ["Fuzzy Rule Consequent"],
                ["Gaussian Center"],
                ["Gaussian Standard Deviation"],
            ],
            row_labels=[
                MathTex("\mathfrak{F}", color=BLACK, tex_template=myTemplate),
                MathTex("\mathbf{x}", color=BLACK, tex_template=myTemplate),
                MathTex("U", color=BLACK, tex_template=myTemplate),
                MathTex("\mathcal{C}", color=BLACK, tex_template=myTemplate),
                Tex("$I_\mathcal{C}$", color=BLACK, tex_template=myTemplate),
                MathTex("i", color=BLACK, tex_template=myTemplate),
                MathTex("j", color=BLACK, tex_template=myTemplate),
                MathTex("u", color=BLACK, tex_template=myTemplate),
                MathTex("\mathcal{m}_{u}", color=BLACK, tex_template=myTemplate),
                MathTex("\mathcal{g}_{u}", color=BLACK, tex_template=myTemplate),
                MathTex("c_{i, j, u}", color=BLACK, tex_template=myTemplate),
                MathTex("\sigma_{i, j, u}", color=BLACK, tex_template=myTemplate),
            ],
            col_labels=[
                # Tex("Symbol", color=BLACK, tex_template=myTemplate),
                Tex("Meaning", color=BLACK, tex_template=myTemplate)
            ],
            element_to_mobject=lambda x: Tex(
                x, color=BLACK, tex_template=myTemplate
            ),  # use LaTeX for the entries
        ).next_to(gaussian_tsk_formula, RIGHT).scale(0.75)
        annotation_table.get_horizontal_lines().set_color(BLACK)
        annotation_table.get_vertical_lines().set_color(BLACK)

        # CREATE ALL LABELS AND BRACES FOR SUM & MEAN
        sum_brace = Brace(weight_sum_term_formula, DOWN, color=DARK_BLUE)
        sum_brace_lbl = Tex(r"\texttt{sum}", color=DARK_BLUE).next_to(
            sum_brace, DOWN
        )
        sum_surrounding_rectangle = SurroundingRectangle(
            weight_sum_term_formula, color=DARK_BLUE
        )
        labeled_sum_brace = VGroup(sum_brace, sum_brace_lbl, sum_surrounding_rectangle)
        mean_brace = Brace(weight_mean_term_formula, DOWN, color=DARK_BLUE)
        mean_brace_lbl = Tex(r"\texttt{mean}", color=DARK_BLUE).next_to(
            mean_brace, DOWN
        )
        mean_surrounding_rectangle = SurroundingRectangle(
            weight_mean_term_formula, color=DARK_BLUE
        )
        labeled_mean_brace = VGroup(mean_brace, mean_brace_lbl, mean_surrounding_rectangle)

        self.play(Create(tsk_all), Create(annotation_table))

        if self.play_indicate:
            self.wait(1)
            self.next_slide(loop=True)
            self.play(Indicate(tsk_formula[2]), Indicate(tsk_formula[-1]))

        self.wait(1)
        self.next_slide()

        # incl. everything so it can all be seen
        group.add(
            citation_tex, tsk_formula, tsk_function_tex, gaussian_tsk_formula,
            annotation_table, labeled_sum_brace, labeled_mean_brace
        )
        self.play(
            Create(tsk_all_1),
            self.camera.frame.animate.move_to(group.get_center()).set(
                width=group.width + 2, height=group.height + 2,
            ),
        )

        self.wait(1)
        self.next_slide()

        if self.play_substitute:
            new_numerator = gaussian_tsk_formula.copy().move_to(tsk_formula[2])
            numerator_group = VGroup(
                *tsk_formula[:2].copy(),
                new_numerator,
                *tsk_formula[3:4].copy(),
            ).arrange(
                RIGHT, buff=0.1
            )  # .move_to(tsk_formula[2])

            animations = []
            for i in range(2):  # move the items to the left of the replacement
                animations.append(tsk_formula[1 - i].animate.move_to(numerator_group[i]))
            for i in range(3, 4):  # move the items to the right of the replacement
                animations.append(tsk_formula[i].animate.move_to(numerator_group[i]))
            # determine where the bar will be positioned
            reference = (
                tsk_formula[4]
                .next_to(numerator_group, DOWN, buff=0.1)
                .get_boundary_point(LEFT)
            )

            animations.append(tsk_function_tex.animate.next_to(reference, LEFT, buff=1.5))
            # move the overline down a bit
            animations.append(
                tsk_formula[4].animate.next_to(numerator_group, DOWN, buff=0.1)
            )
            animations.append(tsk_formula[4].animate.stretch(1.5, dim=0))

            # replace it in the denominator
            new_denominator = (
                gaussian_tsk_formula.copy()
                .move_to(tsk_formula[-1])
                .next_to(numerator_group, DOWN, buff=0.2)
            )
            animations.append(tsk_formula[5].animate.next_to(new_denominator, LEFT))

            self.play(
                *animations,
                tsk_formula[2].animate.become(new_numerator),
                tsk_formula[-1].animate.become(new_denominator),
            )
            self.wait(1)
            self.next_slide()

            old_formulas = VGroup(
                tsk_function_tex, tsk_formula, new_numerator, new_denominator
            )
            self.play(TransformMatchingTex(old_formulas, concise_tsk_formula))
        else:
            self.play(Create(gaussian_tsk_formula))
            self.wait(1)
            self.next_slide()
            self.play(Create(concise_tsk_formula))
        self.wait(1)
        self.next_slide()

        curr_focus: VGroup = VGroup(softmax_formula, where_tex)
        self.play(
            # group.animate.arrange(DOWN, buff=0.5, center=False, aligned_edge=LEFT),
            Create(softmax_formula),
            Create(where_tex),
            # self.camera.frame.animate.move_to(curr_focus.get_center()).set(
            #     height=group.height + 2
            # ),
        )
        self.wait(1)
        self.next_slide()

        curr_focus.add(such_that_tex, weight_sum_term_formula)
        self.play(
            # group.animate.arrange(DOWN, buff=0.5, center=False, aligned_edge=LEFT),
            Create(such_that_tex),
            Create(weight_sum_term_formula),
            # self.camera.frame.animate.move_to(curr_focus.get_center()).set(
            #     height=group.height + 2
            # ),
        )
        self.wait(1)
        self.next_slide()

        curr_focus.add(or_tex, weight_mean_term_formula)
        self.play(
            Create(or_tex),
            Create(weight_mean_term_formula),
            LaggedStart(Create(labeled_mean_brace), Create(labeled_sum_brace)),
            # self.camera.frame.animate.move_to(group.get_center()).set(
            #     height=group.height + 2, width=weight_term_formulas.width + 2
            # ),
        )
        self.wait(1)
        self.next_slide()

        # emphasize this is the softmax formula
        surrounding_rectangle = SurroundingRectangle(softmax_formula, color=DARK_BLUE)
        self.play(Create(surrounding_rectangle), Create(labeled_brace))
        self.wait(1)
        self.next_slide()

        softmax_common_trick_formula.shift(1.5 * RIGHT)
        new_surrounding_rectangle = SurroundingRectangle(softmax_common_trick_formula, color=DARK_BLUE)
        new_brace = Brace(softmax_common_trick_formula, DOWN, color=DARK_BLUE)
        new_brace_lbl = Tex(r"\texttt{softmax}", color=DARK_BLUE).next_to(new_brace, DOWN)
        labeled_new_brace = VGroup(new_brace, new_brace_lbl)
        self.play(
            LaggedStart(
                AnimationGroup(
                    ReplacementTransform(surrounding_rectangle, new_surrounding_rectangle),
                    ReplacementTransform(labeled_brace, labeled_new_brace),
                ),
                TransformMatchingTex(softmax_formula, softmax_common_trick_formula),
                lag_ratio=0.5,
            )
        )
        # group.remove(softmax_formula)
        # self.wait(1)
        # self.next_slide()
        #
        # # incl. everything so it can all be seen
        # group.add(citation_tex)
        # group.add(tsk_formula)
        # group.add(tsk_function_tex)
        # group.add(gaussian_tsk_formula)
        # self.play(
        #     self.camera.frame.animate.move_to(group.get_center()).set(
        #         width=group.width + 2, height=group.height + 2,
        #     ),
        # )


if __name__ == "__main__":
    # high_dim_trick().render()
    CurseOfDimensionality().render()
