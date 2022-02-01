import ast

import astunparse
import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

node_names = {}
node_num = 0
node_color1 = []


def get_name_of_node(node):
    if isinstance(node, ast.Module):
        return "Module", 'rosybrown'
    elif isinstance(node, ast.If):
        return "if", 'lightskyblue'
    elif isinstance(node, ast.Compare):
        return astunparse.unparse(node), 'pink'
    elif isinstance(node, ast.For):
        return "for", 'thistle'
    elif isinstance(node, ast.LtE):
        return "<=", 'paleturquoise'
    elif isinstance(node, ast.arguments):
        return astunparse.unparse(node), 'khaki'
    elif isinstance(node, ast.FunctionDef):
        return node.name, 'lightcoral'
    elif isinstance(node, ast.Constant):
        return astunparse.unparse(node), 'tan'
    elif isinstance(node, ast.Name):
        return astunparse.unparse(node), 'mediumturquoise'
    elif isinstance(node, ast.BinOp):
        return astunparse.unparse(node), 'plum'
    elif isinstance(node, ast.Expr):
        return str(node.__class__.__name__), 'moccasin'
    elif isinstance(node, ast.Assign):
        return str(node.__class__.__name__), 'silver'
    elif isinstance(node, ast.Load):
        return str(node.__class__.__name__), 'mediumseagreen'
    elif isinstance(node, ast.Store):
        return str(node.__class__.__name__), 'lavender'
    elif isinstance(node, ast.Call):
        return str(node.__class__.__name__), 'cadetblue'
    elif isinstance(node, ast.Attribute):
        return str(node.__class__.__name__), 'violet'
    elif isinstance(node, ast.Tuple):
        return str(node.__class__.__name__), 'darksalmon'
    elif isinstance(node, ast.Raise):
        return str(node.__class__.__name__), 'indianred'
    elif isinstance(node, ast.List):
        return str(node.__class__.__name__), 'lemonchiffon'
    elif isinstance(node, ast.Return):
        return "return", 'beige'
    elif isinstance(node, ast.arg):
        return "Arg", 'darkkhaki'
    elif isinstance(node, ast.Add):
        return "+", 'mistyrose'
    else:
        return str(node.__class__.__name__), 'yellow'


def tree_iterate(node, parent_num, g, depth=0):
    global node_num, node_names
    node_num += 1

    g.add_node(node_num)
    if parent_num != 0:
        g.add_edge(parent_num, node_num)

    node_names[node_num], x = get_name_of_node(node)
    node_color1.append(x)
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

    plt.gcf().set_size_inches(40, 40)
    pos = graphviz_layout(g, prog="dot")
    nx.draw(g, pos=pos, with_labels=True, node_color=node_color1, labels=node_names, node_size=6000, node_shape='s')
    plt.savefig('artifacts/hard.png', bbox_inches='tight')
