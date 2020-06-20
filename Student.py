class Student:
    def __init__(self,FName, LName):
        self.FName= FName
        self.LName= LName
        
    def Greatme(self):
        print("Hello "  + self. FName + " " + self. LName)
    
    def GetFullNameinEthiopia(self):
        print("IN Ethiopia "  + self. FName + " " + self. LName)
    def GetFullNameinWestern(self):
        print("In Western "  + self. LName + ", " + self. FName)


s1=Student("Eshetu","Mulunah")
s1.GetFullNameinEthiopia()
s2=Student("Micheal","Jackson")
s2.GetFullNameinWestern()


#print(id(Nejat))
#print(id(Naaol))
