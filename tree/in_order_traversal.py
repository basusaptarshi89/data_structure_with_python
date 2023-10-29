class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_l_child(self, node):
        self.left = node
    
    def add_r_child(self, node):
        self.right = node
    
    def __str__(self):
        i = 0
        stack = []
        pointer = self        

        _str = ""
        while pointer or stack:            
            if pointer:                
                _str += "  " * i + str(pointer.data) + "\n"                
                if pointer.right:
                    stack.append({"p": pointer.right, "l": i+1})
                pointer = pointer.left
                i += 1
                
            elif stack:
                item = stack.pop()
                pointer = item.get("p")
                i = item.get("l")
        return _str


def prepare_data():
    drinks = Node('Drinks')
    hot = Node('hot')
    cold = Node('cold')
    tea = Node('tea')
    masala_tea = Node('masala_tea')
    cofee = Node('cofee')
    cola = Node('cola')
    fanta = Node('fanta')    

    drinks.add_l_child(hot)
    drinks.add_r_child(cold)

    hot.add_l_child(tea)
    hot.add_r_child(cofee)

    tea.add_l_child(masala_tea)

    cold.add_l_child(cola)
    cold.add_r_child(fanta)   

    return drinks


def in_order_traversal(node):
    stack = []
    
    while True:
        if node:
            stack.append(node)
            node = node.left
        else:
            if stack:
                t = stack.pop()
                print(t.data)
                node = t.right
            else:
                break

drinks = prepare_data()
print(drinks)
in_order_traversal(drinks)
