plugins = {}


def go_to_plugins(func):
    plugins[func.__name__] = func
    return func


@go_to_plugins
def hello(args):
    print('Hello!',args)


@go_to_plugins
def gudbay(args):
    print('Пока',args)




print(plugins)

