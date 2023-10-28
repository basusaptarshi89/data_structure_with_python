class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):               
        ret = "  " * level + str(self.data) + "\n"
        for c in self.children:
            ret += c.__str__(level + 1)
        return ret
    
    def addChild(self, child):
        self.children.append(child)


drinks = TreeNode('drinks', [])
cold = TreeNode('cold', [])
hot = TreeNode('hot', [])
cola = TreeNode('cola')
fanta = TreeNode('fanta')
tea = TreeNode('tea')
coffee = TreeNode('coffee')

drinks.addChild(cold)
drinks.addChild(hot)

cold.addChild(cola)
cold.addChild(fanta)

hot.addChild(coffee)
hot.addChild(tea)

print(drinks)

