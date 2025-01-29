from manim_beamer.slides import PromptSlide


class PastResearch(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="Previous Research",
            skip=False,
        )


class CurrentResearch(PromptSlide):
    def __init__(self):
        super().__init__(
            prompt="Current Research",
            skip=False,
        )


if __name__ == "__main__":
    PastResearch().render()
    CurrentResearch().render()
