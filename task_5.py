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
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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


def draw_tree(tree_root, title):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.text(pos[tree_root.id][0] - 0.8, pos[tree_root.id][1], "{}".format(title))
    plt.show()


def lighten_color(color, amount=0.5):

    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])


def bfs(node):
    visited = []
    queue = [node]
    while queue:
        current = queue.pop(0)
        if current:
            visited.append(current)
            queue.append(current.left)
            queue.append(current.right)
    return visited

def dfs(node, visited):
    if node is not None:
        visited.append(node)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited


def draw_search(root, func, title):
    test = func
    color = 1
    for node in test:
        node.color = lighten_color(node.color, color)
        color -= 1/len(test)
    draw_tree(root,title)


# Створення дерева
root = Node(0,color="blue")
root.left = Node(4,color="blue")
root.left.left = Node(5,color="blue")
root.left.right = Node(10,color="blue")
root.right = Node(1,color="blue")
root.right.left = Node(3,color="blue")
root.right.right = Node(10,color="blue")


draw_search(root, bfs(root),"BFS Search path")
draw_search(root, dfs(root,[]),"DFS Search path")

