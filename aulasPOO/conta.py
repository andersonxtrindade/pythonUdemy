from abc import ABC, abstractmethod
from random import randint

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Idade deve ser um numero inteiro. ")
        self._idade = valor

class Conta(Pessoa, ABC):
    def __init__(self, nome, idade, agencia, conta, saldo):
        super().__init__(nome, idade)
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def descricao(self):
        print(f"Nome: {self.nome}, Idade {self.idade},Agencia: {self._agencia} Conta: {self._conta}, Saldo: {self._saldo}")


    def depositar(self, valor):
        self._saldo += valor
        print(f"Adicionando {valor} a conta!")

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, nome, idade, agencia, conta, saldo, limite = 1000):
        super().__init__(nome, idade, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        self._saldo -= valor
        self._limite -= valor
        if self._saldo < 0:
            print("Saldo insuficiente!")
            self._saldo += valor
            self._limite += valor
            return
        if self._limite< 0:
            self._saldo += valor
            self._limite += valor
            print("Limite de saque diario alcançado!")
            return
        self._saldo += valor

        print(f"Removendo {valor} da conta!")


class ContaPoupança(Conta):
    def __init__(self, nome, idade, agencia, conta, saldo, limite = 500):
        super().__init__(nome, idade, agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        self._saldo -= valor
        self._limite -= valor
        if self._saldo < 0:
            print("Saldo insuficiente!")
            self._saldo += valor
            self._limite += valor
            return
        if self._limite< 0:
            self._saldo += valor
            self._limite += valor
            print("Limite de saque diario alcançado!")
            return

        print(f"Removendo {valor} da conta!")


class Banco:
    def __init__(self):
        self.contas = {}
        self.client = ()
        self.clientPou = ()
        self.agencia = 0
        self.conta = 0
        self.auth = False
        self.authP = False
        self.contador = 1
        self.nc= ""


    def insContas(self, cc):
        cliente = input("Qual é o seu nome? ")
        idade = int(input("Qual é a sua idade? "))
        self.agencia = randint(1000,9999)
        self.conta = randint(10000, 99999)
        self.contas[f"Cliente{self.contador}"] =  {
                'nome': f"{cliente}",
                'agencia': f"{self.agencia}",
                'conta': f"{self.conta}",
                'saldo': 0,
                'idade':idade,
                'contaTipo': cc
            }
        print(f"Conta criada com sucesso!!!\nO numero da sua agencia é: {self.agencia} e o da sua conta é {self.conta}")
        self.contador+=1


    def autenticCor(self):
        Cliente = input("Insira o seu nome: ")
        idade = input("Qual é a sua idade? ")
        Conta = input("Insira a sua conta: ")
        Agencia = input("Insira a sua agencia: ")
        for bk, bv in self.contas.items():
            nv = bv["nome"]
            coAg = bv["agencia"]
            coCo = bv["conta"]
            tc = bv["contaTipo"]

            if Cliente == nv and Agencia == coAg and Conta == coCo and tc == "Corrente":
                self.auth = True
                print("Autenticado!!!")
                self.client = ContaCorrente(Cliente, idade, self.agencia, self.conta, 0)
                self.nc = bk
                return
        print("Não foi possivel autenticar!!!")


    def autenticPou(self):
        Cliente = input("Insira o seu nome: ")
        idade = input("Qual é a sua idade? ")
        Conta = input("Insira a sua conta: ")
        Agencia = input("Insira a sua agencia: ")
        for bk, bv in self.contas.items():
            nv = bv["nome"]
            coAg = bv["agencia"]
            coCo = bv["conta"]
            tc = bv["contaTipo"]

            if Cliente == nv and Agencia == coAg and Conta == coCo and  tc == 'Poupança':
                self.authP = True
                print("Autenticado!!!")
                self.clientPou = ContaPoupança(Cliente, idade, self.agencia, self.conta, 0)
                self.nc = bk
                return
        print("Não foi possivel autenticar!!!")



class Principal:
    def principal(self):
        b = Banco()
        continuar = 5
        while continuar != 0:
            escolha = int(input("O que deseja fazer: \n 1: Criar uma conta corrente\n 2: Autenticar a conta corrente\n 3: Depositar conta corrente\n"
                                " 4: Sacar conta corrente\n 5: Trocar de conta\n 6: Criar uma conta poupança \n 7: Autenticar a conta poupança"
                                " \n 8: Depositar conta poupança \n 9: Sacar conta poupança \n 0: Sair\n"))
            continuar = escolha
            if escolha == 1:
                print()
                cc="Corrente"
                b.insContas(cc)
                print()
            elif escolha == 2:
                print()
                b.autenticCor()
                print()

            elif escolha == 3 and b.auth == True:
                print()
                for bk, bv in b.contas.items():
                    if b.nc == bk:
                        valF = bv["saldo"]
                val = int(input("Quanto deseja depositar: "))
                b.client.depositar(val)
                valF += val
                for bk, bv in b.contas.items():
                    if b.nc == bk:
                        bv["saldo"] = valF
                valF=0
                print()

            elif escolha == 4 and b.auth == True:
                print()
                for bk, bv in b.contas.items():
                    if b.nc == bk:
                        valF = bv["saldo"]
                val = int(input("Quanto deseja sacar: "))
                b.client.sacar(val)
                if (valF - val) < 0:
                    print("")
                else:
                    valF -= val
                    for bk, bv in b.contas.items():
                        if b.nc == bk:
                            bv["saldo"] = valF
                valF = 0
                print()


            elif escolha == 5:
                b.auth = False

            elif escolha == 6:
                print()
                cc = "Poupança"
                b.insContas(cc)
                print()

            elif escolha==7:
                print()
                b.autenticPou()
                print()


            elif escolha == 8 and b.authP == True:
                print()
                for bk, bv in b.contas.items():
                    if b.nc == bk:
                        valF = bv["saldo"]

                val = int(input("Quanto deseja depositar: "))
                b.clientPou.depositar(val)
                valF += val

                for bk, bv in b.contas.items():
                    if b.nc == bk:
                        bv["saldo"] = valF

                valF = 0
                print()


            elif escolha == 9 and b.authP == True:
                print()
                limit = 500
                for bk, bv in b.contas.items():
                    if b.nc == bk:
                        valF = bv["saldo"]

                val = int(input("Quanto deseja sacar: "))
                b.clientPou.sacar(val)
                limit -= val
                if (valF - val) < 0:
                    print("")

                elif limit < 0:
                    limit += val

                else:
                    valF -= val
                    for bk, bv in b.contas.items():
                        if b.nc == bk:
                            bv["saldo"] = valF

                valF = 0
                print()

            elif escolha == 1002:
                print(b.contas)

            else:
                print("Comando invalido!!!")



p = Principal()
p.principal()

