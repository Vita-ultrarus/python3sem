def swap(function_to_decorate):
    def the_wrapper_around_the_original_function(a,b,show):
        function_to_decorate(b,a,show)
        return
    return the_wrapper_around_the_original_function

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res
div(2, 4, show=True)
