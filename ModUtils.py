import inspect


def getSource(func):
    return inspect.getsource(func).replace('\t', ' ')
