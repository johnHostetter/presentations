from typing import List

from manim_slides import Slide
from natsort import natsorted
from manim import ImageMobject, Group, RIGHT, ReplacementTransform, FadeIn, config, WHITE, BLACK, \
    Tex, DOWN, UP, Write, Unwrite, FadeOut

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
        prev_title = None
        prev_images = None
        legend_img_path = self.image_dir / "legend.png"
        legend_img = ImageMobject(legend_img_path).to_edge(DOWN)
        for img_idx in [0, 2, 4]:
            for img_type in ["softmax", "entmax15", "norm_softmax", "norm_entmax15"]:
                sorted_img_path = self.image_dir / "sorted" / f"{img_type}_0_{img_idx}.png"
                unsorted_img_path = self.image_dir / "unsorted" / f"{img_type}_0_{img_idx}.png"
        # for unsorted_img_path, sorted_img_path in list(zip(unsorted_images, sorted_images)):  # cannot be [:4] or greater for some reason
        #     if int(unsorted_img_path.stem.split("_")[-1]) not in [0, 1, 4]:
        #         continue  # only show the selected 3 images
        #     print(unsorted_img_path.stem)
        #     print(sorted_img_path.stem)

                print(sorted_img_path)
                print(unsorted_img_path)

                intermediate_firing_type = r"1.5-\texttt{entmax}" if "entmax15" in unsorted_img_path.stem else r"\texttt{softmax}"
                layer_norm = "w/ Layer Normalization" if "norm" in unsorted_img_path.stem else " w/o Layer Normalization"
                title_str_lst: List[str] = ["Neuro-Fuzzy Network using", intermediate_firing_type, layer_norm]
                tex_string = " ".join(title_str_lst)
                title = Tex(
                    tex_string,
                    color=BLACK
                ).to_edge(UP)
                if prev_title is None:
                    self.play(Write(title))
                elif prev_title.tex_string != tex_string:
                    self.play(FadeOut(prev_title), Write(title))
                else:
                    title = prev_title
                unsorted_img = ImageMobject(unsorted_img_path)
                sorted_img = ImageMobject(sorted_img_path)
                images = Group(
                    unsorted_img, sorted_img
                ).arrange(RIGHT)
                if prev_images is None:
                    unsorted_img_caption = Tex(
                        "(1) Unsorted", color=BLACK).scale(0.5).next_to(unsorted_img, DOWN)
                    sorted_img_caption = Tex(
                        "(2) Sorted", color=BLACK).scale(0.5).next_to(sorted_img, DOWN)
                    images_caption = Tex(
                        "Example firing levels across 256 fuzzy logic rules each with 1600 conditions.",
                        color=BLACK
                    ).scale(0.75).next_to(images, 3 * DOWN)
                    self.play(
                        Write(unsorted_img_caption),
                        Write(sorted_img_caption),
                        Write(images_caption),
                        FadeIn(legend_img),
                        FadeIn(*images)
                    )
                else:
                    # try:
                    #     # try to replace the previous images if they are the same shape
                    #     self.play(ReplacementTransform(prev_images, images))
                    # except AssertionError:
                    self.play(FadeIn(*images), FadeOut(*prev_images))
                prev_images = images
                prev_title = title
                self.wait(1)
                self.next_slide()

        self.wait(1)

if __name__ == "__main__":
    AmplifyFiringLevels().construct()
