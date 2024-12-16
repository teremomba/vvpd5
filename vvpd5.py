"""Практическая ВВПД 5"""
ITERATIONS = 100

def maclaurin_ln1(x: float) -> float:
    """
    Вычисляет значение ln(1-x) с помощью ряда Маклорена.

    Аргументы:
        x (float): Значение переменной x. Граничные значения: -1 < x <= 1.

    Возвращаемое значение:
        float: Приближённое значение ln(1-x).

    Пример использования:
        >>> maclaurin_ln1(0.5)
        -0.6931471805599451
    """
    if not (-1 < x <= 1):
        raise ValueError("x должен быть в пределах -1 < x <= 1")

    result = 0.0
    for n in range(1, ITERATIONS + 1):
        result -= (x ** n) / n
    return result

def maclaurin_arctg(x: float) -> float:
    """
    Вычисляет значение arctg(x) с помощью ряда Маклорена.

    Аргументы:
        x (float): Значение переменной x. Граничные значения: -1 <= x <= 1.

    Возвращаемое значение:
        float: Приближённое значение arctg(x).

    Пример использования:
        >>> maclaurin_arctg(0.5)
        0.46364760900080587
    """
    if not (-1 <= x <= 1):
        raise ValueError("x должен быть в пределах -1 <= x <= 1")

    result = 0.0
    for n in range(ITERATIONS):
        result += ((-1) ** n * (x ** (2 * n + 1))) / (2 * n + 1)
    return result


def maclaurin_1(x: float, m: float) -> float:
    """
    Вычисляет значение (1-x)^m с помощью ряда Маклорена.

    Аргументы:
        x (float): Значение переменной x. Граничные значения: -1 < x < 1.
        m (float): Показатель степени m.

    Возвращаемое значение:
        float: Приближённое значение (1-x)^m.

    Исключения:
        ValueError: Если x находится вне допустимого диапазона.

    Пример использования:
        >>> maclaurin_1(0.5, 2)
        0.25
    """
    if not (-1 < x < 1):
        raise ValueError("x должен быть в пределах -1 < x < 1")

    result = 1.0
    term = 1.0
    for n in range(1, ITERATIONS + 1):
        term *= (m - (n - 1)) * (-x) / n
        result += term
    return result

def user_menu():
    """
    Отображает меню для пользователя и позволяет выбрать функцию и ввести x.
    """
    while True:
        print("\nВыберите функцию для вычисления:")
        print("1. ln(1-x)")
        print("2. arctg(x)")
        print("3. (1-x)^m")
        print("4. Выход")

        choice = input("Введите номер функции (1-4): ")

        match choice:
            case '1':
                try:
                    x = float(input("Введите x (-1 < x <= 1): "))
                    print(f"Результат ln(1-x): {maclaurin_ln1(x)}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            case '2':
                try:
                    x = float(input("Введите x (-1 <= x <= 1): "))
                    print(f"Результат arctg(x): {maclaurin_arctg(x)}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            case '3':
                try:
                    x = float(input("Введите x (-1 < x < 1): "))
                    m = float(input("Введите m (показатель степени): "))
                    print(f"Результат (1-x)^m: {maclaurin_1(x, m)}")
                except ValueError as e:
                    print(f"Ошибка: {e}")
            case '4':
                print("Выход из программы.")
                break
            case _:
                print("Некорректный ввод. Попробуйте снова.")

user_menu()
