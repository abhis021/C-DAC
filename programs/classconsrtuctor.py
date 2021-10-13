class partyanimal:
    x=0
    name=' '
    def __init__(self,name1):
        self.name=name1
    def party(self):
        self.x=self.x+1
        print(self.name,'party count',self.x)
an=partyanimal('sally')
an.party()

na=partyanimal('jim')
na.party()
na.party()
