def cache_decorator(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = hash((args, frozenset(kwargs.items())))

        if key in cache_dict:
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Викликана функція triangle_area з аргументами {a} та {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Викликана функція circle_area з аргументом {r}')
    return 3.14 * (r * r)


print('Результат виконання triangle_area(5, 10):', triangle_area(5, 10))
print('Результат виконання triangle_area(5, 10):', triangle_area(5, 10))
print('Результат виконання circle_area(20):', circle_area(20))
print('Результат виконання triangle_area(10, 10):', triangle_area(10, 10))
print('Результат виконання circle_area(20):', circle_area(20))
