def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
            incorrect_data += 1
    return result


def calculate_average(numbers):
    try:
        num = personal_sum(numbers)
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None
    del_ = 0
    for i in numbers:
        if isinstance(i, (int, float)):
            del_ += 1
    try:
        avg = num / del_
    except ZeroDivisionError:
        return 0
    return avg


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
