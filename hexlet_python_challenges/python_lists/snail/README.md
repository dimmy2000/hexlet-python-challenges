[Back](../README.md)

## Snail

Матрицу можно представить в виде двумерного списка. Например, список
`[[1, 2, 3, 4], [5, 6, 7, 8]]` — это отображение матрицы:
```commandline
1 2 3 4
5 6 7 8
```
Реализуйте функцию `snail_path()`, которая принимает на вход матрицу
и возвращает список элементов матрицы по порядку следования от левого верхнего
элемента по часовой стрелке к внутреннему. Движение по матрице напоминает
улитку:

<p align="center">
<img src="https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjZkNWQ4NzZmNGZjOGRlMWJiN2I0YWYwMzllODRjNmQ4LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=682ed57beed2ad11d420a0678a67745066e71b2dc7d238f2d16792b9f474f451" alt="Путь улитки" width="256" height="256">
<img src="https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjYzODkyMDdhMzFmOGQ3NmY4YTNlNDUyMTUxN2M0MTI5LnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=b4fdf90a164491f651d6322c713b24e83893b112ed095a38c21d4471b5899ecf" alt="Snail path" width="256" height="256">
</p>

```python
>>> from solution import snail_path
>>> snail_path([[1, 2], [3, 4]])
[1, 2, 4, 3]
>>> snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]])
['b', 'c', 'a', 11, 0, 'foo', None, '3', True]
>>>
```
