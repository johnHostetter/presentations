from manim import config, BLACK, WHITE, Tex, VGroup, ORIGIN

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
            entry_tex = self.convert_entry_to_long_pub(bib, entry)
            entries[i] = entry_tex

        pending_pub = VGroup(
            Tex(
                r"\textbf{Hostetter, J.}, Saha, A., Islam, M., Barnes, T., and Chi, M. (2025). "
                r"Human-Readable Neuro-Fuzzy Networks from Frequent Yet Discernible Patterns "
                r"in Reward-Based Environments. \textit{(In Review at IJCAI 2025)}.",
                color=BLACK,
                tex_environment="flushleft",
            )
        )
        entries.insert(0, pending_pub)

        super().__init__(
            title="Publications",
            subtitle="",
            beamer_list=ItemizedList(
                items=entries,
                default_m_object=partial(Tex, tex_environment="flushleft"),
            ),
            adjust_by_height=True,
        )

    @staticmethod
    def convert_entry_to_long_pub(bib, entry):
        authors: str  = bib.get_author_last_names_only(entry, et_al=False)
        if "Hostetter, J." in authors:
            authors = authors.replace(
            r"Hostetter, J.", r"\textbf{Hostetter, J.}"
            )  # for apa format
        elif "Hostetter" in authors:
            authors = authors.replace(
            r"Hostetter", r"\textbf{Hostetter}"
            )

        title = entry["title"].replace("{", "").replace("}", "")
        place = entry["booktitle"] if "booktitle" in entry else entry["journal"]
        place = place.replace("{", "").replace("}", "")
        place = rf"\textit{{{place}}}"
        # place = "In " + place.replace("{", "").replace("}", "")

        apa_citation_str: str = f"{authors} ({entry['year']}). {title}. {place}"
        if "pages" in entry:
            apa_citation_str += f", {entry['pages']}."
        else:
            apa_citation_str += "."

        entry_tex = VGroup(
            Tex(
                BibTexManager.wrap_by_word(
                    apa_citation_str, num_of_words=8
                    # f"{authors}. {title} {place}, {entry['year']}.", num_of_words=8
                ),
                color=BLACK,
                tex_environment="flushleft",
            )
        )
        return entry_tex

    def construct(self):
        self.draw(ORIGIN, 1.0, target_scene=self, animate=True)


if __name__ == "__main__":
    Publications().render()
