class BinomialSequence:
    """Класс для генерации строк треугольника Паскаля."""
    
    @staticmethod
    def generate(n):
        """Генерирует n-ю строку треугольника Паскаля (C(n,0) до C(n,n))."""
        coefficient = 1  # C(n,0) = 1
        
        for k in range(n + 1):
            yield coefficient
            # Вычисляем следующий коэффициент по формуле:
            # C(n, k+1) = C(n, k) * (n - k) // (k + 1)
            coefficient = coefficient * (n - k) // (k + 1)

# Проверка работы
print("Треугольник Паскаля (первые 6 строк):")
for n in range(6):
    print(f"n={n}: {list(BinomialSequence.generate(n))}")

print("\nСтрока n=10 (первые 5 коэффициентов):")
gen = BinomialSequence.generate(10)
for i in range(5):
    print(f"C(10,{i}) = {next(gen)}")