#special method

class Book():

    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

    #special method
    #string represenataion of objject
    def __str__(self):
        #return "hello"
        return "Title:{},Author:{},Pages:{}".format(self.title,self.author,self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is deleted")

b=Book("java","Mr.SP",256)
print(b)
#when we call print function on object it looks for string represenattion
#no string rep then <__main__.Book object at 0x7f5e5d136978>
print(len(b))
#no len method so created len method and called that 
book=Book("python","np",100)
del book