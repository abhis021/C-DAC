class Time:
    """    """
    def __str__(self):
        return '%.2d:%.2d:%.2d'%(self.hour,self.minute,self.second)
time=Time(9,34)
print(time)
