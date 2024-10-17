from typing import Union


def filter_by_state(list_of_dicts: list, state: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, у которых ключ соответствует указанному значению"""
    updated_list_of_dicts = []
    for item in list_of_dicts:
        if item['state'] == state:
            updated_list_of_dicts.append(item)
    return updated_list_of_dicts


def sort_by_date(list_of_dicts: list, sort_direction: bool = True) -> Union[str, list]:
    """Функция принимает список словарей и необязательный параметр сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате"""

    if list_of_dicts != []:
        for item in list_of_dicts:

            if len(item["date"]) != 26:
                return "Одна из дат указана в некорректном формате"
            else:
                sorted_list_of_dicts = sorted(list_of_dicts, key=lambda item: item["date"], reverse=sort_direction)
        return sorted_list_of_dicts
    else:
        return "Список пустой"
