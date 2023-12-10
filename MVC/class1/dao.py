from model import Pessoa


class PessoaDal:
    @classmethod
    def save(cls, person: Pessoa):
        with open('data.txt', 'a', encoding="utf-8") as f:
            f.write(person.Name + ' ' + person.Age + ' ' + person.CPF + '\n')

    @classmethod
    def save_raw_data(cls, person: Pessoa):
        data = {
            "Nome": person.Name,
            "Idade": person.Age,
            "CPF": person.CPF
        }
        Pessoa.raw_data.append(data)

    @staticmethod
    def return_raw_data():
        print(Pessoa.raw_data)
