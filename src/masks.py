from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    if card_number != 0 and card_number != "":
        card_number_str = str(card_number)
        if len(card_number_str) == 16:
            mask_card_number = card_number_str[-16:-12] + " " + card_number_str[-12:-10] + "** **** " + card_number_str[-4:]
            return mask_card_number
        else:
            return "Номер карты должен состоять из 16 цифр"
    else:
        return "Номер карты отсутствует"


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"""
    if account_number != 0 and account_number != "":
        account_number_str = str(account_number)
        if len(account_number_str) == 20:
            mask_account_number = "**" + account_number_str[-4:]
            return mask_account_number
        else:
            return "Номер карты должен состоять из 20 цифр"
    else:
        return "Номер счета отсутствует"
