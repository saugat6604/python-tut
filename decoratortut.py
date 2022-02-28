


# s="Global variable"
# def func():
#     mylocal=10
#     #dictionary of local and global variables.
#     print(locals())
#     #print(globals())
#     print(globals()['s'])
# func()

def hello(name="Sanjay"):
    return "Brother"+name

print(hello())

mynewbro=hello  #func hello
print(mynewbro())