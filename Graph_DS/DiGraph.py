from JSONEncoder import CustomEncoder
from Edge import Edge
from Node import Node
from typing import Any, Dict, Tuple, Union
from GraphInterface import GraphInterface
import json
from itertools import chain


class DiGraph(GraphInterface):
    def __init__(self) -> None:
        self.__nodesCount = 0
        self.__edgesCount = 0
        self.__nodes = dict()
        self.__edges = dict()
        self.__in_edges = dict()
        self.__version = 0

    def v_size(self) -> int:
        return self.__nodesCount

    def e_size(self) -> int:
        return self.__edgesCount

    def get_all_v(self) -> dict:
        return self.__nodes

    def all_in_edges_of_node(self, id1: int) -> Union[dict, None]:
        assert(isinstance(id1, int))
        return self.__in_edges.get(id1, None)

    def all_out_edges_of_node(self, id1: int) -> Union[dict, None]:
        assert(isinstance(id1, int))
        return self.__edges.get(id1, None)

    def get_mc(self) -> int:
        return self.__version

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        try:
            edge = Edge(id1, id2, weight)

            out_edge = self.__edges.get(id1, None)
            if out_edge is None:
                self.__edges[id1] = [edge]
            else:
                out_edge.append(edge)

            in_edge = self.__in_edges.get(id2, None)
            if in_edge is None:
                self.__in_edges[id2] = [edge]
            else:
                in_edge.append(edge)

            self.__version += 1
            return True
        except:
            return False

    def add_node(self, node_id: int, pos: Union[Tuple[float, float, float], str, None] = None) -> bool:
        try:
            self.__nodes[node_id] = Node(node_id, pos)
            self.__version += 1
            return True
        except:
            return False

    def remove_node(self, node_id: int) -> bool:
        if (self.__nodes.pop(node_id, None) is None) or \
                (self.__edges.pop(node_id, None) is None) or \
                (self.__in_edges.pop(node_id, None) is None):
            return False

        self.__version += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (self.__edges.pop(node_id1, None) is None) or \
                (self.__in_edges.pop(node_id2, None) is None):
            return False

        self.__version += 1
        return True

    @property
    def v(self):
        return self.__nodesCount

    @property
    def e(self):
        return self.__edgesCount

    @property
    def nodes(self):
        return self.__nodes

    @property
    def edges(self):
        return chain(*self.__edges.values())

    @property
    def in_edges(self):
        return self.__in_edges

    def __eq__(self, o: object) -> bool:
        if o is DiGraph and \
                self.__version == o.__version and \
                self.__nodes == o.__nodes and \
                self.__edges == o.__edges and \
                self.__in_edges == o.__in_edges:
            return True
        return False

    def dict(self) -> Dict[str, Any]:
        return {
            "Edges": list(self.edges),
            "Nodes": list(self.__nodes.values()),
        }

    def __str__(self) -> str:
        return json.dumps(self.dict(), cls=CustomEncoder)

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def toPosition(pos: str) -> Tuple[float, float, float]:
        return tuple([float(point) for point in pos.split(',')])
