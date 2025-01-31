from manim import Tex

from manim_beamer.slides import PromptSlide


class PastResearch(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="Prior Research in\\\\Existing Construction Paradigms",
            skip=False,
            default_m_object=Tex,
        )


class CurrentResearch(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="A New Construction Paradigm", skip=False, default_m_object=Tex
        )


class Distill(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="Distillation \& Transformation", skip=False, default_m_object=Tex
        )


class SelfOrganize(PromptSlide):
    def __init__(self):
        super().__init__(prompt="Self-Organization", skip=False, default_m_object=Tex)


class Exp(PromptSlide):
    def __init__(self):
        super().__init__(prompt="Experiments", skip=False, default_m_object=Tex)

class Scenarios(PromptSlide):
    def __init__(self):
        super().__init__(prompt="Scenarios", skip=False, default_m_object=Tex)


if __name__ == "__main__":
    for slide in [PastResearch, CurrentResearch, Distill, SelfOrganize, Exp, Scenarios]:
        slide().render()
