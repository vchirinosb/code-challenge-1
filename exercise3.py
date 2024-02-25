"""
Having the class `Caller` and the function `fn`
Refactor the function `fn` to execute any method from `Caller` using the
argument `fn_to_call` reducing the `fn` function to only one line.
"""


class Caller:

    """Provide results to arithmetical operations."""

    add = lambda a, b: a + b
    concat = lambda a, b: f'{a},{b}'
    divide = lambda a, b: a / b
    multiply = lambda a, b: a * b


def fn(fn_to_call, *args):
    """
    Get result from a specific method from Caller class.

    :param fn_to_call: str, method to call.

    :return: result of the called method.
    """
    return getattr(Caller, fn_to_call)(*args)


if __name__ == '__main__':
    """Test scenarios."""
    assert fn('add', 2, 3) == 5
    assert fn('concat', 'Jon', 'Doe') == 'Jon,Doe'
    assert fn('divide', 8, 4) == 2
    assert fn('multiply', 2, 3) == 6

    try:
        assert fn('sqrt', 2, 3) == 8
    except AttributeError:
        print('Method not supported')
