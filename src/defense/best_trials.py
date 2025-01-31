import pandas as pd
from decimal import Decimal
from manim_slides import Slide
from manim import (
    config,
    BLACK,
    WHITE,
    ImageMobject,
    Table,
    MathTex,
    FadeIn,
    FadeOut,
    Tex,
    Group,
    DOWN,
    RED, Uncreate, Create, VGroup, TexTemplate, MovingCameraScene, GREEN, SurroundingRectangle,
    DARK_BLUE, MAROON, BLUE, PURPLE,
)

from src.manim_presentation.utils import get_project_root

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class BestTrials(Slide, MovingCameraScene):
    def __init__(self):
        super().__init__()
        self.table_ctr: int = 0

    def construct(self):
        # img = ImageMobject(
        #     get_project_root() / f"defense/images/{self.file_name}"
        # ).scale(1.5)

        all_groups = VGroup()
        for file_name, architecture in [("dnn_results", "DNNs"), ("nfn_results", "NFNs")]:
            all_groups.add(self.make_table(file_name, architecture))
        all_groups.arrange(DOWN)
        self.camera.frame.move_to(all_groups).set(
            height=all_groups.get_height() + 1, width=all_groups.get_width() + 1
        )
        self.wait(1)
        self.next_slide()
        self.play(Create(all_groups))
        self.wait(1)
        self.next_slide()
        self.play(Uncreate(all_groups))
        self.wait(1)

    def make_table(self, file_name, architecture):
        tmp_df = pd.read_csv(get_project_root() / f"defense/data/{file_name}.csv")
        tmp_df.loc[:, " $\eta$"] = tmp_df[" $\eta$"].apply(
            lambda x: "${:.2e}$".format(Decimal(x))
        )
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsmath}")  # for piecewise formula
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        myTemplate.add_to_preamble(r"\usepackage[cal=boondox]{mathalfa}")
        table = Table(
            table=tmp_df.values.astype(str).tolist(),
            col_labels=[
                Tex(column_name.strip(), tex_template=myTemplate)
                for column_name in tmp_df.columns
            ],
            element_to_mobject=lambda x: Tex(
                x.strip(), tex_template=myTemplate
            ),  # use LaTeX for the entries
            # element_to_mobject_config={
            #     "use_svg_cache": False,
            # }
        ).scale(0.5)
        table.get_col_labels().set_weight("bold")
        table.get_horizontal_lines().set_color(BLACK)
        table.get_vertical_lines().set_color(BLACK)
        if architecture == "NFNs":
            table.add(SurroundingRectangle(table.get_columns()[2], color=BLUE))  # premise aggregation
            table.add(SurroundingRectangle(table.get_columns()[4], color=GREEN))  # softmax
            table.add(SurroundingRectangle(table.get_columns()[7], color=MAROON))  # layer norm
        table.add(SurroundingRectangle(table.get_columns()[-3], color=PURPLE))  # mean results

        for entry in table.get_entries():
            entry.set_color(BLACK)
        caption = Tex(
            f"Table {self.table_ctr + 1}: Best hyperparameters identified for "
            f"{architecture} trained by Duel DDQL using TPE.",
            color=BLACK,
        ).scale(0.5)
        group = VGroup(table, caption).arrange(DOWN)
        self.table_ctr += 1
        return group


# class ResultsDNN(ResultsTmp):
#     def __init__(self):
#         super().__init__("dnn_results", architecture="DNNs")


# class ResultsNFN(ResultsTmp):
#     def __init__(self):
#         super().__init__("nfn_results", architecture="NFNs")


if __name__ == "__main__":
    BestTrials().render()
