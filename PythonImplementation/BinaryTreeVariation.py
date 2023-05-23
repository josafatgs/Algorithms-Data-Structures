class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    
    def DFS(self):
        print(self.data)
        if self.left:
            self.left.DFS()
        if self.right:
            self.right.DFS()
    def BFS(self, visited = []):
        
        if self.data in visited:
            pass
        else:
            print(self.data)

        #Verificar que el nodo izquierdo exista
        if self.left:
            if self.left.data in visited:
                pass
            else:
                print(self.left.data)
                visited.append(self.left.data)

        #Verificar que el nodo derecho exista
        if self.right:
            if self.right.data in visited:
                pass
            else:
                print(self.right.data)
                visited.append(self.right.data)
        
        #Verficar que el nodo izquierdo exista
        if self.left:
            self.left.BFS(visited)
        #Verificar que el nodo derecho exista
        if self.right:
            self.right.BFS(visited)
        


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.left = B
A.right = C
B.left = D
B.right = E
C.right = F

#A.DFS()
A.BFS()

"""
    A
   / \
  B   C
 / \    \
D   E    F
"""

