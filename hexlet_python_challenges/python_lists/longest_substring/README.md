[Back](../README.md)

## The longest substring

Реализуйте функцию `find_longest_length()`, принимающую на вход строку
и возвращающую длину максимальной последовательности из неповторяющихся
символов. Подстрока может состоять из одного символа. Например в строке
`qweqrty`, можно выделить следующие подстроки: `qwe`, `weqrty`. Самой длинной
будет `weqrty`, а её длина — 6 символов.

```python
>>> find_longest_length('abcdeef')
5
>>> find_longest_length('jabjcdel')
7
```
