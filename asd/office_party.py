class Employee:
    def __init__(self, fun, name):
        self.emp = []
        self.fun = fun
        self.name = name

        self.f = -1
        self.f_names = []

        self.g = -1
        self.g_names = []


def f(v):
    if v.f >= 0:
        return v.f, v.f_names

    x = v.fun
    x_names = []

    for vi in v.emp:
        vi_fun, vi_names = g(vi)

        x += vi_fun
        x_names.extend(vi_names)

    y, y_names = g(v)

    if x > y:
        v.f = x
        v.f_names = x_names
        v.f_names.append(v.name)  # w tym scenriuszu pracownik 'v' idzie na impreze
    else:
        v.f = y
        v.f_names = y_names  # w tym scenriuszu pracownik 'v' nie idzie na impreze

    return v.f, v.f_names


def g(v):
    if v.g >= 0:
        return v.g, v.g_names

    v.g = 0
    v.g_names = []

    for vi in v.emp:
        vi_fun, vi_names = f(vi)

        v.g += vi_fun
        v.g_names.append(vi_names)

    return v.g, v.g_names
