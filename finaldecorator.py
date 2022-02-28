def new_decorator(func):

    def wrap_func():
        print("code here before executing func")
        func()
        print("func called")
    
    return wrap_func
#@new_decorator
def func_needs_decorator():
    print("this function is in nedd of a decorator")
 
func_needs_decorator=new_decorator(func_needs_decorator)
#line 13 right see
#newdecorator ma func pass so in wrap func vitra passed func run
func_needs_decorator()
