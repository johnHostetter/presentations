from manim_slides import Slide
from manim import (
    config,
    BLACK,
    WHITE,
    ImageMobject,
    FadeIn,
    FadeOut,
    Tex,
    Group,
    DOWN,
    RED,
)

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class ResultsTmp(Slide):
    def __init__(self, file_name: str, architecture: str):
        super().__init__()
        self.file_name = file_name
        self.architecture = architecture

    def construct(self):
        img = ImageMobject(
            get_project_root() / f"defense/images/{self.file_name}"
        ).scale(1.5)
        caption = Tex(
            f"Best hyperparameters identified for {self.architecture} trained by Duel DDQL using TPE.",
            color=BLACK,
        ).scale(0.5)
        tmp_caption = Tex("NOTE: This is a placeholder.", color=RED).scale(0.5)
        group = Group(img, caption, tmp_caption).arrange(DOWN)
        self.wait(1)
        self.next_slide()
        self.play(FadeIn(group))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(group))
        self.wait(1)
        self.next_slide()


class ResultsDNN(ResultsTmp):
    def __init__(self):
        super().__init__("tmp_dnn_results.png", architecture="DNNs")


class ResultsNFN(ResultsTmp):
    def __init__(self):
        super().__init__("tmp_nfn_results.png", architecture="NFNs")


if __name__ == "__main__":
    ResultsDNN().render()
    ResultsNFN().render()
