from pydantic import BaseModel, field_validator
from typing import List
import re
from .property import PropertyOut


class ProducerBase(BaseModel):
    name: str
    cpf_cnpj: str

    @field_validator("cpf_cnpj")
    def validate_cpf_cnpj(cls, v: str) -> str:
        v = re.sub(r"\D", "", v)

        if len(v) == 11:
            if not cls.validate_cpf(v):
                raise ValueError("CPF inválido")
        elif len(v) == 14:
            if not cls.validate_cnpj(v):
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("CPF ou CNPJ deve ter 11 ou 14 dígitos")
        return v

    @staticmethod
    def validate_cpf(cpf: str) -> bool:
        if cpf == cpf[0] * 11:
            return False

        def calc_digit(cpf_part):
            s = sum(
                int(c) * f for c, f in zip(cpf_part, range(len(cpf_part) + 1, 1, -1))
            )
            d = 11 - s % 11
            return d if d < 10 else 0

        digit1 = calc_digit(cpf[:9])
        digit2 = calc_digit(cpf[:9] + str(digit1))
        return cpf[-2:] == f"{digit1}{digit2}"

    @staticmethod
    def validate_cnpj(cnpj: str) -> bool:
        if cnpj == cnpj[0] * 14:
            return False

        def calc_digit(cnpj_part):
            weights = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
            s = sum(int(c) * w for c, w in zip(cnpj_part, weights[-len(cnpj_part) :]))
            d = 11 - s % 11
            return d if d < 10 else 0

        digit1 = calc_digit(cnpj[:12])
        digit2 = calc_digit(cnpj[:12] + str(digit1))
        return cnpj[-2:] == f"{digit1}{digit2}"


class ProducerCreate(ProducerBase):
    pass


class ProducerOut(ProducerBase):
    id: int
    properties: List[PropertyOut] = []

    model_config = {"from_attributes": True}
