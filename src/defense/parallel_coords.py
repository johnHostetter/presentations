from typing import Tuple
from collections import OrderedDict

import numpy as np
from manim import *
from manim_slides import Slide

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class ParallelCoords(Slide, MovingCameraScene):
    def __init__(self):
        super().__init__()
        # this is hardcoded for my setup and may need to be changed, but want to dynamically
        # fetch the images from another project
        self.pycharm_dir = (
            Path(__file__).resolve().parents[3]
        )  # 'home/username/PycharmProjects'
        self.pysoft_dir = self.pycharm_dir / "PySoft"
        # point to the VizDOOM directory
        self.output_dir = (
            self.pysoft_dir / "output" / "experiments" / "online-rl" / "vizdoom"
        )
        self.intermediate_dir = Path("custom") / "CO-FIS" / "DDQL" / "optuna"
        self.available_environments = list(self.output_dir.glob("*"))
        self.select_environments = [
            # "predict_position",
            "defend_the_center",
            # "health_gathering",
            # "take_cover",
        ]
        self.unfinished_environments = [
            "deathmatch",
            "deadly_corridor",
            "health_gathering_supreme",
        ]

        # keep a reference to the possible evaluators & their corresponding images when created
        self.possible_evaluators: OrderedDict[str, Any] = OrderedDict(
            (
                ("fanova", None),
                ("mean_decrease_impurity", None),
                ("ped_anova_0.1", None),
                # ("ped_anova_0.05", None),
            )
        )
        self.evaluators_display_names = {
            "fanova": "fANOVA",
            "mean_decrease_impurity": "Mean Decrease Impurity",
            "ped_anova_0.1": "PED-ANOVA (Top 10\%)",
            "ped_anova_0.05": "PED-ANOVA (Top 5\%)",
        }
        self.evaluators_results = {}

    def construct(self):
        self.camera.frame.save_state()
        prev_table: Union[None, Table] = None
        prev_evaluator_title: Union[None, Tex] = None
        prev_environment_title: Union[None, Tex] = None
        for environment_dir in self.available_environments:
            if environment_dir.is_file():
                continue

            environment_title = (
                Tex(" ".join(environment_dir.stem.split("_")).title(), color=BLACK)
                .scale(1.25)
                .set_z_index(100)
            )  # bring to front with a very high z-index

            # if environment_dir.stem not in self.select_environments:
            #     continue

            if environment_dir.stem in self.unfinished_environments:
                continue

            curr_dir = environment_dir / self.intermediate_dir
            for evaluator_idx, evaluator_name in enumerate(self.possible_evaluators):
                print(environment_dir)
                # begin preparing data collection for an overview table
                # where a table is created for each possible evaluator
                # and its rows are the environments & columns are the hyperparameters
                if evaluator_name not in self.evaluators_results:
                    self.evaluators_results[evaluator_name] = {
                        "environments": [],
                        "hyperparameters": [],
                        "param_values": [],
                        "results_columns": [],
                        "results_values": [],
                        "count": [],
                    }

                # create the evaluator image & its title
                evaluator_title = (
                    Tex(self.evaluators_display_names[evaluator_name], color=BLACK)
                    .scale(0.75)
                    .set_z_index(100)
                )  # bring to front with a very high z-index
                hyperparameter_importance_img_stem = (
                    f"{evaluator_name}_hyperparameter_importance"
                )
                parallel_coord_all_params_img_stem = (
                    f"parallel_coordinate_sorted_by_{evaluator_name}"
                )
                suffixes = ["_all_params", "_top_params"]
                hyperparameter_importance_img = ImageMobject(
                    str(curr_dir / f"{hyperparameter_importance_img_stem}.png")
                ).scale(1.5)
                evaluator_title.next_to(hyperparameter_importance_img, 0.1 * UP).shift(
                    0.5 * DOWN
                )

                # make parallel coordinate plot
                parallel_coord_all_params_img = ImageMobject(
                    str(
                        curr_dir
                        / f"{parallel_coord_all_params_img_stem}{suffixes[0]}.png"
                    )
                ).scale(1.5)
                img_group = (
                    Group(hyperparameter_importance_img, parallel_coord_all_params_img)
                    .arrange(buff=0.25)
                    .move_to(ORIGIN)
                )
                # shift the parallel coord image to the left to accommodate the image's margins
                parallel_coord_all_params_img.shift(LEFT)

                items_to_fade_in = []
                animations = []
                if prev_environment_title == None:
                    # set up the title and table
                    environment_title.next_to(evaluator_title, UP)
                    items_to_fade_in.append(environment_title)
                    items_to_fade_in.append(evaluator_title)
                else:
                    environment_title.move_to(prev_environment_title.get_center())
                    evaluator_title.move_to(prev_evaluator_title.get_center())
                    animations.extend(
                        [
                            ReplacementTransform(prev_evaluator_title, evaluator_title),
                            ReplacementTransform(
                                prev_environment_title, environment_title
                            ),
                        ]
                    )
                # only create & add the table once - this data does not change
                # get the table of data to show
                import pandas as pd

                # load and round the data to 2 decimal places
                df: pd.DataFrame = pd.read_csv(curr_dir / "all_trials_sorted.csv")
                # cols = [
                #     'Certainty', 'Constraint', "Cui, Y. et al. ('21)", 'Gumbel Noise',
                #     'Normalize', 'Use Entmax', 'Use GMT', 'Mean Reward', 'Std. Dev.', 'Slope'
                # ]
                # df = df[cols]
                pos_df = df
                # pos_df: pd.DataFrame = df[df["Slope"] > 0].head(TOP_K)

                # rearrange the columns to match the hyperparameter importance image & parallel coordinate plot
                hyperparameter_importance_df = pd.read_csv(
                    curr_dir / "hyperparameter_importance_ordering.csv"
                )
                hyperparameter_importance_df.set_index("Evaluator", inplace=True)
                top_params = []
                total_importance = 0
                IMPORTANCE_THRESHOLD = 0.90
                sorted_importance_results: List[Tuple[str, float]] = sorted(
                    list(hyperparameter_importance_df.loc[evaluator_name].items()),
                    key=lambda x: x[1],
                    reverse=True,
                )  # sort by importance (1th element)
                for param, importance in sorted_importance_results:
                    total_importance += importance
                    if (
                        round(total_importance, ndigits=2) <= IMPORTANCE_THRESHOLD
                    ):  # keep the top % of the importance
                        top_params.append(param)
                    else:
                        break
                # get the ordering for this particular evaluator
                hyperparameter_ordering_df = pd.read_csv(
                    curr_dir / "hyperparameter_index_ordering.csv"
                )
                hyperparameter_ordering_df.set_index("Evaluator", inplace=True)
                hyperparameter_ordering: List[str] = (
                    hyperparameter_ordering_df.loc[evaluator_name]
                    .sort_values()
                    .index.tolist()
                )  # sort the columns by their importance ordering
                hyperparameter_ordering = [
                    col for col in hyperparameter_ordering if col in pos_df
                ]  # only keep the columns that are in the dataframe
                target_columns = [
                    "Mean Reward",
                    "Std. Dev.",
                    # "Slope",
                    # "Count",
                ]
                new_pos_df = pos_df.copy()[
                    hyperparameter_ordering + target_columns
                ]  # rearrange the columns

                # simplify the data
                new_pos_df.loc[:, "Constraint"] = new_pos_df.loc[
                    :, "Constraint"
                ].astype(bool)
                # median-split floats
                for float_param in ["Learning Rate", "Epsilon", "Temperature", "Rules"]:
                    from decimal import Decimal

                    median_split: float = new_pos_df[float_param].median()
                    if float_param == "Learning Rate":
                        median_split_display: str = "{:.2e}".format(
                            Decimal(new_pos_df[float_param].median())
                        )
                    else:
                        median_split_display: str = str(
                            round(new_pos_df[float_param].median(), 2)
                        )
                    new_pos_df.loc[:, float_param] = (
                        new_pos_df.loc[:, float_param] <= median_split
                    ).map(
                        {
                            True: f"$\leq$ {median_split_display}",
                            False: f"$>$ {median_split_display}",
                        }
                    )
                # anything greater than 1
                for param in ["Gumbel Noise", "Neurogenesis"]:
                    # True if delayed, False if immediate
                    new_pos_df.loc[:, param] = new_pos_df.loc[:, param] > 1

                for param in ["Constraint", "Gumbel Noise", "Temperature"]:
                    # remove the value if it's not used because GMT is not used
                    new_pos_df.loc[new_pos_df["Use GMT"] == False, param] = "-"

                counts = new_pos_df[top_params].value_counts().values
                tmp_group_df = new_pos_df[top_params + target_columns].groupby(
                    top_params
                )
                agg_df = tmp_group_df.mean().reset_index()

                def pooled_variance(group) -> float:
                    n_samples = 25  # number of samples per group
                    sample_sizes: np.ndarray[int] = np.array([n_samples] * len(group))
                    return (
                        ((sample_sizes - 1) * (group["Std. Dev."] ** 2)).sum()
                        / (sample_sizes - 1).sum()
                    ) ** 0.5

                agg_df.loc[:, "Std. Dev."] = tmp_group_df.apply(
                    pooled_variance
                ).reset_index()[
                    0
                ]  # the result is stored in column 0

                # calculate the slope of the mean reward
                if "Slope" in target_columns:
                    agg_df.loc[:, "Slope"] = tmp_group_df.median().reset_index()[
                        "Slope"
                    ]

                agg_df.loc[:, "Count"] = counts
                agg_df = agg_df.sort_values("Mean Reward", ascending=False)

                # keep the best parameters
                self.evaluators_results[evaluator_name]["environments"].append(
                    environment_dir.stem
                )
                self.evaluators_results[evaluator_name]["hyperparameters"].append(
                    top_params
                )
                self.evaluators_results[evaluator_name]["param_values"].append(
                    agg_df.iloc[0, :][top_params].values.tolist()
                )
                self.evaluators_results[evaluator_name]["results_columns"].append(
                    target_columns
                )
                self.evaluators_results[evaluator_name]["results_values"].append(
                    agg_df.iloc[0, :][target_columns].values.tolist()
                )
                self.evaluators_results[evaluator_name]["count"].append(
                    agg_df.iloc[0, :]["Count"]
                )

                if environment_dir.stem in self.select_environments:
                    # focus on this particular environment to show the hyperparameter importance
                    # plot, the parallel coordinate plot and the best trial groups
                    table = self.make_table(img_group, agg_df)

                    # begin manipulating the table to make conclusions easier to draw
                    # row_mask = (agg_df["Slope"] < 0).values  # mask the rows where the slope is negative
                    # entry_animations = []
                    # for row_idx, row in enumerate(table.get_rows()[1:]):
                    #     if row_mask[row_idx]:
                    #         for entry in row:
                    #             entry_animations.append(entry.animate.set_color(WHITE))

                    # if len(entry_animations) > 0:
                    #     animations.append(AnimationGroup(*entry_animations))

                    # reorient the camera
                    camera_focus_group = Group(environment_title, img_group, table)
                    self.camera.frame.move_to(camera_focus_group.get_center())
                    self.camera.frame.set(
                        width=camera_focus_group.width + 0.2,
                        height=camera_focus_group.height + 0.2,
                    )
                    items_to_fade_in.append(img_group)
                    if prev_table is None:
                        items_to_fade_in.append(table)
                    else:
                        animations.append(ReplacementTransform(prev_table, table))

                    prev_table = table
                    animations.append(FadeIn(*items_to_fade_in))
                    animation_group: AnimationGroup = AnimationGroup(
                        *animations,
                    )

                    self.play(animation_group)
                    self.wait(1)
                    self.next_slide()

                    # replace the parallel coordinate plot with only the top parameters
                    parallel_coord_top_params_img = (
                        ImageMobject(
                            str(
                                curr_dir
                                / f"{parallel_coord_all_params_img_stem}{suffixes[1]}.png"
                            )
                        )
                        .scale(1.5)
                        .move_to(parallel_coord_all_params_img)
                    )
                    self.play(
                        ReplacementTransform(
                            parallel_coord_all_params_img, parallel_coord_top_params_img
                        )
                    )
                    self.wait(1)
                    self.next_slide()
                    prev_evaluator_title = evaluator_title
                    prev_environment_title = environment_title

        self.make_evaluator_table(img_group, evaluator_name=evaluator_name)

    def make_evaluator_table(self, img_group, evaluator_name: str):
        import pandas as pd

        def create_data(all_hyperparameters: OrderedDict = None) -> OrderedDict:
            if all_hyperparameters is None:
                all_hyperparameters = OrderedDict()

            environments = self.evaluators_results[evaluator_name]["environments"]
            for env_idx, environment in enumerate(environments):
                print(env_idx, environment)
                curr_hyperparameters = self.evaluators_results[evaluator_name][
                    "hyperparameters"
                ][env_idx]
                for param_idx, param in enumerate(curr_hyperparameters):
                    new_param_value: str = str(
                        self.evaluators_results[evaluator_name]["param_values"][
                            env_idx
                        ][param_idx]
                    )
                    if param not in all_hyperparameters:
                        all_hyperparameters[param] = ["n/a"] * len(environments)
                    if all_hyperparameters[param][env_idx] in ["-", "n/a"]:
                        all_hyperparameters[param][
                            env_idx
                        ] = new_param_value  # overwrite the value
                    elif new_param_value not in all_hyperparameters[param][env_idx]:
                        # not in is important as the concatenated string may already contain the value
                        # append the value to the existing string; this is contested
                        if new_param_value not in [
                            "-",
                            "n/a",
                        ]:  # only append if it's not a placeholder
                            all_hyperparameters[param][
                                env_idx
                            ] = f"{all_hyperparameters[param][env_idx]}, {new_param_value}"
            new_tasks: List[str] = [
                " ".join(env.split("_")).title()
                for env in self.evaluators_results[evaluator_name]["environments"]
            ]
            if "Task" in all_hyperparameters:
                curr_tasks = all_hyperparameters["Task"]
                assert curr_tasks == new_tasks, "Tasks are not the same"
                del all_hyperparameters[
                    "Task"
                ]  # delete it so we can add it to the right of the table
            # add the task to the right of the table
            all_hyperparameters["Task"] = new_tasks
            if "Trials" not in all_hyperparameters:
                all_hyperparameters["Trials"] = np.zeros(len(environments))
            all_hyperparameters["Trials"] += np.array(
                self.evaluators_results[evaluator_name]["count"], dtype=int
            )
            all_hyperparameters["Trials"] = all_hyperparameters["Trials"].tolist()
            return all_hyperparameters

        def inner_make_evaluator_table(
            evaluator_display_name: str, prev_table=None, all_hyperparameters=None
        ):
            if all_hyperparameters is None:
                # need to create the data for the first time
                all_hyperparameters = create_data(
                    all_hyperparameters=all_hyperparameters
                )

            tmp_df = pd.DataFrame(all_hyperparameters)
            table = self.make_table(
                img_group, tmp_df, top_k=7, shift_value=50, row_id=False
            )
            caption = (
                Tex(
                    f"Trials grouped by the most important hyperparameters for concurrent optimization, as determined by {evaluator_display_name}.",
                    color=BLACK,
                )
                .scale(0.75)
                .set_z_index(100)
            )
            caption.next_to(table, 0.5 * DOWN)
            captioned_table = Group(table, caption)
            if prev_table is None:
                self.play(FadeIn(captioned_table))
            else:
                self.play(
                    ReplacementTransform(prev_table, captioned_table),
                )
            self.play(
                self.camera.frame.animate.set(width=captioned_table.width + 0.2),
            )
            self.play(
                self.camera.frame.animate.move_to(captioned_table.get_center()),
            )
            return captioned_table

        table = None
        all_findings = OrderedDict()
        for (
            evaluator_name,
            evaluator_display_name,
        ) in self.evaluators_display_names.items():
            if evaluator_name in self.evaluators_results:
                table = inner_make_evaluator_table(
                    evaluator_display_name,
                    prev_table=table,
                )
                # keep track of the data for the final slide
                all_findings = create_data(all_hyperparameters=all_findings)
                self.wait(1)
                self.next_slide()

        columns_to_remove = [
            "Learning Rate",
            "Epsilon",
            "Temperature",
            "Rules",
            "Trials",
        ]  # remove these columns because they don't really help in the final slide
        for col in columns_to_remove:
            if col in all_findings.keys():
                del all_findings[col]
        inner_make_evaluator_table(
            evaluator_display_name="ALL",
            prev_table=table,
            all_hyperparameters=all_findings,
        )
        self.wait(1)
        self.next_slide()

    def make_table(
        self,
        img_group,
        pos_df,
        top_k: int = 7,
        shift_value: float = 0.5,
        row_id: bool = True,
    ) -> Table:
        new_columns = {
            "Use GMT": r"GMT",
            "Constraint": r"$\theta$",
            "Learning Rate": r"$\eta$",
            "Cui, Y. et al. ('21)": r"$w_{u}$",
            "Epsilon": r"$\epsilon$",
            "Temperature": r"$\tau$",
            "Normalize": r"LN",
            # "Use Entmax": r"$\overline{w}_{u}'$",
            "Use Entmax": r"1.5-\texttt{entmax}",
            "Gumbel Noise": r"$\mathbf{N}$",
            "Rules": "Rules",
            "Neurogenesis": r"$+\mu$",
            "Certainty": r"CFs",
            "Mean Reward": r"Mean",
            "Std. Dev.": r"$\sigma$",
            # "Slope": r"$m$",
            "Count": r"Trials",
        }
        # pos_df.rename(columns=new_columns, inplace=True)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        # if an error occurs here, it's likely due to the mathrsfs package not being installed
        # OR writing LaTeX throws ParseError: no element found: line 1, column 0
        # SOLUTION: delete the media/Tex and media/texts directories
        # REASON: the error is likely due to a corrupted file in the media directory
        # HOW IT HAPPENED: if this script is interrupted while running, it may corrupt the files
        DECIMAL_PLACES: int = 2
        tmp_df = pos_df.copy(deep=True)
        tmp_df.rename(columns=new_columns, inplace=True)
        tmp_df = tmp_df.round(DECIMAL_PLACES).head(top_k)
        tmp_df_cols = tmp_df.columns.tolist()
        if row_id:
            tmp_df["Row"] = range(1, top_k + 1)
            tmp_df = tmp_df[["Row"] + tmp_df_cols]
        elif "Task" in tmp_df_cols and "Trials" in tmp_df_cols:
            # arrange it so columns are to the left, then Trials, then Task
            tmp_df_cols = [col for col in tmp_df_cols if col not in ["Task", "Trials"]]
            tmp_df_cols += ["Trials", "Task"]
            # cast the columns to the right types
            tmp_df["Trials"] = tmp_df["Trials"].astype(int)
        table = Table(
            table=tmp_df.values.astype(str).tolist(),
            col_labels=[
                MathTex(column_name[1:-1]) if "$" in column_name else Tex(column_name)
                for column_name in tmp_df.columns
            ],
            element_to_mobject=lambda x: Tex(x),  # use LaTeX for the entries
            # element_to_mobject_config={
            #     "use_svg_cache": False,
            # }
        )
        # table_columns = table.get_columns()[-len(target_columns):]
        # for column in table_columns:
        #     column.set_color(GRAY)
        table.get_col_labels().set_weight("bold")
        table.get_horizontal_lines().set_color(BLACK)
        table.get_vertical_lines().set_color(BLACK)
        for entry in table.get_entries():
            entry.set_color(BLACK)
        table.scale(0.5).move_to(img_group.get_center()).next_to(
            img_group, shift_value * DOWN
        )
        return table


if __name__ == "__main__":
    ParallelCoords().render()
