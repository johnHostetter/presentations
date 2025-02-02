from typing import Union, List
from manim import config, ImageMobject, Tex, Group, VGroup, WHITE, BLACK, Any, DOWN
from manim_slides.slide import Slide

from manim_beamer.bibtex import BibTexManager
from manim_beamer.slides import SlideShow, SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL
from src.defense.publications import Publications
from src.oral_proposal.studies.pyrenees import (
    IntelligentTutoringSystemResults,
)
from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class CEWStudy(SlideShow):
    def __init__(self, **kwargs):
        super().__init__(slides=[CEWResults(), cew_summary()], **kwargs)


class CEWDiagram(Slide):
    def __init__(self, selected_idx: Union[None, int], *args: Any, **kwargs):
        super().__init__(*args, **kwargs)
        self.img_dir = get_project_root() / "assets" / "images" / "cew_diagram"
        self.diagram_caption = "Self-organization with CLIP-ECM-Wang-Mendel (CEW)."
        self.bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")
        self.selected_idx: Union[None, int] = selected_idx

    def construct(self):
        for file_idx, file_name in enumerate(
            [
                "overview.png",
                "clip_highlighted.png",
                "ecm_highlighted.png",
                "wm_highlighted.png",
                "fcql_highlighted.png",
            ]
        ):
            if self.selected_idx is not None and file_idx != self.selected_idx:
                continue
            self.diagram_img = ImageMobject(self.img_dir / file_name)
            self.caption_tex = (
                Tex(self.diagram_caption, color=BLACK)
                .scale(0.7)
                .next_to(self.diagram_img, DOWN)
            )
            self.citation_vgroup: VGroup = Publications.convert_entry_to_long_pub(
                self.bib, self.bib["hostetter2023self"]
            ).scale(0.5)
            content = Group(
                self.diagram_img, self.caption_tex, self.citation_vgroup
            ).arrange(DOWN, buff=0.5)
            self.add(content)
            self.wait(1)
            self.next_slide()


class CEW0(CEWDiagram):
    def __init__(self, *args: Any, **kwargs):
        super().__init__(selected_idx=0, *args, **kwargs)


class CEW1(CEWDiagram):
    def __init__(self, *args: Any, **kwargs):
        super().__init__(selected_idx=1, *args, **kwargs)


class CEW2(CEWDiagram):
    def __init__(self, *args: Any, **kwargs):
        super().__init__(selected_idx=2, *args, **kwargs)


class CEW3(CEWDiagram):
    def __init__(self, *args: Any, **kwargs):
        super().__init__(selected_idx=3, *args, **kwargs)


class CEW4(CEWDiagram):
    def __init__(self, *args: Any, **kwargs):
        super().__init__(selected_idx=4, *args, **kwargs)


class CEWResults(IntelligentTutoringSystemResults):
    def __init__(self):
        data: List[List[str]] = [
            [
                "CEW (N = 45)",
                ".744 (.138)",
                ".803 (.163)",
                ".187 (.658)",
                "1.58 (.680)",
            ],
            [
                "Expert (N = 47)",
                ".761 (.189)",
                ".683 (.165)",
                "-1.55 (3.80)",
                "1.80 (.946)",
            ],
        ]
        super().__init__(data, highlighted_columns=[2, 3])


def cew_summary() -> SlideWithList:
    """
    Create a slide summarizing my AAMAS 2023 paper.

    Returns:
        The slide with a short summary.
    """
    bibtex_manager = BibTexManager(
        path=get_project_root() / "oral_proposal" / "ref.bib"
    )
    return SlideWithList(
        title="Offline Model-Free Fuzzy Reinforcement Learning",
        subtitle="A Preliminary Systematic Design Process of NFNs",
        width_buffer=6.0,
        beamer_list=BL(
            items=[
                bibtex_manager.cite_entry(
                    bibtex_manager["hostetter2023self"], num_of_words=8
                ),
                "Primary Intuition",
                ItemizedList(
                    items=[
                        "CLIP constructs fuzzy sets & ECM identifies exemplars",
                        "Wang-Mendel algorithm constructs fuzzy rules from exemplars",
                        "Modify Fuzzy Q-Learning w/ CQL augmentation and train the NFN offline",
                    ]
                ),
                "Summary",
                ItemizedList(
                    items=[
                        "Effectiveness shown in Cart Pole & ITS",
                        "Great potential for offline RL if:",
                        BL(
                            items=[
                                "Limited data is available",
                                "Possible human expert knowledge",
                                "Need interpretation & accuracy",
                            ]
                        ),
                    ]
                ),
                "Contributions",
                ItemizedList(
                    items=[
                        "First dedicated offline model-free RL process w/ NFNs",
                        "Works well in high-dimensional spaces",
                    ]
                ),
                "Limitations",
                ItemizedList(
                    items=[
                        "The premises of fuzzy logic rule grows linear w/ number of inputs",
                        "Evaluated only on Cart Pole and our ITS",
                        "Computer vision",
                    ]
                ),
            ]
        ),
    )


if __name__ == "__main__":
    CEWDiagram(selected_idx=None).render()
    for idx in range(5):
        eval(f"CEW{idx}().render()")
    # CEWStudy().render()
