from src.masks import get_mask_account, get_mask_card_number


def get_date(date: str) -> str:
    """Функция принимает строку с датой в формате 2024-03-11T02:26:18.671407 и возвращает в формате 11.03.2024"""
    if date == "":
        return "Данные отсутствуют"
    elif len(date) != 26:
        return "Некорректный формат данных"
    else:
        updated_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
        return updated_date


def mask_account_card(account_info: str) -> str:
    """Функция принимает информацию о картах и счетах и маскирует их"""
    if len(account_info) > 15:
        if account_info[-20].isdigit():
            mask_account_info = str(account_info[:-20] + get_mask_account((account_info[-20:-1]+account_info[-1])))
        else:
            mask_account_info = str(account_info[:-16] + get_mask_card_number((account_info[-16:-1]+account_info[-1])))
        return mask_account_info
    else:
        return "Номер карты/счета должен состоять из 16/20 цифр"
