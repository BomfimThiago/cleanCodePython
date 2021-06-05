def stop_some_logic():
    """Here we want some end logic
    for example, close connect to some database
    or close some service, in my case I will 
    just close a file
    """
    print('closing a file...')

def start_some_logic():
    """Here we want some initial logic
    for example, connect to some database
    or start some service, in my case I will 
    just open a file
    """
    print('opening a file...')

# A way to implement a context_manager inside my class
class MyHandler:
    """With a method enter and a method exit
    we can guarantee that something is always be called
    before and after any logic
    """
    def __enter__(self):
        start_some_logic()
        return self

    def __exit__(self, exc_type, ex_value, ex_traceback):
        stop_some_logic()



# The last code can be written using a python lib
# with a function
import contextlib

@contextlib.contextmanager
def other_handler():
    start_some_logic()
    yield
    stop_some_logic()


# Another way to do it is to this is using a decorator
class my_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        start_some_logic()

    def __exit__(self, exc_type, ex_value, ex_traceback):
        stop_some_logic()

# once the decorator is ready, we can use it to decorater a function
@my_decorator()
def another_handler_with_decorator():
    print('main logic')



if __name__ == "__main__":
    """Quando eu chamar os códigos acima, eles sempre 
    vão executar o método enter e o exit independente do resultado
    da minha lógica principal, dessa forma o print pra esse caso 
    será primeiro o 'opening a file' ,depois o 'main logic' e depois
    o 'closing a file'
    """
    with MyHandler():
        print('main logic')
    with other_handler():
        print('main logic')

    # Quando fazemos a opção do decorator não precisamos do with
    # só precisamos chamar a função
    another_handler_with_decorator()






