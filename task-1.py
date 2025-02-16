
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Task 1.1: Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Task 1.2: Insertion sort for linked list
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return

        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def _sorted_insert(self, sorted_head, new_node):
        if not sorted_head or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        return sorted_head

    # Task 1.3: Merge two sorted linked lists
    @staticmethod
    def merge_sorted_lists(list1, list2):
        merged_list = LinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 and current2:
            if current1.data <= current2.data:
                merged_list.append(current1.data)
                current1 = current1.next
            else:
                merged_list.append(current2.data)
                current2 = current2.next

        # Add remaining elements from list1, if any
        while current1:
            merged_list.append(current1.data)
            current1 = current1.next

        # Add remaining elements from list2, if any
        while current2:
            merged_list.append(current2.data)
            current2 = current2.next

        return merged_list

# Example usage:
def test_linked_list():
    # Test reversal
    llist = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        llist.append(i)
    print("Original list:")
    llist.print_list()
    llist.reverse()
    print("Reversed list:")
    llist.print_list()

    # Test sorting
    unsorted_list = LinkedList()
    for i in [4, 2, 1, 5, 3]:
        unsorted_list.append(i)
    print("\nUnsorted list:")
    unsorted_list.print_list()
    unsorted_list.insertion_sort()
    print("Sorted list:")
    unsorted_list.print_list()

    # Test merging
    list1 = LinkedList()
    list2 = LinkedList()
    for i in [1, 3, 5]:
        list1.append(i)
    for i in [2, 4, 6]:
        list2.append(i)
    print("\nList 1:")
    list1.print_list()
    print("List 2:")
    list2.print_list()
    merged = LinkedList.merge_sorted_lists(list1, list2)
    print("Merged list:")
    merged.print_list()

if __name__ == "__main__":
    test_linked_list()