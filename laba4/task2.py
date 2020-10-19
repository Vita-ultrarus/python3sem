def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_function(a):
        m=function_to_decorate(a)
        if m==0:
            print('Нет(')
        if m>10:
            print('Очень много')
        return
    return the_wrapper_around_the_original_function

@my_shiny_new_decorator
def chet(a):
    k=0
    for i in a:
        i=int(i)
        if i%2==0:
            k+=1
    return(k)
a=[1,3,7]
chet(a)
