class employer:
    __name = None
    __age = None
    __zp = None

    def __name__(self,name):
        self.__name = name
    def __age__(self, age):
        self.age = age
    def __zp__(self,zp):
        self.zp = zp

    def show(self):
        return self.__name
        return self.__age
        return self.__zp
e = employer('john', '18', '29809')
print(employer.show(e)) 