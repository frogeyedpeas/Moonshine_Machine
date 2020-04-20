import pydot

graph = pydot.Dot(graph_type='digraph')

node_a = pydot.Node("Node A")

node_b = pydot.Node("Node B")

graph.add_node(node_a)

graph.add_node(node_b)

graph.add_edge(pydot.Edge(node_a, node_b))

graph.write_png('example2_graph.png')

graph.write_svg('graph.svg')
