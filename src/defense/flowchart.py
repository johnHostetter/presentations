import re
from manim import *
from manim_slides import Slide
from natsort import natsorted

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}

class Flowchart(Slide, MovingCameraScene):
    def __init__(self):
    # def __init__(self, image_dir: Path):
        super().__init__()
        self.image_dir = Path("test_images")
        self.objects_to_be_shifted = {}

    def construct(self):
        self.camera.frame.save_state()
        prev_image = None
        prev_text = None
        # regex_pattern = re.compile(r"^center_\d+_exemplar$")  # no need for .jpg since stem cuts it
        # regex_pattern = re.compile(r"_axes$")  # no need for .jpg since stem cuts it
        i = 0

        # get time-steps that the agent was consulted, these are stored in optuna as folders
        time_steps = sorted(
            [
                int(folder.stem) for folder in (self.image_dir / "optuna").iterdir()
                if folder.is_dir()
            ]
        )

        START_IDX: int = 397  # was 470 or 500 for 'test_images' directory (long is 4434)
        END_IDX: int = 530  # was 530 for 'test_images' directory (long is 4499)
        image_paths = natsorted((self.image_dir / "inputs" / "original_no_axes").iterdir())[START_IDX:]
        resized_paths = natsorted((self.image_dir / "inputs" / "resized_no_axes").iterdir())[START_IDX:]

        prev_group_jpg = None
        for original_path, resized_path in zip(image_paths, resized_paths):
            if original_path.stem != resized_path.stem:
                raise ValueError(
                    f"Original and Resized image paths do not match: {original_path.stem} != {resized_path.stem}"
                )

            print(original_path)
            left_jpg = ImageMobject(original_path)
            left_text = Text(
                "Original Image", font_size=24, color=BLACK
            ).next_to(left_jpg, DOWN).set_z_index(100)  # bring to front with a very high z-index
            right_jpg = ImageMobject(resized_path).next_to(left_jpg, RIGHT)
            right_text = Text(
                "Resized Image", font_size=24, color=BLACK
            ).next_to(right_jpg, DOWN).set_z_index(100)  # bring to front with a very high z-index
            group_jpg = Group(
                Group(left_jpg, left_text),
                Group(right_jpg, right_text)
            ).move_to(ORIGIN)
            if prev_group_jpg is None:
                self.play(FadeIn(group_jpg, run_time=1))
            elif isinstance(prev_group_jpg, Group):
                self.play(
                    ReplacementTransform(prev_group_jpg, group_jpg, run_time=(1/10))
                )
            prev_group_jpg = group_jpg
            del left_jpg, left_text, right_text, group_jpg  # free up memory
            self.wait(1/10)

            curr_time_step: int = int(original_path.stem)
            if curr_time_step in time_steps:  # stem is the time-step
                # self.shift_objects(direction=RIGHT)  # send the objects out of view

                # reveal optuma figure for the time-step
                optuna_path = self.image_dir / "optuna" / original_path.stem
                occlusion_jpg = ImageMobject(optuna_path / "occlusion.png").scale(0.89).move_to(right_jpg).shift(0.125 * DOWN).shift(4.53 * RIGHT)

                rectangle = Rectangle(
                    width=occlusion_jpg.get_width() * 0.89,
                    height=occlusion_jpg.get_height() * 0.1,
                    fill_color=WHITE,
                    fill_opacity=1.0,
                ).move_to(occlusion_jpg).shift(1.7 * UP)  # used to cover up the plot's titles
                self.play(
                    FadeIn(
                        occlusion_jpg, rectangle
                    ),
                    self.camera.frame.animate.move_to(occlusion_jpg)
                )
                self.wait(1)
                self.play(
                    FadeOut(occlusion_jpg, rectangle)
                )
                del occlusion_jpg, rectangle  # free up memory

                self.shift_objects(direction=LEFT)  # bring back into view

                # reveal the convolutional layers

                conv_paths = natsorted(
                    (self.image_dir / "after_conv" / original_path.stem).iterdir()
                )
                self.wait(1)
                right_most_jpg = right_jpg
                for conv_idx, conv_path in enumerate(conv_paths):
                    print(conv_path)
                    # group_jpg.shift(LEFT * 5)
                    if "matching" in conv_path.stem:
                        # transform the color scheme to match with NFNs
                        conv_jpg = ImageMobject(conv_path).scale(0.5).move_to(right_most_jpg)
                        self.play(
                            ReplacementTransform(
                                right_most_jpg,
                                conv_jpg
                            ),
                        )
                    else:
                        conv_jpg = ImageMobject(conv_path).scale(0.5).next_to(right_most_jpg, RIGHT).shift(1.5 * RIGHT)
                        conv_text = Text(
                            f"After Convolutional Layer {conv_idx + 1}", font_size=24, color=BLACK
                        ).next_to(conv_jpg, DOWN)
                        # TODO: fix this so it replaces the previous image
                        if f"{conv_path.parent.name}_{conv_idx}" in self.objects_to_be_shifted:
                            self.play(
                                ReplacementTransform(
                                    self.objects_to_be_shifted[f"{conv_path.parent.name}_{conv_idx}"],
                                    Group(conv_jpg, conv_text)
                                ),
                                self.camera.frame.animate.move_to(conv_jpg)
                            )
                        else:
                            self.play(
                                FadeIn(Group(conv_jpg, conv_text), run_time=1),
                                self.camera.frame.animate.move_to(conv_jpg)
                            )
                        right_most_jpg = conv_jpg
                        self.objects_to_be_shifted[f"{conv_path.parent.name}_{conv_idx}"] = Group(
                            conv_jpg, conv_text
                        )
                    self.wait(1)

                # compare to the NFN's center exemplars
                mu_paths = natsorted(
                    (self.image_dir / "mu" / original_path.stem).iterdir()
                )

                INCREASE_HEIGHT_FACTOR: float = 1.25  # increase the height of the camera frame
                mu_centers_pattern = re.compile(r"^center_\d+_exemplar$")  # no need for .jpg since stem cuts it
                mu_degrees_pattern = re.compile(r"^center_\d+_mu$")  # no need for .jpg since stem cuts it
                rule_exemplar_pattern = re.compile(r"^rule_\d+_exemplar$")  # no need for .jpg since stem cuts it
                rule_mu_pattern = re.compile(r"^rule_\d+_mu$")  # no need for .jpg since stem cuts it
                right_most_jpg = self.add_mu_items(
                    mu_paths, right_most_jpg, regex_pattern=mu_centers_pattern, text="Exemplary Percepts"
                )
                # objects_to_be_shifted.append(right_most_jpg)
                self.play(self.camera.frame.animate.set(height=right_most_jpg.get_height() * INCREASE_HEIGHT_FACTOR))
                self.wait(2)
                right_most_jpg = self.add_mu_items(
                    mu_paths, right_most_jpg[0][0], regex_pattern=mu_degrees_pattern, text="Membership Degrees"
                )
                # objects_to_be_shifted.append(right_most_jpg)
                self.play(self.camera.frame.animate.set(height=right_most_jpg.get_height() * INCREASE_HEIGHT_FACTOR))
                self.wait(2)
                right_most_jpg = self.add_mu_items(
                    mu_paths, right_most_jpg[0][0], regex_pattern=rule_exemplar_pattern, text="Fuzzy Logic Rules", idx_to_start_from=1
                )
                # objects_to_be_shifted.append(right_most_jpg)
                self.play(self.camera.frame.animate.set(height=right_most_jpg.get_height() * INCREASE_HEIGHT_FACTOR))
                self.wait(2)
                right_most_jpg = self.add_mu_items(
                    mu_paths, right_most_jpg[0][1], regex_pattern=rule_mu_pattern, text="Rule Applicability", idx_to_start_from=1
                )
                # objects_to_be_shifted.append(right_most_jpg)
                self.wait(2)

                # go back to the original image
                self.play(
                    self.camera.frame.animate.set(
                        height=right_most_jpg.get_height() * 0.5
                    ),  # still keep the current bird's eye view
                    self.camera.frame.animate.move_to(prev_group_jpg)
                )
                self.wait(1)

                # reset the camera frame to its original position if it was modified
                self.shift_objects(direction=RIGHT)  # send the objects out of view
                self.play(
                    Restore(self.camera.frame),
                )
                self.wait(1)

            i += 1
            if curr_time_step == END_IDX:
                break

    def shift_objects(self, direction):
        if len(self.objects_to_be_shifted) > 0:
            self.play(
                Group(*self.objects_to_be_shifted.values()).animate.shift(30 * direction),
                Restore(self.camera.frame),
            )
            self.wait(1)

    def add_mu_items(self, mu_paths, right_most_jpg, regex_pattern, text: str, idx_to_start_from: int = 0):
        centers = []
        def add_to_centers(start_idx, end_idx, append: bool):
            tmp_mu_paths = [
                mu_path for mu_path in mu_paths
                if regex_pattern.match(mu_path.stem)
            ]
            for mu_path in tmp_mu_paths[start_idx:end_idx]:
                if regex_pattern.match(mu_path.stem):
                    print(mu_path)
                    new_exemplar = ImageMobject(
                        mu_path
                    ).scale(0.5).next_to(right_most_jpg, RIGHT).shift(RIGHT)
                    if len(centers) > 0:
                        if append:
                            new_exemplar.next_to(centers[-1], DOWN)
                        else:
                            new_exemplar.next_to(centers[0], UP)
                    if append:
                        centers.append(new_exemplar)
                    else:  # insert at the beginning
                        centers.insert(0, new_exemplar)

        add_to_centers(idx_to_start_from, len(mu_paths), append=True)
        add_to_centers(0, idx_to_start_from, append=False)

        centers_group = Group(*centers)
        centers_text = Text(
            f"{text}", font_size=24, color=BLACK
        ).next_to(centers_group, DOWN)
        centers_group_with_text = Group(centers_group, centers_text)

        if text in self.objects_to_be_shifted:
            self.play(
                ReplacementTransform(
                    self.objects_to_be_shifted[text],
                    centers_group_with_text
                ),
                self.camera.frame.animate.move_to(centers_group)
            )
        else:
            self.play(
                FadeIn(centers_group_with_text, run_time=1),
                self.camera.frame.animate.move_to(centers_group)
            )
        self.objects_to_be_shifted[text] = centers_group_with_text
        return centers_group_with_text


if __name__ == "__main__":
    # Flowchart(Path("test_images/mu")).construct()
    Flowchart().construct()