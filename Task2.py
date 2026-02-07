def my_all(lst):
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
    
    # 1. Проверка положительных чисел с помощью any
    has_positive = any(isinstance(x, (int, float)) and x > 0 for x in lst)
    print(f"1. Есть ли положительные числа? {'Да' if has_positive else 'Нет'}")
    
    # 2. Проверка всех элементов на числа с помощью my_all
    all_are_numbers = my_all(lst)
    print(f"2. Все элементы - числа? {'Да' if all_are_numbers else 'Нет'}")
    
    # 3. Сортировка с помощью sorted
    sorted_lst = sorted(lst)
    print(f"3. Отсортированный список: {sorted_lst}")



if __name__ == "__main__":
    main()