def outer_function(a, b):
    """The outer functions calls the inner 
    function and returns the sum of a and b"""
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
# Hover over outer_function and see the docstring.
result = outer_function(5, 10)
print(result)