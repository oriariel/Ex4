import math
import unittest

from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


class GraphAlgoTest(unittest.TestCase):

    def setUp(self) -> None:
        graph = DiGraph()
        for n in range(10):
            graph.add_node(n)
        graph.add_edge(0, 1, 2.2)
        graph.add_edge(0, 4, 1)
        graph.add_edge(0, 6, 7.5)
        graph.add_edge(1, 3, 5.9)
        graph.add_edge(2, 3, 5.4)
        graph.add_edge(3, 5, 11.1)
        graph.add_edge(5, 9, 10)
        graph.add_edge(6, 3, 4.3)
        graph.add_edge(8, 7, 5.8)
        self.graph_algo = GraphAlgo(graph)

    def test_get_graph(self):
        graph = DiGraph()
        graph.add_node(0)
        graph_one_node = GraphAlgo(graph)
        self.assertNotEqual(graph_one_node.get_graph(), self.graph_algo.get_graph(), "graph with one node to setUp")

        graph_equal = GraphAlgo()
        for n in range(10):
            graph_equal.graph.add_node(n)
        graph_equal.graph.add_edge(0, 1, 2.2)
        graph_equal.graph.add_edge(0, 4, 1)
        graph_equal.graph.add_edge(0, 6, 7.5)
        graph_equal.graph.add_edge(1, 3, 5.9)
        graph_equal.graph.add_edge(2, 3, 5.4)
        graph_equal.graph.add_edge(3, 5, 11.1)
        graph_equal.graph.add_edge(5, 9, 10)
        graph_equal.graph.add_edge(6, 3, 4.3)
        graph_equal.graph.add_edge(8, 7, 5.8)
        graph_algo1 = GraphAlgo(graph_equal.graph)
        self.assertEqual(self.graph_algo.get_graph(), graph_algo1.get_graph(), "compare graph same the setUp graph")
        graph_equal.graph.remove_node(0)
        self.assertNotEqual(self.graph_algo.get_graph(), graph_algo1.get_graph(), "after remove 1 node")

    def test_load_save_json(self):
        file_path = 'unittest.json'
        self.assertTrue(self.graph_algo.save_to_json(file_path), "save setUp graph")
        file_path = '../data/A0'
        graph_from_json1 = GraphAlgo()
        self.assertFalse(graph_from_json1.load_from_json('test.json'), 'file not exist')
        self.assertTrue(graph_from_json1.load_from_json(file_path), "load A0 graph")
        self.assertEqual(graph_from_json1.get_graph().v_size(), 11, "node size A0 graph")
        self.assertEqual(graph_from_json1.get_graph().e_size(), 22, "edge size A0 graph")

    def test_shortest_path(self):
        self.assertTupleEqual(self.graph_algo.shortest_path(0, 10), (math.inf, []), "10 is not in graph")
        self.assertTupleEqual(self.graph_algo.shortest_path(12, 0), (math.inf, []), "12 is not in graph")
        self.assertTupleEqual(self.graph_algo.shortest_path(15, 15), (math.inf, []), "15 is not in graph")
        self.assertTupleEqual(self.graph_algo.shortest_path(0, 7), (math.inf, []), "dont have path")
        self.assertTupleEqual(self.graph_algo.shortest_path(2, 2), (math.inf, []), "node to himself")
        self.assertTupleEqual(self.graph_algo.shortest_path(0, 1), (2.2, [0, 1]), "basic path")
        self.graph_algo.graph.remove_edge(0, 1)
        self.assertTupleEqual(self.graph_algo.shortest_path(0, 1), (math.inf, []), "after remove edge")
        self.graph_algo.graph.add_edge(0, 1, 12)
        self.assertTupleEqual(self.graph_algo.shortest_path(0, 3), (11.8, [0, 6, 3]))
        self.assertTupleEqual(self.graph_algo.shortest_path(0, 9), (32.9, [0, 6, 3, 5, 9]), "from start to end")

    def test_connected_component(self):
        self.assertListEqual(self.graph_algo.connected_component(10), [], "not in graph")
        self.graph_algo.graph.remove_edge(2, 3)
        self.assertListEqual(self.graph_algo.connected_component(2), [2], "only node no edges")
        self.assertListEqual(self.graph_algo.connected_component(8), [8], "one edge out")
        self.assertListEqual(self.graph_algo.connected_component(7), [7], "one edge in")
        self.graph_algo.graph.add_edge(7, 8, 7.6)
        self.assertListEqual(self.graph_algo.connected_component(8), [7, 8], "two edges out,in")
        self.assertListEqual(self.graph_algo.connected_component(7), [7, 8], "two edges out,in")
        self.assertListEqual(self.graph_algo.connected_component(3), [3], "no scc")
        self.graph_algo.graph.add_edge(9, 3, 1.5)
        self.assertListEqual(self.graph_algo.connected_component(3), [3, 5, 9], "after add edge(9,3)")
        self.assertListEqual(self.graph_algo.connected_component(0), [0], "have neighbours but no scc")
        """0-->1-->3,0-->6-->3,3-->5-->9"""
        self.graph_algo.graph.add_edge(3, 0, 6.9)
        self.assertListEqual(self.graph_algo.connected_component(0), [0, 1, 3, 5, 6, 9])
        self.graph_algo.graph.remove_edge(9, 3)
        self.assertListEqual(self.graph_algo.connected_component(0), [0, 1, 3, 6], "remove edge(9,3) one scc down")

    def test_connected_components(self):
        graph = DiGraph()
        graph_algo = GraphAlgo(graph)
        self.assertListEqual(graph_algo.connected_components(), [], "new graph without nodes")
        graph_algo.graph.add_node(0)
        self.assertListEqual(graph_algo.connected_components(), [[0]], "graph with one node")
        graph_algo.graph.add_node(1)
        self.assertListEqual(graph_algo.connected_components(), [[0], [1]], "graph with two node")
        graph_algo.graph.add_edge(0, 1, 3)
        self.assertListEqual(graph_algo.connected_components(), [[0], [1]], "graph with two node one edge")
        graph_algo.graph.add_edge(1, 0, 2)
        self.assertListEqual(graph_algo.connected_components(), [[0, 1]], "graph with two node and connected edge")
        self.assertListEqual(self.graph_algo.connected_components(), [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]])
        self.graph_algo.graph.add_edge(3, 0, 4)
        self.assertListEqual(self.graph_algo.connected_components(), [[0, 1, 3, 6], [2], [4], [5], [7], [8], [9]])
        self.graph_algo.graph.add_edge(7, 8, 2.2)
        self.assertListEqual(self.graph_algo.connected_components(), [[0, 1, 3, 6], [2], [4], [5], [7, 8], [9]])
