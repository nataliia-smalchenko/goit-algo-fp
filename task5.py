import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import uuid

class Node:
    """Клас для вузлів дерева"""
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def get_color(index, total, start_color='#6b04d1', end_color='#e5cffa'):
    """Функція для отримання кольору на основі порядкового номера"""
    start_rgb = [int(start_color[i:i+2], 16) for i in (1, 3, 5)]
    end_rgb = [int(end_color[i:i+2], 16) for i in (1, 3, 5)]
    color_rgb = [(start_rgb[i] + (end_rgb[i] - start_rgb[i]) * index // total) for i in range(3)]
    return '#{:02X}{:02X}{:02X}'.format(*color_rgb)


def build_tree():
    """Функція для побудови дерева"""
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.left = Node('F')
    root.right.right = Node('G')
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Функція для додавання ребер до графу"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def dfs_traversal(root):
    """Обхід у глибину (DFS) з використанням стека"""
    if not root:
        return []

    stack = [root]
    visited_nodes = []
    while stack:
        node = stack.pop()
        visited_nodes.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return visited_nodes


def bfs_traversal(root):
    """Обхід у ширину (BFS) з використанням черги"""
    if not root:
        return []

    queue = deque([root])
    visited_nodes = []
    while queue:
        node = queue.popleft()
        visited_nodes.append(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited_nodes


def draw_tree(tree_root, nodes, title):
    """Візуалізація дерева"""
    if not tree_root:
        print("Дерево порожнє")
        return
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    # Визначення кольорів для вузлів
    total_nodes = len(nodes)
    colors = [get_color(i, total_nodes - 1) for i in range(total_nodes)]
    for i, node in enumerate(nodes):
        for n in tree.nodes(data=True):
            if n[0] == node.id:
                n[1]['color'] = colors[i]

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=14, fontweight="bold")
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Побудова дерева
root = build_tree()

# Обхід у глибину (DFS) та його візуалізація
dfs_nodes = dfs_traversal(root)
draw_tree(root, dfs_nodes, "DFS")

# Обхід у ширину (BFS) та його візуалізація
bfs_nodes = bfs_traversal(root)
draw_tree(root, bfs_nodes, "BFS")
