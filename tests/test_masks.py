import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("x,expected", [(1111222233334444, "1111 22** **** 4444"),
                                        (0000000000000000, "Номер карты отсутствует"),
                                        (12345, "Номер карты должен состоять из 16 цифр"),
                                        (11111111111111111111111, "Номер карты должен состоять из 16 цифр"),
                                        ("", "Номер карты отсутствует")])
def test_get_mask_card_number(x: str, expected: str):
    assert get_mask_card_number(x) == expected


@pytest.mark.parametrize("x,expected", [(11112222333344445555, "**5555"),
                                        (0000000000000000, "Номер счета отсутствует"),
                                        (12345, "Номер карты должен состоять из 20 цифр"),
                                        (11111111111111111111111, "Номер карты должен состоять из 20 цифр"),
                                        ("", "Номер счета отсутствует")])
def test_get_mask_account(x: str, expected: str):
    assert get_mask_account(x) == expected
