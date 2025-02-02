from manim import *
from manim_slides import Slide
from manim_timeline.quotes import quotable_person

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class Godel(Slide):
    # Godel actually worked on multivalued logic, called Gödel-Dummett logic
    # https://link.springer.com/article/10.1023/A:1022997524909
    def construct(self):
        paragraph, source_text, person, signature_group = self.draw(
            self, origin=ORIGIN, scale=1.0
        )
        self.wait(1)
        self.next_slide()
        self.play(
            FadeOut(
                Group(VGroup(paragraph, source_text, person), signature_group),
                run_time=2,
            )
        )
        self.wait(1)
        self.next_slide()

    @staticmethod
    def draw(scene, origin, scale, animate: bool = True):
        signature = SVGMobject(
            get_project_root() / "assets" / "signatures" / "Kurt_Gödel_signature.svg",
            # color=WHITE
        ).scale(1.0)
        person_svg = SVGMobject(
            get_project_root()
            / "assets"
            / "people"
            / "Young_Kurt_Gödel_as_a_student_in_1925.svg"
            # / "kurt_godel.svg",
            # color=BLACK,
            # fill_color=WHITE,
            # stroke_color=BLACK
        ).scale(2.0)
        paragraph, source_text, person, signature_group = quotable_person(
            scene,
            person_svg=person_svg,
            quote=(
                '"The more I think about language,\nthe more it amazes me that people\never understand each other at all."'
                # '"So far as the laws of mathematics refer to reality,\nthey are not certain. '
                # 'And so far as they are certain, \nthey do not refer to reality."'
            ),
            # http://kevincarmody.com/math/goedel.html
            source="(Reflections on Kurt Gödel, MIT Press, 1987, pg. 95)",
            signature=signature,
            origin=origin,
            scale=scale,
            left_shift=1.25,
            animate=animate,
        )
        return paragraph, source_text, person, signature_group


if __name__ == "__main__":
    c = Godel()
    c.render()
