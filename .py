


class Main:
    def __init__(self, nome ,idade, saldo,valor):
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo
        self.__valor = valor
    @property
    def Nome(self):
        return self.__nome 
     
    @Nome.setter  
    def Nome(self,novo_Nome):
         self.__nome = novo_Nome

    @property     
    def Idade(self):
         return self.__idade
    
    @Idade.setter
    def Idade(self,nova_Idade):
         self.__idade = nova_Idade

    @property
    def Saldo(self):
         return self.__saldo
    @Saldo.setter
    def Saldo(self, novo_saldo):
         self.__saldo = novo_saldo
    @property  
    def Valor(self):
         return self.__valor
    @Valor.setter
    def Valor(self,novo_valor):
         self.__valor = novo_valor
    def sacar(self):
         if self.Saldo < self.Valor :
                print("Saldo insuficiente")
         else:
              self.Saldo -= self.Valor; 
              print(f"Saque realizado! Saldo atual: {self.Saldo}")
    def depositar(self):
         self.Saldo += self.Valor   
         print(f"Deposito realizado! Saldo atual: {self.Saldo}")       
main = Main("Herik",22,1000,250)


main.Nome ="Herik"
main.Idade = 22
main.Saldo = 1000
main.Valor = 2000

print(f"Nome:{main.Nome} | Idade: {main.Idade} | Saldo: {main.Saldo}  | Valor : {main.Valor}")
main.depositar()