class Node: # Класс Нода имеет следующие атрибуты: хранимые данные, ссылка на левый и правый элементы
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree: # Класс дерево имеет атрибут корень, который по умолчанию None (для пустого дерева)

    def __init__(self):
        self.root = None



    def search(self, node, value, parent): # Функция для поиска элемента с необходимым значением.
                                        # На вход принимает саму ноду, искомое значение и родителя.
                                        # Используется для добавления нового элемента - необходимо знать куда именно вставлять
                                        # новый элемент, а также для удаления элемента.

        if node is None:
            return node, parent, False

        if value == node.data:
            return node, parent, True

        if value > node.data:
            if node.right:
                return self.search(node.right, value, node)

        if value < node.data:
            if node.left:
                return self.search(node.left, value, node)

        return node, parent, False

    def add_node(self, node): # Функция для добавления нового элемента.
                              # На вход принимает ноду
        if self.root is None:
            self.root = node
            return node
        else:
            res = self.search(self.root, node.data, None)
            if res[2] is False:

                if node.data > res[0].data:
                    res[0].right = node
                else:
                    res[0].left = node
            return node

    def show_tree(self, node): # Функция для отображения дерева
        if node:
            print(node.data)
            self.show_tree(node.left)
            self.show_tree(node.right)

    def find_left(self, node, parent): # Функция для поиска минимальной ноды дерева в в заданном диапозоне
        if node.left:
            return self.find_left(node.left, node)
        return node, parent
    def remove_node(self, value): # Функция для удаления элемента с необходимым значением.
                                        # На вход принимает значение.
                                        # Рассматривается три случая возможного расположения удаляемой ноды в дереве

        res = self.search(self.root, value, None)

        if res[2] is False: # Ноды с таким значением нет
            return None

        if res[0].left is None and res[0].right is None: # Нода не имеет потомков, те является листом
            if res[1].left:
                if res[1].left.data == value:
                    res[1].left = None
            if res[1].right:
                if res[1].right.data == value:
                    res[1].right = None

        if res[0].left is None or res[0].right is None: # Нода имеет только одного потомка
            if res[1].left == res[0]:
                if res[0].left is None:
                    res[1].left = res[0].right
                if res[0].right is None:
                    res[1].left = res[0].left
            if res[1].right == res[0]:
                if res[0].left is None:
                    res[1].right = res[0].right
                if res[0].right is None:
                    res[1].right = res[0].left

        else:
            res_min = self.find_left(res[0].right, res[0]) # Нода имеет двух потомков
            res[0].data = res_min[0].data
            if res_min[0].right:
                res_min[1].right = res_min[0].right
            else: res_min[1].left = None









tree_1 = Tree()

tree_1.add_node(Node(15))
#tree_1.add_node(Node(17))
tree_1.add_node(Node(20))
tree_1.add_node(Node(10))
tree_1.add_node(Node(8))
tree_1.add_node(Node(16))


tree_1.show_tree(tree_1.root)
print(20*'* ')

tree_1.remove_node(15)

tree_1.show_tree(tree_1.root)