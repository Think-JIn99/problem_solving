#트리
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        
    def show(self):
        print(self.data)
        
def insert(num,node):
    child = Node(num)
    if node.data > num: ##현재 노드의 데이터가 insert하려는 값보다 클 경우 왼쪽으로 
        if node.left == None:
            node.left = child
            child.parent = node
        else: 
            insert(num,node.left)
              
    if node.data < num:
        if node.right == None:
            node.right = child
            child.parent = node
        else: 
            insert(num,node.right)
            

def inorder(node): #트리전체를 순회하며 값 조회
    if(node is None): return
    inorder(node.left)
    node.show()
    inorder(node.right)

def preorder(num,node):
    current = node
    stack = []
    while stack or current:
        if current:
            if current.data == num: break #삭제할 노드 탐색 후 리턴
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            current = current.right
       
    return current
    
def successor(node):
    if node.right != None: #우측 서브트리가 존재하면 해당 트리의 최소 값이 곧 Successor
        loc = node.right
        while loc.left:
            loc = loc.left #가장 좌측 값이 최소 값이다..
            
        return loc
    
    #우측 서브트리가 없다면 왼쪽 루트를 처음으로 타게하는 노드가 Successor
    # parent = node.parent
    # while parent is not None and parent.right == node: 
    #     node = parent
    #     parent = node.parent
        
    # return parent
            
    
def delete(loc):
    global root
    node_removed = None #실질적으로 삭제할 노드
    node_child = None #삭제할 노드의 자식
    if loc.left is None or loc.right is None: 
        node_removed = loc #자식이 1개 이하면 삭제해야할 노드와 실질적으로 삭제할 노드가 일치
        
    #자식이 2개인 경우 실질적으로 삭제할 노드(Successor)와 삭제해야할 노드가 불일치  
    else: node_removed = successor(loc)
    
    #삭제할 노드의 자식 값을 초기화
    if node_removed.left is not None:
        node_child = node_removed.left
        
    else:
        node_child = node_removed.right
        
    if node_child:
        node_child.parent = node_removed.parent
        
    #루트를 삭제하는 경우          
    #루트를 삭제하는 경우는 루트가 1개 이하의 자식을 갖는 경우만 존재
    #루트가 Successor로서 존재 불가하기 때문 2개 이상의 자식이면 부모가 아닌 오른쪽 서브트리의 최소가 Successor
    #1개의 자식의 경우 삭제만 진행하면 되기 때문에 삭제 진행 후 리턴 
    if node_removed.parent is None:
        root = node_child
        return node_removed.data
        
    #삭제할 노드를 제외하고 노드를 연결.     
    elif node_removed == (node_removed.parent).left:  
        (node_removed.parent).left = node_child
        
    elif node_removed == (node_removed.parent).right:  
        (node_removed.parent).right = node_child    
    
    if node_removed != loc:  
        loc.data = node_removed.data       
        
    #실질적으로 삭제된 노드
    return  node_removed.data
    
       
if __name__ == '__main__':
    f = open('test.txt','r')
    node_count = int(f.readline()) 
    data = []
    for i in range(node_count):
        data.append(int(f.readline()))   #strip은 양 끝의 개행문자를 제거해준다.
    root = Node(data[0])
    for j in data[1:]:
        insert(j,root)
    inorder(root)
    print('removed: %d' % delete(preorder(1,root)))
    inorder(root)