class Btree(object):
    class Node(object):
        
        def __init__(self,t):
            self.keys = []
            self.children = []
            self.leaf = True
            self._t = t
        
        def split(self,parent,payload):
            new_node = self.__class__(self._t)
            """ new_node = Node(self._t) 
            __class__와 Class()의 차이
             https://stackoverflow.com/questions/20623925/class-vs-self-class-when-creating-object
             """
            mid_point = self.size//2
            split_value = self.keys[mid_point]
            parent.add_key(split_value)
            """ 
            부무로의 요소 전달 없이 split을 진행하면 필연적으로 한쪽 subtree의 height가 깊은 현상이 발생한다.
            이를 부모에 요소를 전달 시키는 방식으로 바꿔 원소가 서브트리의 높이만 영향을 미치는 것이 아닌 전체트리의 높이에 영향을 미치게 만듦
            """
            new_node.children = self.children[mid_point + 1 :]
            self.children = self.children[: mid_point + 1]
            new_node.keys = self.keys[mid_point + 1 :] #큰 값 복사
            self.keys = self.keys[: mid_point] #부모에 하나 전달했으므로 -1
            
            if len(new_node.children) > 0:
                new_node.leaf = False
                
            parent.children = parent.add_child(new_node)
            if payload < split_value:
                return self
            else:
                return new_node
             
        @property
        def is_full(self):
            return self.size == 2 * self._t - 1
        
        @property    
        def size(self):
            return len(self.keys)
            
        def add_key(self,value):
            self.keys.append(value)
            self.keys.sort()
                
        def add_child(self,new_node):
            i = len(self.children) - 1
            while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
                i -= 1
            return self.children[:i+1] + [new_node] + self.children[i + 1:]
                        
            
    def __init__(self,t):
        self._t = t
        if self._t <= 1:
            raise ValueError("B-Tree must have a degree of 2 or more")
        self.root = self.Node(t)
            
    def insert(self,payload):
        node = self.root
        """루트가 full이면 새로운 루트를 만들고 기존 루트를 split처리한다."""
        if node.is_full:
            new_root = self.Node(self._t)
            new_root.children.append(self.root)
            new_root.leaf = False
            node = node.split(new_root,payload)
            self.root = new_root
        while not node.leaf:
            i = node.size - 1
            while i > 0 and payload < node.keys[i]:
                i -= 1
            if payload > node.keys[i]:
                i += 1
            next = node.children[i]
            """리프를 탐색하면서  Split을 진행해야 하는 노드는 Split을 모두 실행해준다. 
            이를 통해 부모 요소에 Split이 필요한 경우도 문제 없다. 
            일반적으론 leaf노드를 방문해 해당 노드에 key값을 전해준 뒤 재귀적으로 다시 탐색하면서 split이 필요한
            부모노드를 split한다. 
            """
            if next.is_full:
                node = next.split(node,payload)
            else:
                node = next
                
        node.add_key(payload)  
    
    
     
        
    def print_order(self):
        """Print an level-order representation."""
        this_level = [self.root]
        while this_level:
            next_level = []
            output = ""
            for node in this_level:
                if node.children:
                    next_level.extend(node.children)
                output += str(node.keys) + " "
            print(output)
            this_level = next_level
            
if __name__ == '__main__':
    nodes = []
    btree = Btree(2)
    for i in range(1,18):
        btree.insert(i)
    btree.print_order()