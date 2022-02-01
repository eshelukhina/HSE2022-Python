import ast

import astunparse
import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

node_names = {}
node_num = 0


def get_name_of_node(node):
    if isinstance(node, ast.Constant) or isinstance(node, ast.Name):
        return astunparse.unparse(node)
    elif isinstance(node, ast.BinOp):
        return node.op.__class__.__name__
    else:
        return str(node.__class__.__name__)


def tree_iterate(node, parent_num, g, depth=0):
    global node_num, node_names
    node_num += 1

    g.add_node(node_num)
    if parent_num != 0:
        g.add_edge(parent_num, node_num)

    node_names[node_num] = get_name_of_node(node)
    if node is ast.Name:
        return
    else:
        parent = node_num
        for child in ast.iter_child_nodes(node):
            tree_iterate(child, parent, g, depth + 1)


if __name__ == '__main__':
    text_file = open("easy.py", "r")
    fibonacci_func = text_file.read()
    text_file.close()

    g = nx.DiGraph()
    tree_iterate(ast.parse(fibonacci_func), 0, g)

    plt.gcf().set_size_inches(35, 15)
    pos = graphviz_layout(g, prog="dot")
    nx.draw_networkx(g, pos=pos, with_labels=True, labels=node_names, node_shape="", node_size=1000)
    plt.savefig('artifacts/medium.png', bbox_inches='tight')
