from typing import Union
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json
from matplotlib import pyplot as plt
# For Shortest Path Algo
from collections import deque as stack
# For Priority Queue
import heapq as heap
# Only for integers or
# tuples having the 0-index as priority
# or classes which have __lt__(less-than) operator defined,
# for custom data need to make a custom heap class


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: Union[GraphInterface, None] = None) -> None:
        if graph is None:
            self.__graph = DiGraph()
        else:
            self.__graph = graph

    def get_graph(self) -> GraphInterface:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            graph_data = json.load(open(file_name))
            for node in graph_data["Nodes"]:
                self.__graph.add_node(node["id"], node["pos"])
            for edge in graph_data["Edges"]:
                self.__graph.add_edge(edge["src"], edge["dest"], edge["w"])
            return True
        except:
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'w') as f:
                f.write(str(self.graph))
            return True
        except:
            return False

    def plot_graph(self) -> None:
        plt.figure()
        ax = plt.axes(projection="3d")
        for src_node in self.graph.nodes.values():
            x, y, z = src_node.pos
            edges = self.graph.all_out_edges_of_node(src_node.id)
            ax.scatter3D(x, y, z, c=z, cmap='hsv')
            if edges is not None:
                for edge in edges:
                    x1, y1, z1 = self.graph.nodes[edge.dest].pos
                    ax.plot3D([x, x1], [y, y1], [z, z1], 'gray')
        plt.show()

    @property
    def graph(self):
        return self.__graph
