from manim import *
from manim_beamer.slides import SlideWithList
from manim_beamer.lists import ItemizedList, BulletedList as BL

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class WKUFit(SlideWithList):
    """
    Create a slide with my plan for upcoming 5 years, and how it fits with position & department.

    Returns:
        The slide with a list of studies.
    """

    def __init__(self):
        super().__init__(
            title="Plan for the Next 5 Years",
            subtitle=None,
            width_buffer=12.0,
            beamer_list=ItemizedList(
                items=[
                    "Continue improving transparency in AI",
                    "XAI Pedagogical Policies in Intelligent Tutoring Systems (ITSs)",
                    BL(
                        items=[
                            "Secure Funding",
                            "Assemble a Research Team",
                            "Build an ITS for AI & Data Science Education",
                        ]
                    ),
                    "New: Human-in-the-Loop XAI Recommendation Systems",
                    BL(
                        items=[
                            "Healthcare",
                            "Supply Chain Management",
                        ]
                    ),
                ]
            ),
        )


if __name__ == "__main__":
    WKUFit().render()
