[Back](../README.md)

## Scrabble

Реализуйте функцию-предикат `scrabble`, которая принимает на вход два параметра:
набор символов (строку) и слово, и проверяет, можно ли из переданного набора
составить это слово. В результате вызова функция возвращает `True` или `False`.

При проверке учитывается количество символов, которые нужны для составления
слова, и не учитывается их регистр.

Для решения используйте встроенный инструмент —
[Counter](https://docs.python.org/3/library/collections.html#collections.Counter).

### Пример

```python
>>> scrabble('rkqodlw', 'world')
True
>>> scrabble('avj', 'java')
False
>>> scrabble('avjafff', 'java')
True
>>> scrabble('', 'hexlet')
False
>>> scrabble('scriptingjava', 'JavaScript')
True
```
