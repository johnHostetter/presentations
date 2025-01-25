from manim_slides import Slide
from natsort import natsorted
from manim import ImageMobject, Group, RIGHT, ReplacementTransform, FadeIn, config, WHITE, BLACK, \
    Tex, DOWN, UP, Write, FadeOut, Scene

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

class AmplifyFiringLevels(Scene):
    def __init__(self):
        super().__init__()
        self.image_dir = get_project_root() / "defense" / "images" / "firing_levels"

    def construct(self):
        sorted_images = natsorted((self.image_dir / "sorted").glob("*.png"))
        unsorted_images = natsorted((self.image_dir / "unsorted").glob("*.png"))

        prev_title = None
        prev_images = None
        prev_intermediate_firing_type = None
        prev_layer_norm = None
        for unsorted_img_path, sorted_img_path in list(zip(unsorted_images, sorted_images)):
            if int(unsorted_img_path.stem.split("_")[-1]) not in [0]:
                continue  # only show the selected 3 images

            intermediate_firing_type = r"1.5-\texttt{entmax}" if "entmax15" in unsorted_img_path.stem else r"\texttt{softmax}"
            layer_norm = " w/ Layer Normalization" if "norm" in unsorted_img_path.stem else " w/o Layer Normalization"
            title = Tex(
                "Neuro-Fuzzy Network using ",
                intermediate_firing_type, layer_norm,
                color=BLACK
            ).to_edge(UP)

            unsorted_img = ImageMobject(unsorted_img_path)
            sorted_img = ImageMobject(sorted_img_path)
            images = Group(
                unsorted_img, sorted_img
            ).arrange(RIGHT).next_to(title, DOWN)
            unsorted_img_caption = Tex(
                "(1) Unsorted", color=BLACK).scale(0.5).next_to(unsorted_img, DOWN)
            sorted_img_caption = Tex(
                "(2) Sorted", color=BLACK).scale(0.5).next_to(sorted_img, DOWN)
            images_caption = Tex(
                "Example firing levels across 256 fuzzy logic rules each with 1600 conditions.",
                color=BLACK
            ).scale(0.75).next_to(images, 3 * DOWN)
            images.add(images_caption)

            # if prev_intermediate_firing_type is None and prev_layer_norm is None:
            #     self.play(Write(title))
            # elif prev_intermediate_firing_type != intermediate_firing_type or prev_layer_norm != layer_norm:
            #     self.play(FadeOut(prev_title), FadeIn(title))
            #     prev_intermediate_firing_type = intermediate_firing_type
            #     prev_layer_norm = layer_norm

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
            prev_title = title
            self.wait(1)
            # self.next_slide()

        self.wait(1)

if __name__ == "__main__":
    AmplifyFiringLevels().construct()
