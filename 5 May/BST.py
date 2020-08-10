class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.element=-1
class BST:
    def __init__(self):
        self.Tree=None
    def insert(self,element):
        newNode = Node()
        newNode.element=element
        if(self.Tree==None):
            self.Tree=newNode
        else:
            temp=self.Tree
            while(temp!=None):
                if(element<temp.left):
                    temp=temp.left
                else:
                    temp=temp.right
            temp=newNode

    def getMinValue(self,temp):
        while(temp.left is not None):
            temp=temp.left
        return temp
    def remove(self,element):
        temp=self.Tree
        while(temp.element!=element):
            parent=temp
            if(element<temp.element):
                temp=temp.left
            elif(element>temp.element):
                temp=temp.right
        if(temp.left is not None and temp.right is not None):
            newN=self.getMinValue(temp)

        if(parent.left==temp):
            parent.left=None
        else:
            parent.right=None


    def inOrderTraversal(self):
        self.preOrder(self.Tree)
    def inOrder(self,node):
        node=node.left
        print(node.element)
        node=node.right
    def postOrderTraversal(self):
        self.postOrder(self.Tree)
    def postOrder(self,node):
        node=node.left
        node=node.right
        print(node.element)
    def preOrderTraversal(self):
        self.postOrder(self.Tree)

    def preOrder(self, node):
        print(node.element)
        node = node.left
        node = node.right
    def leverOrderTraversal(self):
        self.levelOrder(self.Tree)
    def levelOrder(self,temp):
        lst=[]
        currentNode=self.Tree
        lst.append(currentNode)
        while(len(lst)>0):
            currentNode=lst[0]
            lst.append(currentNode.left)
            lst.append(currentNode.right)
            print(currentNode.element)
            lst.pop(0)




b=BST()
ch=input("Do u want to add element to the Tree?y/n")
while(ch=='y'):
    b.insert(int(input("Enter the element")))
    ch=input("Do you want to add more Elements?y/n")
b.inOrderTraversal()
b.preOrderTraversal()
b.postOrderTraversal()
b.leverOrderTraversal()
ch=input("Do u want to remove element from the Tree?y/n")
while(ch=='y'):
    b.remove (int(input("Enter the element to remove")))
    ch=input("Do you want to remove more Elements?y/n")
b.inOrderTraversal()