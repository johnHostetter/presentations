from manim import config, BLACK, WHITE, ImageMobject, Write, SVGMobject, Unwrite
from manim_slides import Slide
from natsort import natsorted

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class Farewell(Slide):
    def __init__(self):
        super().__init__()
        self.people_image_dir = get_project_root() / "assets" / "people"
        self.wku_image_dir = get_project_root() / "assets" / "images"

    def construct(self):
        prev_img = None

        for sub_dir in ["evelyn", "wedding"]:
            self.wait(1)
            self.next_slide(loop=True)
            self.iter_dir(
                self.people_image_dir, sub_dir=sub_dir, prev_img=prev_img, scale=0.25
            )

        self.wait(1)
        self.next_slide()

        logo_svg = SVGMobject(
            str(self.wku_image_dir / "wku" / "wkucupboxline.svg")
        ).scale(2.0)
        self.play(Write(logo_svg))

        self.wait(1)
        self.next_slide()

        self.play(Unwrite(logo_svg))

        self.wait(1)
        self.next_slide(loop=True)
        self.iter_dir(self.wku_image_dir, sub_dir="wku", prev_img=None, scale=1.0)

        self.wait(1)
        self.next_slide()

    def iter_dir(self, image_dir, sub_dir, prev_img, scale: float = 0.5):
        for img_path in natsorted((image_dir / sub_dir).rglob("*.jpg")):
            # prev_img = self.add_image(img_path)
            prev_img = ImageMobject(str(img_path)).scale(scale)
            self.add(prev_img)
            self.wait(3)
            self.remove(prev_img)
            # self.play(FadeIn(prev_img))
        return prev_img


if __name__ == "__main__":
    Farewell().render()
