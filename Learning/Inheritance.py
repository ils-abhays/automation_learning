from Learning.Oops import Calculator


class ChildImpl(Calculator): #Stntax -> class childcalss(parent class) (accuring all the properties of parent class in child class)
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())