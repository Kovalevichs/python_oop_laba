class Employer:
    def __init__(self,name,zp):
		    self.name = name
		    self.zp = zp
    def show(self):
        return self.name + ' ' + str(self.zp)
    def proz(self):
        return ((float(self.zp) * 0.1) + float(self.zp))
    
e = Employer('sofa', 20000)
print(Employer.show(e))
print(Employer.proz(e))