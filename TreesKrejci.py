#Jack Krejci

#Binary Tree Class
import queue
class BinaryTree:

    #Class for the nodes in the tree
    class _Node:
        def __init__(self, element, left = None, right = None):
            self._left = left
            self._right = right
            self._element = element


    #Binary tree functions

    def __init__(self):
        self._root = None
        #We start with an empty tree
        self._size = 0

    #Length
    def __len__(self):
        return self._size
    
    #Function to get the root of the tree
    def root(self):
        return self._root

    #Function to add the root element
    def add_root(self, e):
        if self._root: #if self._root is not None same thing
            raise Exception()
        
        #Create root when there's no root yet
        node = self._Node(e)
        self._root = node

        #Increase the size of the tree
        self._size += 1
        return node

    #Function to add nodes in tree as left child
    def add_left(self, e, p): #e is element you're inserting, p is the node you're adding it to
        node = self._Node(element = e)
        #New node becomes left child of p
        p._left = node

        #Increase the size of the tree
        self._size += 1        
        return node
        
    #Function to add nodes in tree as right child same concept as left
    def add_right(self, e, p):
        node = self._Node(element = e)
        p._right = node

        #Increase the size of the tree
        self._size += 1       
        return node

    #In order traversal of binary tree (the version for iteration we use the function version for non iteration like the other ones)
    def in_order(self):
       for e in self._in_order(self._root):
           yield e
    #Recursive function for in order traversale
    def _in_order(self, p):
        if p is not None:
            #Visit left subtree then visit the node then the right subtree
            #Need to do recursive call on left and right subtree
            for other in self._in_order(p._left):
                yield other

            yield p._element
            for other in self._in_order(p._right):
                yield other
        #If p is actually none we don't have to do anything

    #Count the number of times a value appears in a tree
    def countK(self, num):
        #Initialize a counter to see how many elements match
        count = 0

        #If the tree is empty return 0
        if self._size == 0:
            return count
        
        for e in self._in_order(self._root):
            if e == num:
                count += 1
        return count

    #Pre order traversal (Visit the node then go left then right)
    def pre_order(self):
        self._pre_order(self._root)
    #Preform the traversal recursively (Need to two functions for a recursive call to be possible)
    def _pre_order(self, p):
        if p is not None:
            print(p._element)
            self._pre_order(p._left)
            self._pre_order(p._right)
        
    #Post order traversal (Visit left/right then visit the node)
    def post_order(self):
        self._post_order(self._root)
    #Preform the recursion and printing
    def _post_order(self, p):
        if p is not None:
            self._post_order(p._left)
            self._post_order(p._right)
            print(p._element)

    #Breadth first function (Visit the nodes let to right in each level from lowest to highest level)
        #we can use a queue for this
    def breadth_first(self):
        #No recursion with a breadth first search
        #Use the yield method for iteration (simply just change print(p._element) to yield p._element to use it in this fashion)
        #We need to push the root first then get into the loop
        q = queue.Queue()
        q.put(self._root)

        #Loop for each of the children and grandchildren etc for the root
        while not q.empty():
            p = q.get()
            #Do below if left and right children aren't nothing (Make sure to start with left)
            if p._left:
                q.put(p._left)
            if p._right:
                q.put(p._right)

            print(p._element)

    #Find height of the function
    #Height of any node p is 1 + the height of its left or right subtree (the max between the two)
    def height(self):
        return self._height(self._root)

    #Worst case of this is n (if the tree is completely linear)
    #Best case of this if the tree is balanced it will be logn
    def _height(self, p):
        #Return 0 if tree is empty
        if p is None:
            return 0

        #Otherwise return the height using the left and right method discussed above
        height_left = self._height(p._left)
        height_right = self._height(p._right)

        #Add one to biggest one of the two and return as height
        return 1 + max(height_left, height_right)

    #Check if another tree is equivalent to another tree
    def equal(self, btree2):
        is_equal = self._equal(self._root, btree2._root)
        if is_equal == 1:
            return True
        else:
            return False
    #Call another function with the roots of the two to see traveling them and see if they're equal
    def _equal(self, a, b): #a is self._root and b is btree2._root
        #Base Case: Return true if both nodes are none, false if one is none while the other isn't none
        if a is None and b is None:
            return 1
        if a is None or b is None:
            return 0
        
        #Recursion: If the node for a and b aren't equal return False (0), if they are equal step through left and right subtree
        if a._element != b._element:
            return 0

        #Walk through the left and right subtree (Need to check for their values seperately, or you'll run into
            #a problem where it will stop everything after checking the left subtree if all the nodes were equal in it)
        if self._equal(a._left, b._left) != 1:
            return 0
        if self._equal(a._right, b._right) != 1:
            return 0
        
        #If it is able to completely walk through the recursion return true (1) 
        return 1
    

    
#Main Code
#Here we build two trees to check for our to functions, this is a sample of that checking process!

#Below is not how we typically build a tree we will talk more in binary search of a tree)
#Set btree as a new binary tree
btree = BinaryTree()
#Add 4 as the root to the tree
root = btree.add_root(4)

#Add left node to the root
node = btree.add_left(2, root)

#Build left sub tree of 2
btree.add_left(1, node)
btree.add_right(3, node)

#Build right subtree of 2
node = btree.add_right(6, root)
btree.add_left(5, node)
btree.add_right(7, node)


#Print the pre order traversal
btree.post_order()
print()


#Show how many times 5 appears in the tree
print("5 appears", btree.countK(5) ,"times in the tree")
print()


#Check if another tree equals the original tree
#Set btree as a new binary tree
btree2 = BinaryTree()
#Add 4 as the root to the tree
root = btree2.add_root(4)

#Add left node to the root
node = btree2.add_left(2, root)

#Build left sub tree of 2
btree2.add_left(1, node)
btree2.add_right(3, node)

#Build right subtree of 2
node = btree2.add_right(6, root)
btree2.add_left(5, node)
btree2.add_right(7, node)

#The elements in the second tree
print("Below are the elements in the second tree:")
btree2.pre_order()
print()

#Use the equal function in the tree to see if btree and btree2 are equal
print("btree and btree2 are equal (T/F):", btree.equal(btree2))

