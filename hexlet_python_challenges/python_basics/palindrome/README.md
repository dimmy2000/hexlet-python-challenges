[Back](../README.md)

## Palindrome

*Палиндром* — слово или текст, одинаково читающиеся в обоих направлениях.
Примеры:

- "я",
- "радар",
- "асса",
- "ишак ищет у тещи каши"

Реализуйте функцию `is_palindrome()`, которая принимает на вход слово,
определяет является ли оно палиндромом и возвращает логическое значение.

```python
>>> from solution import is_palindrome
>>> is_palindrome('')  # пустая строка тоже считается палиндромом
True
>>> is_palindrome('radar')
True
>>> is_palindrome('a')
True
>>> is_palindrome('abs')
False
>>> is_palindrome('ишак ищет у тещи каши')
True
>>>
```
