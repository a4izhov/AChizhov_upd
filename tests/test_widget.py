import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize("x,expected", [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                                        ("Счет 73654108430135874305", "Счет **4305"),
                                        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                        ("", "Номер карты/счета должен состоять из 16/20 цифр"),
                                        ("12345", "Номер карты/счета должен состоять из 16/20 цифр")])
def test_mask_account_card(x: str, expected: str):
    assert mask_account_card(x) == expected


@pytest.mark.parametrize("x,expected", [("2024-03-11T02:26:18.671407", "11.03.2024"),
                                        ("", "Данные отсутствуют"),
                                        ("12345", "Некорректный формат данных")])
def test_get_date(x: str, expected: str):
    assert get_date(x) == expected
