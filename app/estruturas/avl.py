class No:
    def __init__(self, carga: any):
        self.__carga = carga
        self.__esq = None
        self.__dir = None
        self.__altura = 1 # atributo que especifica a altura que determina o fator de balanco do nó

    @property
    def carga(self) -> any:
        return self.__carga

    @property
    def esq(self) -> any:
        return self.__esq

    @property
    def dir(self) -> any:
        return self.__dir

    @property
    def altura(self) -> any:
        return self.__altura

    @carga.setter
    def carga(self, nova_carga: any):
        self.__carga = nova_carga

    @esq.setter
    def esq(self, nova_esq: any):
        self.__esq = nova_esq

    @dir.setter
    def dir(self, nova_dir: any):
        self.__dir = nova_dir

    @altura.setter
    def altura(self, nova_altura: any):
        self.__altura = nova_altura

    def __str__(self):
        return f'|{self.carga}:h={self.altura}|'

class AVL:
    def __init__(self, carga: any = None):
        self.__raiz = carga

    @property
    def raiz(self)->any:
        return self.__raiz

    def esta_vazia(self) -> bool:
        return self.__raiz == None

    def busca(self, chave: any) -> any:
        if (self.__raiz != None):
            carga = self.__busca_dado(chave, self.__raiz)
            return carga

    def __busca_dado(self, chave: any, no: No) -> No:
        if (chave == no.carga):
            return no
        elif (chave < no.carga and no.esq != None):
            return self.__busca_dado(chave, no.esq)
        elif (chave > no.carga and no.dir != None):
            return self.__busca_dado(chave, no.dir)
        else:
            return None

    def count(self) -> int:
        return self.__count(self.__raiz)

    def __count(self, no: No) -> int:
        if (no == None):
            return 0
        else:
            return 1 + self.__count(no.esq) + self.__count(no.dir)

    def __len__(self):
        return self.count()

    def inserir(self, chave: any):
        if(self.__raiz == None):
            self.__raiz = No(chave)
        else:
            self.__raiz = self.__inserir(self.__raiz, chave)

    def __inserir(self, no: No, chave: any):
        # Step 1 - Performs a BST recursion to add the no
        if not no:
            return No(chave)
        elif chave < no.carga:
            no.esq = self.__inserir(no.esq, chave)
        else:
            no.dir = self.__inserir(no.dir, chave)

        # Step 2 - Update the height of ancestor no
        no.altura = 1 + max(self.pegar_altura(no.esq),
                              self.pegar_altura(no.dir))

        # Step 3 - Computes the balance factor
        balanceamento = self.__pegar_balanceamento(no)

        # Step 4 - Checks if the no is unbalanced
        # Then, one of the following actions will be performed:

        # CASE 1 - Right rotation
        if balanceamento > 1 and chave < no.esq.carga:
            return self.__rotacao_dir(no)

        # CASE 2 - Left rotation
        if balanceamento < -1 and chave > no.dir.carga:
            return self.__rotacao_esq(no)

        # CASE 3 - Double rotation: Left Right
        if balanceamento > 1 and chave > no.esq.carga:
            no.esq = self.__rotacao_esq(no.esq)
            return self.__rotacao_dir(no)

        # CASE 4 - Double rotation: Right Left
        if balanceamento < -1 and chave < no.dir.carga:
            no.dir = self.__rotacao_dir(no.dir)
            return self.__rotacao_esq(no)

        return no

    def __rotacao_esq(self, p: No) -> No:
        u = p.dir
        T2 = u.esq

        # Perform rotation
        u.esq = p
        p.dir = T2

        # Update heights
        p.altura = 1 + max(self.pegar_altura(p.esq),
                         self.pegar_altura(p.dir))
        u.altura = 1 + max(self.pegar_altura(u.esq),
                         self.pegar_altura(u.dir))

        # Return the new root 'u' no
        return u

    def __rotacao_dir(self, p: No) -> No:
        u = p.esq
        T2 = u.dir

        # Perform rotation
        u.dir = p
        p.esq = T2

        # Update heights
        p.altura = 1 + max(self.pegar_altura(p.esq),
                        self.pegar_altura(p.dir))
        u.altura = 1 + max(self.pegar_altura(u.esq),
                        self.pegar_altura(u.dir))

        # Return the new root ('u' no)
        return u

    def pegar_altura(self, no: No) -> int:
        if no is None:
            return 0

        return no.altura

    def __pegar_balanceamento(self, no: No) -> int:
        if not no:
            return 0

        return self.pegar_altura(no.esq) - self.pegar_altura(no.dir)

    def preOrdem(self):
        self.__preOrdem(self.__raiz)

    def __preOrdem(self, no: No):
        if not no:
            return

        print('{0} '.format(no.carga), end='')
        self.__preOrdem(no.esq)
        self.__preOrdem(no.dir)

    def remover(self, chave: any):
        if(self.__raiz is not None):
            self.__raiz = self.__remover(self.__raiz, chave)

    def __remover(self, no: No, chave: any) -> No:
        # Step 1 - Perform standard BST delete
        if not no:
            return no
        elif chave < no.carga:
            no.esq = self.__remover(no.esq, chave)
        elif chave > no.carga:
            no.dir = self.__remover(no.dir, chave)
        else:
            if no.esq is None:
                temp = no.dir
                no = None
                return temp

            elif no.dir is None:
                temp = no.esq
                no = None
                return temp

            temp = self.__pegar_menor_valor(no.dir)
            no.carga = temp.carga
            no.dir = self.__remover(no.dir,
                                      temp.carga)

        # If the tree has only one no,
        # simply return it
        if no is None:
            return no

        # Step 2 - Update the height of the
        # ancestor no
        no.altura = 1 + max(self.pegar_altura(no.esq),
                            self.pegar_altura(no.dir))

        # Step 3 - Get the balance factor
        balanceamento = self.__pegar_balanceamento(no)

        # Step 4 - If the no is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balanceamento > 1 and self.__pegar_balanceamento(no.esq) >= 0:
            return self.__rotacao_dir(no)

        # Case 2 - Right Right
        if balanceamento < -1 and self.__pegar_balanceamento(no.dir) <= 0:
            return self.__rotacao_esq(no)

        # Case 3 - Left Right
        if balanceamento > 1 and self.__pegar_balanceamento(no.esq) < 0:
            no.esq = self.__rotacao_esq(no.esq)
            return self.__rotacao_dir(no)

        # Case 4 - Right Left
        if balanceamento < -1 and self.__pegar_balanceamento(no.dir) > 0:
            no.dir = self.__rotacao_dir(no.dir)
            return self.__rotacao_esq(no)

        return no

    def __pegar_menor_valor(self, no: No) -> No:
        if no is None or no.esq is None:
            return no

        return self.__pegar_menor_valor(no.esq)
