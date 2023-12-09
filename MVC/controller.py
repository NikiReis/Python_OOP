import re

from dao import PessoaDal
from model import Pessoa


class ExceptionVerify(Exception):
    def __init__(self, error: str):
        self.Error = error
        super().__init__(
            self.Error
        )


def verify_name(text: str) -> str:
    message = ("Sorry but apparently there's somethings wrong\n"
               f"with your name. You name can't be numbers or be haven't\n"
               f"less than 2 characters. You've typed: {text}"
               )

    if isinstance(text, str) and len(text) > 2 or (not text.isalnum()):
        return text
    else:
        raise ExceptionVerify(message)


def verify_cpf(text: str):
    message = ("Sorry but apparently there's somethings wrong\n"
               f"with your cpf. Your CPF needs to have at least"
               f"nine digits and can't have dots or letters."
               f"You've typed: {text}"
               )

    text = re.sub("[^\d]", "", text)

    if 9 <= len(text) < 11:
        text = text.zfill(11)
        return text
    else:
        raise ExceptionVerify(message)


class PessoaController:
    @classmethod
    def register(cls, name, age, cpf):
        try:
            cpf = verify_cpf(cpf)
            name = verify_name(name)
            PessoaDal.save(Pessoa(name, age, cpf))
            PessoaDal.save_raw_data(Pessoa(name, age, cpf))
            return True
        except ExceptionVerify as e:
            raise e
