class Human():
    sum3 = 0
    def __init__(self,name, age): # __init__两边均有双下划线在python中还是公有函数
        self.name = name
        self.age = age   
    def get_name(self):
        print(self.name)