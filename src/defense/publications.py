from manim import config, BLACK, WHITE, Tex

from manim_beamer.bibtex import BibTexManager
from manim_beamer.lists import ItemizedList
from manim_beamer.slides import SlideWithList
from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

class Publications(SlideWithList):
    """
    Create a slide containing a list of my publications.
    """
    def __init__(self):
        bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")
        from functools import partial

        entries = [
            bib["mirajul2024edm"],
            bib["abdelshiheed2024example"],
            bib["hostetter2023xai"],
            bib["hostetter2023leveraging"],
            bib["hostetter2023latent"],
            bib["hostetter2023self"],
            bib["abdelshiheed2023bridging"],
            bib["abdelshiheed2023leveraging"],
            bib["abdelshiheed2022mixing"],
            bib["abdelshiheed2022power"],
        ]
        for i, entry in enumerate(entries):
            authors = bib.get_author_last_names_only(entry, et_al=False)
            title = entry["title"].replace("{", "").replace("}", "")
            place = entry["booktitle"] if "booktitle" in entry else entry["journal"]
            place = "In " + place.replace("{", "").replace("}", "")
            entries[i] = BibTexManager.wrap_by_word(f"{authors}. {title} {place}, {entry['year']}.", num_of_words=8)

        super().__init__(
            title="Publications",
            subtitle="",
            beamer_list=ItemizedList(
                items=entries,
                default_m_object=partial(Tex, tex_environment="flushleft")
            ),
        )

if __name__ == "__main__":
    Publications().render()