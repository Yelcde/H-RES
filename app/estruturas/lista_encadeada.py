class ListaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga: any):
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self):
        return self.__carga

    @property
    def prox(self):
        return self.__prox

    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @prox.setter
    def prox(self, novoProx):
        self.__prox = novoProx

    def __str__(self):
        return f'{self.__carga}'

class ListaEncadeada:
    def __init__(self):
        self.__head = None
        self.__tamanho = 0

    def estaVazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

    def __len__(self):
        return self.__tamanho

    def inserir(self, posicao: int, carga: any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho + 1

            novo = No(carga)
            if self.estaVazia():
                self.__head = novo
                self.__tamanho += 1
                return

            if posicao == 1:
                novo.prox = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            cursor = self.__head
            contador = 1
            while contador < posicao - 1:
                cursor = cursor.prox
                contador += 1

            novo.prox = cursor.prox
            cursor.prox = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaException(f'A posição deve ser um número inteiro')
        except AssertionError:
            raise ListaException(
                f'A posicao deve ser um numero maior que zero e menor igual a {self.__tamanho+1}'
            )
        except:
            raise

    def append(self, carga: any):
        self.inserir(self.__tamanho + 1, carga)

    def remover(self, posicao: int) -> any:
        try:
            assert posicao > 0 and posicao <= self.__tamanho

            if self.estaVazia():
                raise ListaException(f'Não é possível remover de uma lista vazia')

            cursor = self.__head
            contador = 1

            while contador <= posicao - 1:
                anterior = cursor
                cursor = cursor.prox
                contador += 1

            carga = cursor.carga

            if posicao == 1:
                self.__head = cursor.prox
            else:
                anterior.prox = cursor.prox

            self.__tamanho -= 1
            return carga

        except TypeError:
            raise ListaException(f'A posição deve ser um número inteiro')
        except AssertionError:
            raise ListaException(f'A posicao não pode ser um número negativo')
        except:
            raise

    def busca(self, chave: any) -> int:
        cont = 1
        cursor = self.__head
        while cursor != None:
            if cursor.carga == chave:
                return cont
            cont += 1
            cursor = cursor.prox

        raise ListaException(f'Chave {chave} não encontrada')

    def elemento(self, posicao: int) -> any:
        try:
            assert posicao > 0 and posicao <= len(self)
            cont = 1
            cursor = self.__head
            while cursor != None:
                if cont == posicao:
                    break
                cont += 1
                cursor = cursor.prox

            return cursor.carga
        except AssertionError:
            raise ListaException('Posicao inválida')

    def __str__(self):
        s = '[ '
        cursor = self.__head
        while cursor != None:
            s += f'{cursor.carga}, '
            cursor = cursor.prox
        s = s[:-2] + ' ]'
        return s
