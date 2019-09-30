def cache(func):
    data = {}
    def wrapper(*args, **kwargs):
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')

        return data
    return wrapper
@cache
def rectangle_area(length, width):
    a = length * width
    return a
a = rectangle_area(2, 3)
print(a)