import collections
import inspect


def this_is_a_function(**kwargs):
    for key, value in kwargs.items():
        pass

def this_function_has_two_arguments(first_arg, second_arg):
    pass
    
print(inspect.signature(this_function_has_two_arguments))