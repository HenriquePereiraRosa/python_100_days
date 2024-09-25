for number in range(1, 101):

    rest_by_3 = number % 3 == 0
    rest_by_5 = number % 5 == 0

    if rest_by_3 and rest_by_5:
        print("FizzBuzz")
    elif rest_by_5:
        print("Buzz")
    elif rest_by_3:
        print("Fizz")
    else:
        print(number)
