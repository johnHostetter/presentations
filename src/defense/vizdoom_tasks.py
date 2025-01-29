from manim import config, Tex, ImageMobject, BLACK, WHITE, UP, SurroundingRectangle
from manim_slides import Slide

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class VideoInSlide(Slide):
    def __init__(self, task: str):
        super().__init__()
        self.task = task

    def construct(self):
        # Add a title
        title_str: str = " ".join(self.task.title().split("_"))
        title = Tex(title_str, color=BLACK).to_edge(UP)
        self.add(title)

        import cv2

        self.wait(1)
        self.next_slide(loop=True)
        video_dir = get_project_root() / "assets" / "videos" / self.task
        for video_file_path in video_dir.rglob("*.mp4"):
            # total_reward_int: int = int(video_file_path.stem.split("_")[-1])
            print(video_file_path)
            cap = cv2.VideoCapture(str(video_file_path))
            flag = True
            idx = 0
            while idx < 600 and flag:
                flag, frame = cap.read()
                if flag:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame_img = ImageMobject(frame).scale(1.5)
                    items_to_add = [frame_img]
                    if idx == 0:
                        frame_border = SurroundingRectangle(
                            frame_img, color=BLACK, fill_opacity=1
                        ).set_z_index(-1)
                        items_to_add.append(frame_border)
                    self.add(*items_to_add)
                    self.wait(
                        1 / 20
                    )  # 30 fps is not possible since Decoding Timestamp (DTS) values may overlap causing them to be non-monotonic
                    self.remove(frame_img)
                idx += 1
            cap.release()

        self.wait(1)
        self.next_slide()


class BP(VideoInSlide):
    def __init__(self):
        super().__init__(task="basic")


class BR(VideoInSlide):
    def __init__(self):
        super().__init__(task="rocket_basic")


class DTC(VideoInSlide):
    def __init__(self):
        super().__init__(task="defend_the_center")


class HTL(VideoInSlide):
    def __init__(self):
        super().__init__(task="defend_the_line")


class HG(VideoInSlide):
    def __init__(self):
        super().__init__(task="health_gathering")


class PP(VideoInSlide):
    def __init__(self):
        super().__init__(task="predict_position")


class TC(VideoInSlide):
    def __init__(self):
        super().__init__(task="take_cover")


if __name__ == "__main__":
    for cls in [BP, BR, DTC, HTL, HG, PP, TC]:
        cls().render()
