from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX"""
    card_number_str = str(card_number)
    mask_card_number = card_number_str[-16:-12] + " " + card_number_str[-15:-13] + "** **** " + card_number_str[-4:]
    return mask_card_number

# print(get_mask_card_number(1111222233334444))


def get_mask_account(account_number: Union[str, int]) -> str:
    """Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"""
    account_number_str = str(account_number)
    mask_account_number = "**" + account_number_str[-4:]
    return mask_account_number

# print(get_mask_account(1111222233334444))
