from typing import Iterable


def my_all(lst):
    # Все способы которые я увидел
    # Добавил проверку с помощью isinstance снова он
    if not isinstance(lst, Iterable):
        raise TypeError(f"Объект типа {type(lst).__name__} не является итерируемым")
    # Добавил проверку на возможность создания итератора
    try:    
        iterator = iter(lst)
    except TypeError:
        raise TypeError(f"Невозможно создать итератор для {type(lst).__name__}")
    # Проверка с помощью for 
    for element in lst:
        if not isinstance(element, (int, float)):
            return False
    return True

def main():
 
    input_str = input("Введите элементы через пробел : ")
    elements = input_str.split()
    
    lst = []
    for item in elements:
        try:
            lst.append(int(item))
        except ValueError:
            try:
                lst.append(float(item))
            except ValueError:
                lst.append(item)
    
    print(f"\nСоздан список: {lst}")
    
    # 1. Проверка положительных чисел с помощью any Функция any() в Python работает, проверяя, истинен ли хотя бы один элемент итерируемого объекта.
    has_positive = any(isinstance(x, (int, float)) and x > 0 for x in lst)
    print(f"1. Есть ли положительные числа? {'Да' if has_positive else 'Нет'}")
    
    # 2. Проверка всех элементов на числа с помощью my_all Функция all() в Python проверяет, истинны ли все элементы итерируемого объекта
    all_are_numbers = my_all(lst)
    print(f"2. Все элементы - числа? {'Да' if all_are_numbers else 'Нет'}")
    
    # 3. Сортировка с помощью sorted
    sorted_lst = sorted(lst)
    print(f"3. Отсортированный список: {sorted_lst}")



if __name__ == "__main__":
    main()