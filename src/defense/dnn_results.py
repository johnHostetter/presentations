from manim_slides import Slide
from manim import config, BLACK, WHITE, ImageMobject, FadeIn, FadeOut, Tex, Group, DOWN

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

class ResultsDNN(Slide):
    def __init__(self):
        super().__init__()

    def construct(self):
        img = ImageMobject(get_project_root() / "defense/images/tmp_dnn_results.png").scale(3.5)
        caption = Tex(
            "Best hyperparameters identified for DNNs trained by Duel DDQL using TPE.",
            color=BLACK
        ).scale(0.5)
        group = Group(img, caption).arrange(DOWN)
        self.wait(1)
        self.next_slide()
        self.play(FadeIn(group))
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(group))
        self.wait(1)
        self.next_slide()

if __name__ == "__main__":
    ResultsDNN().render()