# Classe que implementa as operações básicas de uma Árvore AVL
# Código Original: 
#  https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
#  https://www.geeksforgeeks.org/avl-tree-set-2-deletion/?ref=lbp
# Adaptações feitas pelo professor Alex para a disciplina de Estrutura de Dados
# Última modificação: 17/05/2022
  
class No(object): 
    def __init__(self, value): 
        self.value = value 
        self.left = None
        self.right = None
        self.height = 1 # atributo que especifica a altura que determina o fator de balanco do nó
    
    def __str__(self):
        return f'|{self.value}:h={self.height}|'
  
# Classe AVL tree 
class AVLTree(object): 

    def __init__(self, value:object = None):
        self.__root = value


    def getRoot(self)->any:
        return None if self.__root is None else self.__root.value

    def isEmpty(self)->bool:
        return self.__root == None

    def search(self, key:any )->any:
        if( self.__root != None ):
            value = self.__searchData(key, self.__root)
            return None if value is None else value
        else:
            return None
    
    def __searchData(self, key:any, no:No)->No:
        if ( key == no.value):
            return no
        elif ( key < no.value and no.left != None):
            return self.__searchData( key, no.left)
        elif ( key > no.value and no.right != None):
            return self.__searchData( key, no.right)
        else:
            return None

    def count(self)->int:
        return self.__count(self.__root)

    def __count(self, no:No)->int:
        if ( no == None):
            return 0
        else:
            return 1 + self.__count(no.left) + self.__count(no.right)

    def __len__(self):
        return self.count()


    def insert(self, key:object):
        if(self.__root == None):
            self.__root = No(key)
        else:
            self.__root = self.__insert(self.__root, key)
  
    def __insert(self, root, key):
        # Step 1 - Performs a BST recursion to add the no
        if not root: 
            return No(key) 
        elif key < root.value: 
            root.left = self.__insert(root.left, key) 
        else: 
            root.right = self.__insert(root.right, key) 
  
        # Step 2 - Update the height of ancestor no
        root.height = 1 + max(self.getHeight(root.left), 
                              self.getHeight(root.right)) 
  
        # Step 3 - Computes the balance factor 
        balance = self.__getBalance(root) 
  
        # Step 4 - Checks if the no is unbalanced
        # Then, one of the following actions will be performed:

        # CASE 1 - Right rotation
        if balance > 1 and key < root.left.value: 
            return self.__rightRotate(root) 
  
        # CASE 2 - Left rotation
        if balance < -1 and key > root.right.value: 
            return self.__leftRotate(root) 
  
        # CASE 3 - Double rotation: Left Right 
        if balance > 1 and key > root.left.value: 
            root.left = self.__leftRotate(root.left) 
            return self.__rightRotate(root) 
  
        # CASE 4 - Double rotation: Right Left 
        if balance < -1 and key < root.right.value: 
            root.right = self.__rightRotate(root.right) 
            return self.__leftRotate(root) 
  
        return root 
  
    def __leftRotate(self, p:No)->No: 
        u = p.right 
        T2 = u.left 
  
        # Perform rotation 
        u.left = p 
        p.right = T2 
  
        # Update heights 
        p.height = 1 + max(self.getHeight(p.left), 
                         self.getHeight(p.right)) 
        u.height = 1 + max(self.getHeight(u.left), 
                         self.getHeight(u.right)) 
  
        # Return the new root "u" no 
        return u 
  
    def __rightRotate(self, p:No)->No: 
        u = p.left 
        T2 = u.right 
  
        # Perform rotation 
        u.right = p 
        p.left = T2 
  
        # Update heights 
        p.height = 1 + max(self.getHeight(p.left), 
                        self.getHeight(p.right)) 
        u.height = 1 + max(self.getHeight(u.left), 
                        self.getHeight(u.right)) 
  
        # Return the new root ("u" no)
        return u 
  
    def getHeight(self, no:No)->int: 
        if no is None: 
            return 0
  
        return no.height 
  
    def __getBalance(self, no:No)->int: 
        if not no: 
            return 0
  
        return self.getHeight(no.left) - self.getHeight(no.right) 
  
    def preOrder(self):
        self.__preOrder(self.__root)

    def __preOrder(self, root): 
        if not root: 
            return
  
        print("{0} ".format(root.value), end="") 
        self.__preOrder(root.left) 
        self.__preOrder(root.right) 

    def delete(self, key:object):
        if(self.__root is not None):
            self.__root = self.__delete(self.__root, key)
        

    def __delete(self, root:No, key:object)->No: 
        # Step 1 - Perform standard BST delete 
        if not root: 
            return root   
        elif key < root.value: 
            root.left = self.__delete(root.left, key)   
        elif key > root.value: 
            root.right = self.__delete(root.right, key)   
        else: 
            if root.left is None: 
                temp = root.right 
                root = None
                return temp 
  
            elif root.right is None: 
                temp = root.left 
                root = None
                return temp 
  
            temp = self.__getMinValueNode(root.right) 
            root.value = temp.value 
            root.right = self.__delete(root.right, 
                                      temp.value) 
  
        # If the tree has only one no, 
        # simply return it 
        if root is None: 
            return root 
  
        # Step 2 - Update the height of the  
        # ancestor no 
        root.height = 1 + max(self.getHeight(root.left), 
                            self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.__getBalance(root) 
  
        # Step 4 - If the no is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and self.__getBalance(root.left) >= 0: 
            return self.__rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and self.__getBalance(root.right) <= 0: 
            return self.__leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and self.__getBalance(root.left) < 0: 
            root.left = self.__leftRotate(root.left) 
            return self.__rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and self.__getBalance(root.right) > 0: 
            root.right = self.__rightRotate(root.right) 
            return self.__leftRotate(root) 
  
        return root  
    
    def __getMinValueNode(self, root:No)->No:
        if root is None or root.left is None:
            return root
 
        return self.__getMinValueNode(root.left)