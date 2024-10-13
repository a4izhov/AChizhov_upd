# Фича для личного кабинета клиента банка
## Описание

Конечная задача - разработать виджет, который показывает несколько последних успешных банковских операций клиента. 
Данный проект на бэкенде будет готовить данные для отображения в новом виджете.

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/a4izhov/AChizhov_upd.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Что реализовано:

1. Модуль masks
* Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX
* Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX"
2. Модуль widget
* Функция принимает строку с датой в формате 2024-03-11T02:26:18.671407 и возвращает в формате 11.03.2024
* Функция принимает информацию о картах и счетах и маскирует их
3. Модуль processing
* Функция принимает список словарей и опционально значение для ключа state.
    Возвращает новый список словарей, у которых ключ соответствует указанному значению
* Функция принимает список словарей и необязательный параметр сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате




## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).