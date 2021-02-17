import sys
class Red_black_tree:
    class Node:
        def __init__(self,val):
            self.value = val
            self.height = 0
            self.color  = "Red"
            self.parent  = None
            self.left = None
            self.right = None

    def __init__(self):
        nil_node = self.Node(0)
        nil_node.color = "Black"
        self.Nil = nil_node
        self.root = self.Nil
        self.count = 0
        self.count_array = [0]


    def left_rotate(self,node):
        sub_node = node.right
        node.right = sub_node.left
        if sub_node.left != self.Nil: # 기준노드의 왼쪽에 손자 노드가 존재하면, 기준노드와 연결 해야 하기 떄문에 부모를  재설정해준다
            sub_node.left.parent = node 
        sub_node.parent = node.parent
        if node.parent == self.Nil:
            self.root = sub_node

        elif node.parent.left == node:
            node.parent.left = sub_node
        else: 
            node.parent.right = sub_node
        sub_node.left = node
        node.parent = sub_node

    def right_rotate(self,node):
        sub_node = node.left
        node.left = sub_node.right
        if sub_node.right != self.Nil:
            sub_node.right.parent = node
        sub_node.parent = node.parent
        if node.parent == self.Nil:
            self.root = sub_node
        elif node.parent.left == node:
            node.parent.left = sub_node
        else: 
            node.parent.right = sub_node
        sub_node.right = node
        node.parent = sub_node


    def fix_up(self,node):
        while node.parent.color == "Red":
            grandparent = node.parent.parent
            if node.parent == grandparent.left:
                uncle = grandparent.right
                if  uncle.color == "Red":
                    uncle.color = "Black"
                    node.parent.color = "Black"
                    grandparent.color = "Red"
                    node = node.parent.parent
                else:
                    if node.parent.right == node:
                        node = node.parent #Double red가 다른 서브트리에서도 일어나는지 확인해야 하기 떄문에
                        self.left_rotate(node)
                    node.parent.color = "Black"
                    grandparent.color = "Red"    
                    self.right_rotate(grandparent)
                    

            else:
                uncle = grandparent.left
                if uncle.color == "Red":
                    uncle.color = "Black"
                    node.parent.color = "Black"
                    grandparent.color = "Red"
                    node = node.parent.parent

                else:
                    if node.parent.left == node:
                        node = node.parent #Double red가 다른 서브트리에서도 일어나는지 확인해야 하기 떄문에
                        self.right_rotate(node)
                    node.parent.color = "Black"
                    grandparent.color = "Red"    
                    self.left_rotate(grandparent)
                
        self.root.color = "Black"

    def successor(self,node):
        node_next_me = None
        parent = node.parent
        while parent != self.Nil:
            if node == parent.left:
                node_next_me = parent
                return node_next_me
            else:
                node = parent
                parent = node.parent

        return self.Nil

    def predecessor(self,node):
        node_next_me = None
        parent = node.parent
        while parent != self.Nil:
            if node == parent.right:
                node_next_me = parent
                return node_next_me
            else:
                node = parent
                parent = node.parent

        return self.Nil

    def insert(self,new_node):
        node_parent = self.Nil
        node_loc = self.root
        while node_loc != self.Nil:
            node_parent = node_loc
            if new_node.value < node_parent.value:
                node_loc = node_loc.left
        
            else: 
                node_loc = node_loc.right

        new_node.parent = node_parent

        if node_parent == self.Nil:
            self.root = new_node
            
        elif node_parent.value > new_node.value:
            node_parent.left = new_node
        else:
            node_parent.right = new_node

        new_node.right = self.Nil
        new_node.left = self.Nil

        if node_parent != self.Nil:
            suc = self.successor(new_node)
            pre = self.predecessor(new_node)  
            new_node.height = max(suc.height,pre.height) + 1
            self.count += new_node.height
            self.count_array.append(self.count)
        self.fix_up(new_node)

                

if __name__ == "__main__":
    node_count = int(sys.stdin.readline()) 
    red_black = Red_black_tree()

    for i in range(node_count):
        value = int(sys.stdin.readline()) 
        node = red_black.Node(value)
        red_black.insert(node)
   
    for c in red_black.count_array:
        print(c)
