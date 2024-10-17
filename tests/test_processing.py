from src.processing import filter_by_state, sort_by_date


def test_list_of_dicts_1() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_list_of_dicts_2() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_list_of_dicts_3() -> list:
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_list_of_dicts_4() -> list:
    return [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def test_filter_by_state():
    assert (filter_by_state(test_list_of_dicts_1()) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
    assert (filter_by_state(test_list_of_dicts_1(), 'CANCELED') ==
            [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
    assert filter_by_state(test_list_of_dicts_4()) == []


def test_sort_by_date_1():
    assert (sort_by_date(test_list_of_dicts_1(), True) ==
            [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
    assert (sort_by_date(test_list_of_dicts_1(), False) ==
            [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
             {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
             {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
    assert (sort_by_date(test_list_of_dicts_2(), False) ==
            [{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
             {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])
    assert sort_by_date([], False) == "Список пустой"
    assert sort_by_date(test_list_of_dicts_3(), False) == "Одна из дат указана в некорректном формате"
