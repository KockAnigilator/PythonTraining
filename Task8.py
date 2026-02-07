class CyclicDictIterator:
        
    def __init__(self, data_dict):
        if not isinstance(data_dict, dict):
            raise TypeError("Ожидается словарь")
        
        self.data = data_dict
        self.keys = list(data_dict.keys())
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.keys:
            raise StopIteration("Словарь пуст")
        
        # Получаем текущий ключ и значение
        key = self.keys[self.index]
        value = self.data[key]
        
        # Переходим к следующему индексу циклически
        self.index = (self.index + 1) % len(self.keys)
        
        return key, value


# Простая проверка
if __name__ == "__main__":
    d = {'a': 1, 'b': 2, 'c': 3}
    iterator = CyclicDictIterator(d)
    
    print("Циклический обход словаря:")
    for i in range(10):
        key, value = next(iterator)
        print(f"{i+1}. {key}: {value}")