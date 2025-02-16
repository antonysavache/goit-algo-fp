import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#FFFFFF"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def generate_color_gradient(step, total_steps):
    """Generate color from dark to light blue in hex format"""
    # Start with dark blue (18, 150, 240) to light blue (178, 235, 242)
    r = int(18 + (178 - 18) * (step / total_steps))
    g = int(150 + (235 - 150) * (step / total_steps))
    b = int(240 + (242 - 240) * (step / total_steps))
    return f"#{r:02x}{g:02x}{b:02x}"

def bfs_with_colors(root):
    """Perform BFS and assign colors to nodes based on visit order"""
    if not root:
        return

    queue = deque([(root, 0)])
    visited = {}
    step = 0
    total_nodes = count_nodes(root)

    while queue:
        node, level = queue.popleft()
        if node.id not in visited:
            visited[node.id] = True
            node.color = generate_color_gradient(step, total_nodes - 1)
            step += 1

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

    return root

def dfs_with_colors(root):
    """Perform DFS and assign colors to nodes based on visit order"""
    if not root:
        return

    stack = [root]
    visited = {}
    step = 0
    total_nodes = count_nodes(root)

    while stack:
        node = stack.pop()
        if node.id not in visited:
            visited[node.id] = True
            node.color = generate_color_gradient(step, total_nodes - 1)
            step += 1

            # Add right first so left is processed first (stack is LIFO)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return root

def count_nodes(root):
    """Count total number of nodes in the tree"""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

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

def draw_tree(root, title="Binary Tree"):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def create_sample_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def visualize_traversals():
    # Create and visualize BFS traversal
    bfs_tree = create_sample_tree()
    bfs_with_colors(bfs_tree)
    draw_tree(bfs_tree, "BFS Traversal (Color indicates visit order)")

    # Create and visualize DFS traversal
    dfs_tree = create_sample_tree()
    dfs_with_colors(dfs_tree)
    draw_tree(dfs_tree, "DFS Traversal (Color indicates visit order)")

if __name__ == "__main__":
    visualize_traversals()