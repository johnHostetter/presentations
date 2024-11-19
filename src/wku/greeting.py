from manim import *
from manim_slides import Slide

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class Greeting(Slide):
    def construct(self):
        standby_text = [
            Text(
                "Neuro-Fuzzy Networks",
                font="TeX Gyre Termes",
                color=BLACK,
            ),
            Text(
                "Transparent Rule-Based Decision-Making",
                font="TeX Gyre Termes",
                color=BLACK,
            ),
            Text("© 2024 John Wesley Hostetter", font="TeX Gyre Termes", color=BLACK),
            # Text(
            #     "Presented by John Wesley Hostetter",
            #     font="TeX Gyre Termes",
            #     color=BLACK,
            # ),
            Text(
                "The presentation will begin shortly.",
                font="TeX Gyre Termes",
                color=BLACK,
            ),
        ]
        indications = [
            Circumscribe,  # (title, color=BLACK),
            ShowPassingFlash,  # (Underline(title)),
            Circumscribe,  # (title, color=BLACK),
            ShowPassingFlash,  # (Underline(title)),
            # Circumscribe,  # (title, color=BLACK),
        ]
        self.play(Write(standby_text[0]))
        # self.wait(10)
        self.next_slide(loop=True)
        last_idx: int = -1
        for idx, (message, indication) in enumerate(zip(standby_text, indications)):
            self.add(message)
            if indication is Circumscribe:
                self.play(indication(message, color=BLACK))
            elif indication is ShowPassingFlash:
                self.play(indication(Underline(message, color=BLACK)))
            else:
                self.play(indication(message))
            self.wait(3)
            last_idx = (idx + 1) % len(standby_text)
            self.play(
                AnimationGroup(
                    FadeOut(message, shift=UP * 1.5),
                    FadeIn(standby_text[last_idx], shift=UP * 1.5),
                )
            )
        self.wait(1)
        self.next_slide()
        self.play(FadeOut(standby_text[last_idx]))


if __name__ == "__main__":
    c = Greeting()
    c.render()
