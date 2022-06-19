def identity_function(x):
    if type(x) == str:
        raise TypeError(x, "This is a string!")
    return x
