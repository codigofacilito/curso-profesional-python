def promedio(*args): # Tupla
    return sum(args) / len(args)


def usuarios(**kwargs): # Dict
    print(kwargs)
    print(type(kwargs))


def combinacion(p1, p2, *args, **kwargs, p5=500):
    print(args)
    print(kwargs)


combinacion(1, 2, 3, 4, 5, cody=True, curso='Python')