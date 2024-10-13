def filter_by_state(list_of_dicts: list, state: str = 'EXECUTED') -> list:
    """Функция принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, у которых ключ соответствует указанному значению"""
    updated_list_of_dicts = []
    for item in list_of_dicts:
        if item['state'] == state:
            updated_list_of_dicts.append(item)
    return updated_list_of_dicts


# print(filter_by_state([
# {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))


def sort_by_date(list_of_dicts: list, sort_direction: bool = False) -> list:
    """Функция принимает список словарей и необязательный параметр сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате"""
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda item: item["date"], reverse=sort_direction)
    return sorted_list_of_dicts


# print(sort_by_date([
# {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
# {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
# {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
# {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
