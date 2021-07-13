def fizz_buzz(start, stop):
    output = ""
    fizz = 3
    buzz = 5
    while start <= stop:
        if output:
            output += " " # noqa WPS336
        if start % (fizz * buzz) == 0:
            output += "FizzBuzz" # noqa WPS336
        elif start % fizz == 0:
            output += "Fizz" # noqa WPS336
        elif start % buzz == 0:
            output += "Buzz" # noqa WPS336
        else:
            output += str(start)
        start += 1
    return output
