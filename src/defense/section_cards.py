from manim import Tex

from manim_beamer.slides import PromptSlide


class PastResearch(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="Prior Research in\\\\Existing Construction Paradigms",
            skip=False,
            default_m_object=Tex
        )

class CurrentResearch(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="A New Construction Paradigm",
            skip=False,
            default_m_object=Tex
        )

if __name__ == "__main__":
    PastResearch().render()
    CurrentResearch().render()
