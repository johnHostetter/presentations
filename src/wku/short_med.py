from dataclasses import dataclass
from typing import Tuple, Set, List as ListType, Union as UnionType, Dict as DictType

import torch
import igraph as ig
from manim import *
from manim_slides import Slide

from src.graph_example import NoCodeGraph
from soft.datasets import LabeledDataset
from soft.computing.organize import SelfOrganize
from soft.computing.blueprints.factory import SystematicDesignProcess
from soft.utilities.reproducibility import load_configuration

config.background_color = WHITE
light_theme_style = {
    "fill_color": BLACK,
    "background_stroke_color": WHITE,
}


# https://stackoverflow.com/questions/76175939/manim-add-labels-near-vertices
def get_self_organize(input_size: int = 4, output_size: int = 1) -> SelfOrganize:
    soft_config = load_configuration()
    with soft_config.unfreeze():
        soft_config.clustering.distance_threshold = 0.2
    return SystematicDesignProcess(
        algorithms=["clip", "ecm", "wang_mendel"], config=soft_config
    ).build(
        training_data=LabeledDataset(
            data=torch.rand((250, input_size)), labels=torch.rand((250, output_size))
        )
    )


@dataclass
class GraphPair:
    igraph: ig.Graph  # the igraph.Graph representation of the graph
    digraph: DiGraph  # the manim representation of the igraph.Graph

    def __len__(self) -> int:
        return len(self.igraph.vs)

    def __getitem__(self, item: UnionType[str, int]) -> Tuple[ig.Vertex, Dot]:
        index = item  # assume the given item is a vertex index
        if isinstance(item, str):
            # the given item is a vertex name, get its index
            index = self.igraph.vs.select(name_eq=item).indices[0]
        return self.igraph.vs[index], self.digraph.vertices[index]


class TransformGraphs(Slide, MovingCameraScene):
    def plot_graph(
        self, graph: ig.Graph, layer_types: ListType[str], direction
    ) -> GraphPair:
        if (direction == RIGHT).all():
            opposite_direction = LEFT
        else:
            opposite_direction = RIGHT

        digraph, grouped_vertices = NoCodeGraph.create_manim_digraph(graph, layer_types)
        digraph.shift(DOWN, opposite_direction)
        digraph.scale(1.35)
        digraph.rotate(PI / 2)

        self.add(digraph)

        # Save the state of camera
        self.camera.frame.save_state()

        self.play(
            Create(digraph),
            # self.camera.frame.animate.set_width(digraph.get_width() * 0.7),
            self.camera.frame.animate.move_to(digraph.get_center()),
            run_time=5,
        )
        self.wait()

        # display the individual layers

        self.play(digraph.animate.shift(direction * 3))

        layer_colors = [BLUE, GREEN, RED, YELLOW, PURPLE]
        animations = []
        rewind_animations = []
        for layer_order, (layer_type, layer_color) in enumerate(
            zip(layer_types, layer_colors)
        ):
            layer_vertices = [
                digraph.vertices[v] for v in grouped_vertices[layer_order]
            ]
            surrounding_rectangle = SurroundingRectangle(
                VGroup(*layer_vertices),
                color=layer_color,
                buff=0.25,
                corner_radius=0.25,
            )
            layer_str: str = layer_type.capitalize() + " Layer"
            layer_str += f" {layer_order}" if layer_type == "hidden" else ""
            layer_label = Text(layer_str, color=BLACK, font_size=24).next_to(
                surrounding_rectangle, opposite_direction
            )
            animation = AnimationGroup(
                *[
                    Create(surrounding_rectangle, run_time=2),
                    Write(layer_label, run_time=1),
                    AnimationGroup(
                        *[v.animate.set_color(layer_color) for v in layer_vertices],
                        run_time=0.5,
                    ),
                ],
            )
            rewind_animation = AnimationGroup(
                *[
                    FadeOut(surrounding_rectangle, run_time=2),
                    Unwrite(layer_label, run_time=1),
                    AnimationGroup(
                        *[v.animate.set_color(BLACK) for v in layer_vertices],
                        run_time=0.5,
                    ),
                ],
            )
            animations.append(animation)
            rewind_animations.append(rewind_animation)

        for animation in animations:
            self.play(animation)
            self.wait()

        self.wait(5)

        for rewind_animation in rewind_animations:
            self.play(rewind_animation)
            self.wait()

        return GraphPair(graph, digraph=digraph)

    @staticmethod
    def get_vertices_and_edges_for_flc(
        grouped_premise_indices, max_terms, old_vs=None
    ) -> Tuple[DictType[str, int], Set[Tuple[str, str]]]:
        """
        Create a set of vertices and edges for a graph of an example fuzzy logic controller.

        Returns:
            A tuple containing the vertices and edges of the graph.
        """
        # shuffle to illustrate the randomness of the network morphism
        import random
        values = list(grouped_premise_indices.values())
        random.shuffle(values)
        grouped_premise_indices = {idx: v for idx, v in enumerate(values)}

        vs, edges = NoCodeGraph.make_edges_and_vertices_for_flc(grouped_premise_indices, max_terms)

        # sort the vertices so they remain in the same order
        vs = dict(sorted(vs.items(), key=lambda item: int(item[0][1:])))

        if old_vs is not None:
            # use the old vertices to maintain the same order
            return old_vs, edges

        return vs, edges

    @staticmethod
    def make_premise_indices_for_flc(hidden_size, input_size, output_size):
        flc = NoCodeGraph.make_flc(hidden_size, input_size, output_size)
        grouped_premise_indices, max_terms = NoCodeGraph.get_premise_indices_from_flc(flc)
        return grouped_premise_indices, max_terms

    def construct(self):
        # iterate over creating each type of model and plotting its graph
        model_graphs = {}
        all_models: UnionType[None, Group] = None
        grouped_premise_indices, max_terms = TransformGraphs.make_premise_indices_for_flc(
            input_size=4, hidden_size=16, output_size=1
        )
        vs = None
        for model_type in ["flc0", "flc1", "flc2", "flc3", "flc4", "flc5", "flc6", "flc7", "flc8", "flc9"]:
            if model_type == "dnn":
                displayed_model_name = "Dense Feed-Forward Artificial Neural Network"
                vs, edges = NoCodeGraph.get_vertices_and_edges_for_dnn()
                layer_types = ["input", "hidden", "hidden", "hidden", "output"]
            elif "flc" in model_type:
                displayed_model_name = "Neuro-Fuzzy Network"
                vs, edges = TransformGraphs.get_vertices_and_edges_for_flc(
                    grouped_premise_indices, max_terms, old_vs=vs
                )
                layer_types = ["input", "premise", "rule", "consequence", "output"]
            else:
                raise ValueError(f"Unknown model type: {model_type}")

            # # display the model name
            # displayed_model_text: Text = Text(
            #     displayed_model_name, font_size=24, color=BLACK
            # )
            # self.play(
            #     self.camera.frame.animate.move_to(displayed_model_text.get_center()),
            #     Write(displayed_model_text),
            #     run_time=2,
            # )
            # self.wait(5)
            # self.play(Unwrite(displayed_model_text, run_time=2))
            #
            # # animate example code for the model
            # self.animate_code(model_type, input_size=4, hidden_size=16, output_size=1)

            # create the igraph.Graph representation of the model
            graph: ig.Graph = NoCodeGraph.create_igraph_digraph(edges, vs)

            # create the manim DiGraph representation of the model

            digraph, grouped_vertices = NoCodeGraph.create_manim_digraph(graph, layer_types)
            digraph.scale(1.35)
            digraph.rotate(PI / 2)
            self.camera.frame.move_to(digraph.get_center())
            model_graphs[model_type] = GraphPair(graph, digraph=digraph)
            # if model_type == "dnn":
            #     # move the DNN graph to the left and temporarily hide it
            #     self.play(
            #         # digraph.animate.to_edge(LEFT),
            #         FadeOut(graph_pair.digraph),
            #     )
            # elif model_type == "flc":
            #     # bring the DNN graph back for side-by-side comparison
            #     all_models: UnionType[None, Group] = Group(
            #         model_graphs["dnn"].digraph, model_graphs["flc"].digraph
            #     )
            #     self.play(
            #         # digraph.animate.to_edge(RIGHT),
            #         model_graphs["flc"].digraph.animate.next_to(
            #             model_graphs["dnn"].digraph, RIGHT, buff=3.0
            #         ),
            #         Create(model_graphs["dnn"].digraph),
            #     )
            #     self.play(all_models.animate.move_to(ORIGIN))
            #     self.play(
            #         self.camera.frame.animate.move_to(all_models.get_center()),
            #     )

        self.wait()
        self.next_slide(loop=True)
        prev_graph: UnionType[None, DiGraph] = None
        forward_arrow: UnionType[None, Arrow] = None
        backward_arrow: UnionType[None, Arrow] = None
        for model_type, graph_pair in model_graphs.items():
            if forward_arrow is None:
                forward_arrow = Arrow(DOWN, UP, color=BLUE).next_to(graph_pair.digraph, LEFT)
            if backward_arrow is None:
                backward_arrow = Arrow(UP, DOWN, color=RED).next_to(graph_pair.digraph, LEFT)
            if prev_graph is None:
                # make the arrows for the forward and backward passes
                self.play(Create(graph_pair.digraph))
            else:
                self.play(Unwrite(forward_arrow))
                del forward_arrow
                forward_arrow = Arrow(DOWN, UP, color=BLUE).next_to(graph_pair.digraph, LEFT)
                self.play(Write(backward_arrow))
                self.play(
                    AnimationGroup(
                        FadeOut(prev_graph),
                        Create(graph_pair.digraph),
                    ),
                    run_time=1,
                )
                self.play(Unwrite(backward_arrow))
                del backward_arrow
                backward_arrow = Arrow(UP, DOWN, color=RED).next_to(graph_pair.digraph, LEFT)
            self.play(Write(forward_arrow))
            prev_graph = graph_pair.digraph
        # self.wait(3)

        # if all_models is not None:  # both models exist
        #     # then show the comparison between the two models
        #     self.play(all_models.animate.move_to(ORIGIN))
        #     self.play(
        #         self.camera.frame.animate.move_to(all_models.get_center()),
        #     )
        #     self.wait(5)


if __name__ == "__main__":
    c = TransformGraphs()
    c.render()