class Pessoa: 

    raw_data = None

    def __init__(self, nome:str, idade:int):
        self.legs = None
        self.Nome = nome
        self.Idade = idade
        
    def get_data(self):
        data = {
            "nome":self.Nome,
            "idade":self.Idade
        }
        Pessoa.raw_data.append(data)

    def getdatasdict(self):
        return self.raw_data
    
    def showdata(self):
        return f"{self.getdatasdict()} está funcionando"
    
    @classmethod
    def walk(cls,speed):
        return f'walking down the road at {speed} kmp/h'
    
    def person(cls):
        cls.legs = 2
        return None
    
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, altura:float):
        super().__init__(
            nome, 
            idade,
            altura
        )
    
def main():
    while True:
        nome = input("Digite o nome da Pessoa: ")
        idade = input("Digite a idade da Pessoa: ")
        
        # Checking for a condition to break the loop
        if (nome.lower() == "pedro" or idade.lower() == "pedro"):
            print("Encerrando...")
            break

        pessoa = Pessoa(nome=nome, idade=int(idade))  # Creating an instance of Pessoa
        pessoa.get_data()
        pessoa = Cliente()
        
    print(pessoa.showdata())
    print(Pessoa.walk(62))
        
if __name__ == "__main__":
    main()