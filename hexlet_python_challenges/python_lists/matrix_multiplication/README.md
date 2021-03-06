[Back](../README.md)

## Matrix multiplication

Операция умножения двух матриц А и В представляет собой вычисление
результирующей матрицы С, где каждый элемент C(ij) равен сумме произведений
элементов в соответствующей строке первой матрицы A(ik) и элементов
в столбце второй матрицы B(kj).

Две матрицы можно перемножать только в том случае, если количество столбцов
в первой матрице совпадает с количеством строк во второй матрице. Это значит,
что первая матрица обязательно должна быть согласованной со второй матрицей.
В результате операции умножения матрицы размера M×N на матрицу размером N×K
является матрица размером M×K.

Реализуйте функцию `multiply()`, которая принимает две матрицы и возвращает
новую матрицу — результат их произведения.

```python
>>> from solution import multiply
>>> A = [[1, 2], [3, 2]]
>>> B = [[3, 2], [1, 1]]
>>> multiply(A, B)
[[5, 4], [11, 8]]
>>>
>>> C = [
...   [2, 5],
...   [6, 7],
...   [1, 8],
... ]
>>> D = [
...   [1, 2, 1],
...   [0, 1, 0],
... ]
>>> multiply(C, D)
[[2, 9, 2], [6, 19, 6], [1, 10, 1]]
>>>
```

### Подсказки
- Описание [алгоритма](https://www.math10.com/ru/vysshaya-matematika/matrix/umnozhenie-matric.html) перемножения матриц.
- [Демонстрация](http://matrixmultiplication.xyz/) операции перемножения матриц.
