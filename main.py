def cache(func):
    cache_dict = {}

    def wrapper(*args, **kwargs):
        key = hash((args, frozenset(kwargs.items())))

        if key in cache_dict:
            print('Returning result from cache')
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper


@cache
def triangle_area(a, b):
    print('Calculating triangle area')
    return 0.5 * a * b


print(triangle_area(5, 10))
print(triangle_area(5, 10))
