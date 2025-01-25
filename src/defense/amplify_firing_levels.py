from manim_slides import Slide
from natsort import natsorted
from manim import ImageMobject, Group, RIGHT, ReplacementTransform, FadeIn, config, WHITE, BLACK, \
    Tex, DOWN, UP, Write

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

class AmplifyFiringLevels(Slide):
    def __init__(self):
        super().__init__()
        self.image_dir = get_project_root() / "defense" / "images" / "firing_levels"

    def construct(self):
        sorted_images = natsorted((self.image_dir / "sorted").glob("*.png"))
        unsorted_images = natsorted((self.image_dir / "unsorted").glob("*.png"))

        prev_images = None
        for unsorted_img_path, sorted_img_path in list(zip(unsorted_images, sorted_images))[:3]:

            unsorted_img = ImageMobject(unsorted_img_path)
            sorted_img = ImageMobject(sorted_img_path)
            images = Group(
                unsorted_img, sorted_img
            ).arrange(RIGHT)
            unsorted_img_caption = Tex(
                "(1) Unsorted", color=BLACK).scale(0.5).next_to(unsorted_img, DOWN)
            sorted_img_caption = Tex(
                "(2) Sorted", color=BLACK).scale(0.5).next_to(sorted_img, DOWN)
            images_caption = Tex(
                "Example firing levels across 256 fuzzy logic rules each with 1600 conditions.",
                color=BLACK
            ).scale(0.75).next_to(images, 3 * DOWN)
            images.add(images_caption)
            if prev_images is None:
                self.play(
                    Write(unsorted_img_caption),
                    Write(sorted_img_caption),
                    FadeIn(*images)
                )
            else:
                try:
                    # try to replace the previous images if they are the same shape
                    self.play(ReplacementTransform(prev_images, images))
                except AssertionError:
                    self.play(FadeIn(*images))
            prev_images = images
            self.wait(1)
            self.next_slide()

        self.wait(1)

if __name__ == "__main__":
    AmplifyFiringLevels().construct()
