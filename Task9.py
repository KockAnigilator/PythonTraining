import random
from string import ascii_lowercase, ascii_uppercase

def password_generator(N=16):
    """Функция-генератор случайных паролей длиной N."""
    chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
    
    while True:
        # Генерируем пароль из N случайных символов
        password = ''.join(random.choice(chars) for _ in range(N))
        yield password

# Создаем генератор
gen = password_generator(N=16)

# Выводим первые 5 паролей
print("Первые 5 паролей:")
for i in range(5):
    print(f"{i+1}. {next(gen)}")