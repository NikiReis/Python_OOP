from controller import PessoaController
from dao import PessoaDal


while True:
    choose = int(input("\nType 1 to register a person\n"
                       "2 to see a saved register\n"
                       "and 0 to end the application: "))
    if choose == 0:
        break
    if choose == 2:
        PessoaDal.return_raw_data()

    if choose == 1:
        nome = input("Type the name: ")
        age = input("Type the age: ")
        cpf = input("Type the cpf: ")
        PessoaController.register(nome, str(age), cpf)
