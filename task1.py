class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        """Реверсування однозв'язного списку."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort_insertion(self):
        """Сортування списку вставками."""
        if self.head is None:
            return

        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            sorted_head = self._sorted_insert(sorted_head, current)
            current = next_node

        self.head = sorted_head

    def _sorted_insert(self, sorted_head, new_node):
        if sorted_head is None or sorted_head.data >= new_node.data:
            new_node.next = sorted_head
            return new_node

        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

        return sorted_head

    def merge_sorted_lists(self, list1, list2):
        """Об'єднання двох відсортованих списків."""
        if list1.head is None:
            return list2
        if list2.head is None:
            return list1

        if list1.head.data < list2.head.data:
            merged_head = list1.head
            list1.head = list1.head.next
        else:
            merged_head = list2.head
            list2.head = list2.head.next

        current = merged_head

        while list1.head and list2.head:
            if list1.head.data < list2.head.data:
                current.next = list1.head
                list1.head = list1.head.next
            else:
                current.next = list2.head
                list2.head = list2.head.next
            current = current.next

        if list1.head:
            current.next = list1.head
        elif list2.head:
            current.next = list2.head

        self.head = merged_head
        return self
    

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Друк реверсованого зв'язного списку
llist.reverse()
print("\nРеверсований список:")
llist.print_list()

# Сортування списку
llist.sort_insertion()
print("\nВідсортований список:")
llist.print_list()

# Створення та об'єднання двох відсортованих списків
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

print("\nСписок 1:")
list1.print_list()

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

print("\nСписок 2:")
list2.print_list()

merged_list = LinkedList()
merged_list.merge_sorted_lists(list1, list2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()