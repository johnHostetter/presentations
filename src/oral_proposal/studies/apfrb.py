import igraph as ig
from manim import *
from manim_slides import Slide

from manim_timeline.graph import GraphPair
from manim_beamer.slides import SlideShow, SlideWithList
from manim_beamer.bibtex import BibTexManager
from manim_beamer.lists import ItemizedList, BulletedList as BL
from src.defense.publications import Publications
from src.manim_presentation.utils import get_project_root
from src.graph_example import NoCodeGraph as MyGraph
from src.oral_proposal.studies.pyrenees import (
    IntelligentTutoringSystemResults,
)

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


class APFRB(SlideShow):
    def __init__(self, **kwargs):
        super().__init__(
            slides=[APFRBDiagram(), APFRBResults(), apfrb_summary()], **kwargs
        )


class APFRBResults(IntelligentTutoringSystemResults):
    def __init__(self):
        data: List[List[str]] = [
            [
                "FLC (N = 50)",
                ".748 (.159)",
                ".784 (.153)",
                "-0.02 (0.79)",
                "1.65 (0.45)",
            ],
            [
                "Student Choice (N = 54)",
                ".746 (.158)",
                ".643 (.184)",
                "-0.84 (1.31)",
                "1.54 (0.68)",
            ],
            [
                "Expert (N = 66)",
                ".729 (.166)",
                ".702 (.182)",
                "-0.48 (1.75)",
                "1.60 (0.52)",
            ],
        ]
        super().__init__(data, highlighted_columns=[2, 3])


def apfrb_summary() -> SlideWithList:
    """
    Create a slide with my proposed studies for the completion of my dissertation.

    Returns:
        The slide with a list of studies.
    """
    bibtex_manager = BibTexManager(
        path=get_project_root() / "oral_proposal" / "ref.bib"
    )
    beamer_list = BL(
        items=[
            bibtex_manager.cite_entry(
                bibtex_manager["hostetter2023leveraging"], num_of_words=8
            ),
            "Primary Intuition",
            ItemizedList(
                items=[
                    "APFRB offers a mathematical equivalence between DNNs and FLCs",
                    "Train the more complex DNN, then convert to FLC for inference",
                ]
            ),
            "Summary",
            ItemizedList(
                items=[
                    "The FLC significantly helped students learn probability",
                ]
            ),
            "Contributions",
            ItemizedList(
                items=[
                    "First pedagogical policy using FLCs to teach students",
                ]
            ),
            "Limitations",
            ItemizedList(
                items=[
                    "Works only for some DNNs (e.g., hyperbolic tangent required)",
                    "Number of rules grows exponentially with the number of neurons in the DNN",
                    "The rules are not interpretable by humans",
                ]
            ),
        ]
    )
    return SlideWithList(
        title="Leveraging All-Permutations Fuzzy Rule Base (APFRB)",
        subtitle="Exploring the Potential of Fuzzy Logic in Real-World Applications",
        beamer_list=beamer_list,
    )


class APFRBDiagram(Slide, MovingCameraScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.graphs = {}
        self.bib = BibTexManager(path=get_project_root() / "oral_proposal" / "ref.bib")

    def construct(self):
        self.draw(origin=ORIGIN, scale=1.0, target_scene=self, animate=True)

    def draw(self, origin=ORIGIN, scale=1.0, target_scene=None, animate=True) -> VGroup:
        if target_scene is None:
            target_scene = self
        # note to self I copied this code directly from MyGraph and only kept the relevant parts
        for model_type in ["dnn", "flc"]:
            if model_type == "dnn":
                displayed_model_name = "Deep Neural Network"
                vs, edges = MyGraph.get_vertices_and_edges_for_dnn()
                layer_types = ["input", "hidden", "hidden", "hidden", "output"]
            elif model_type == "flc":
                displayed_model_name = "Neuro-Fuzzy Network"
                vs, edges = MyGraph.get_vertices_and_edges_for_flc()
                layer_types = ["input", "premise", "rule", "consequence", "output"]
            else:
                raise ValueError(f"Unknown model type: {model_type}")

            # create the igraph.Graph representation of the model
            graph: ig.Graph = MyGraph.create_igraph_digraph(edges, vs)

            digraph, grouped_vertices = MyGraph.create_manim_digraph(graph, layer_types)
            digraph.rotate(PI / 2)
            self.graphs[displayed_model_name] = GraphPair(igraph=graph, digraph=digraph)

        # code specific to APFRB diagram

        # v_group = VGroup(*[value.digraph for value in self.graphs.values()])
        v_group: VGroup = VGroup()
        for key, value in self.graphs.items():
            new_item = VGroup(
                Tex(key, font_size=18, color=BLACK)
                .scale(scale_factor=scale)
                .next_to(value.digraph, UP),
                value.digraph,
            )
            if len(v_group) != 0:
                arrow = Arrow(
                    LEFT,
                    RIGHT,
                    color=BLACK,
                    stroke_width=6 * scale,
                    max_stroke_width_to_length_ratio=0.5,
                ).scale(2.5 * scale)

                v_group.add(arrow.next_to(v_group[-1], RIGHT))
                v_group.add(
                    Tex(r"Distill \& APFRB", font_size=18, color=BLACK)
                    .scale(scale_factor=scale)
                    .next_to(arrow, UP)
                )
                new_item.next_to(arrow, RIGHT)
            v_group.add(new_item)

        v_group.scale(scale_factor=scale).move_to(origin)

        # set title to the top of the screen
        title = (
            Tex("All-Permutations Fuzzy Rule Base (APFRB)", font_size=24, color=BLACK)
            .scale(1.5)
            .next_to(v_group, UP, buff=1.0)
        )
        # add the citation
        citation_vgroup: VGroup = (
            Publications.convert_entry_to_long_pub(
                self.bib, self.bib["hostetter2023leveraging"]
            )
            .scale(0.5)
            .next_to(v_group, DOWN, buff=1.0)
        )
        v_group.add(title, citation_vgroup)

        if animate:
            target_scene.camera.frame.move_to(v_group.get_center()).set(
                width=v_group.width * 1.5
            )
            target_scene.next_slide()
            target_scene.play(Create(v_group), run_time=3)
            target_scene.wait(1)
            target_scene.next_slide()
        else:
            target_scene.add(v_group)

        return v_group


if __name__ == "__main__":
    APFRBDiagram().render()
