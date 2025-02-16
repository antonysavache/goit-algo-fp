import uuid
import networkx as nx
import matplotlib.pyplot as plt

class HeapNode:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._heapify_up(parent)

    def to_tree_node(self, index=0):
        if index >= len(self.heap):
            return None

        node = HeapNode(self.heap[index])
        left_idx = self.left_child(index)
        right_idx = self.right_child(index)

        if left_idx < len(self.heap):
            node.left = self.to_tree_node(left_idx)
        if right_idx < len(self.heap):
            node.right = self.to_tree_node(right_idx)

        return node

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

def draw_heap(heap_root):
    tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(tree, heap_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def visualize_heap(values):
    # Create and populate the heap
    heap = BinaryHeap()
    for value in values:
        heap.insert(value)

    # Convert heap to tree structure and visualize
    root = heap.to_tree_node()
    draw_heap(root)

# Example usage
def test_heap_visualization():
    # Test with some sample values
    values = [4, 8, 2, 5, 1, 9, 3, 7, 6]
    print("Visualizing heap with values:", values)
    visualize_heap(values)

if __name__ == "__main__":
    test_heap_visualization()