"""
Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:

-написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
-розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
-написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.

"""

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
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
  
    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current:
            next_node = current.next
            current.next = None
            sorted_list.sorted_insert(current)
            current = next_node
        self.head = sorted_list.head

    def sorted_merge(self, other_list):
        merged_list = LinkedList()
        p = self.head
        q = other_list.head
        while p and q:
            if p.data <= q.data:
                merged_list.insert_at_end(p.data)
                p = p.next
            else:
                merged_list.insert_at_end(q.data)
                q = q.next
        while p:
            merged_list.insert_at_end(p.data)
            p = p.next
        while q:
            merged_list.insert_at_end(q.data)
            q = q.next
        return merged_list




llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("First list:")
llist.print_list()

print("Reverse:")
llist.reverse()
llist.print_list()

print("Sorting:")
llist.insertion_sort()
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_beginning(2)
llist2.insert_at_beginning(34)
llist2.insert_at_beginning(1)
llist2.insert_at_beginning(3)
llist2.insert_at_beginning(43)
llist2.insert_at_beginning(23)
llist2.insertion_sort()
print("Other sorted list")
llist2.print_list()
print("Merged sorted lists:")
llist = llist.sorted_merge(llist2)
llist.print_list()