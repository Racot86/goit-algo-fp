"""
Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код із завдання 4 для побудови бінарного дерева,
необхідно створити програму на Python, яка візуалізує обходи дерева:
у глибину та в ширину.
"""

import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_gradient_colors(n):
    colors = []
    for i in range(n):
        r = int(18 + (180 - 18) * (i / n))
        g = int(150 + (240 - 150) * (i / n))
        b = int(240 + (0 - 240) * (i / n))
        colors.append(f'#{r:02x}{g:02x}{b:02x}')
    return colors

def dfs(node, visited):
    if node is not None:
        visited.append(node)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def visualize_dfs(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    visited = dfs(tree_root, [])
    gradient_colors = generate_gradient_colors(len(visited))

    for i, node in enumerate(visited):
        node.color = gradient_colors[i]

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(title)
    plt.show()

# Example usage
root = Node("Root", color="lightcoral")
node1 = Node("Left", color="skyblue")
node2 = Node("Right", color="skyblue")
node3 = Node("Left.Left", color="lightgreen")
node4 = Node("Left.Right", color="lightgreen")
node5 = Node("Right.Left", color="lightyellow")
node6 = Node("Right.Right", color="lightyellow")

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6

# Visualize DFS
visualize_dfs(root, 'DFS Search Path')

