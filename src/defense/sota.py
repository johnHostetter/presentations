from manim import (
    config,
    BLACK,
    WHITE,
    Tex,
    DARK_BLUE,
    UP,
    Create,
    ImageMobject,
    DOWN,
    FadeIn,
    Group,
)
from manim_slides import Slide

from manim_beamer.bibtex import BibTexManager
from src.defense.publications import Publications
from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class SOTA(Slide):
    def __init__(self):
        super().__init__()
        # self.add(Text("Curse of Dimensionality", color=BLACK, slant=ITALIC))
        self.bibtex_manager = BibTexManager(
            path=get_project_root() / "oral_proposal" / "ref.bib"
        )
        self.image_dir = get_project_root() / "assets" / "images"
        self.play_indicate: bool = False
        self.play_substitute: bool = False

    def construct(self):
        # self.camera.frame.save_state()
        # citation: str = self.bibtex_manager.cite_entry(
        #     self.bibtex_manager["BUTT2024102182"], num_of_words=8
        # )

        # self.play(Create(citation_tex))
        # self.wait(1)
        # self.next_slide()

        pac_man_img = ImageMobject(str(self.image_dir / "pac_man.png")).scale(2.0)
        pac_man_grid_img = ImageMobject(str(self.image_dir / "pac_man_grid.png")).scale(
            2.0
        )

        # citation_tex = Tex(citation, color=DARK_BLUE).to_edge(UP).scale(0.75)
        citation_tex = Publications.convert_entry_to_long_pub(
            self.bibtex_manager, self.bibtex_manager["BUTT2024102182"]
        ).scale(0.5)
        # group: VGroup = VGroup(citation_tex)

        self.play(
            FadeIn(
                Group(pac_man_img, pac_man_grid_img, citation_tex).arrange(DOWN)
            )
        )
        self.wait(1)


if __name__ == "__main__":
    SOTA().render()
