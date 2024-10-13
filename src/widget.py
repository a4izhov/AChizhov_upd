from masks import get_mask_account, get_mask_card_number


def get_date(date: str) -> str:
    """Функция принимает строку с датой в формате 2024-03-11T02:26:18.671407 и возвращает в формате 11.03.2024"""
    updated_date = date[8:10] + "." + date[5:7] + "." + date[0:4]
    return updated_date

# print(get_date("2024-03-11T02:26:18.671407"))


def mask_account_card(account_info: str) -> str:
    """Функция принимает информацию о картах и счетах и маскирует их"""
    if account_info[-20].isdigit():
        mask_account_info = str(account_info[:-20] + get_mask_account(account_info))
    else:
        mask_account_info = str(account_info[:-16] + get_mask_card_number(account_info))
    return mask_account_info

# print(mask_account_card("Счет 73654108430135874305"))
# print(mask_account_card("MasterCard 7158300734726758"))
