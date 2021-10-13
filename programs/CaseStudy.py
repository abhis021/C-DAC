class customer:
    def __init__(self,custID, custNAME):
        self.custID = custID
        self.custName = custNAME


    def Display_details(self,):
        print(self.custID+" "+ self.custNAME)    
    def CalculateAmount(interest, year):
        pass
class RegCust(customer):
    def __init__(self,custID, custNAME, Amount, custType):
        self.custID = custID
        self.custName = custNAME
        self.custType = custType
        self.amount = Amount

    def CalculateAmount(self,principal):
        self.p = principal
        self.r = 3.5
        self.t = 3

        interest = (self.p*self.r*self.t)/100
        print("Regular Customer Interest: ",interest)

class PrivCust(customer):
    def __init__(self,custID, custNAME, Amount, custType):
        self.custID = custID
        self.custName = custNAME
        self.custType = custType
        self.Amount = Amount
    def CalculateAmount(self,principal):
        self.p = principal
        self.r = 3.5
        self.t = 3

        interest = (self.p*self.r*self.t)/100
        # print(interest)
        privamt = interest - 200
        print("Privileged Customer Interest Amount: ",privamt)

regularcustomer = RegCust(12312, "Raju", 100, "Regularcustomer")
privileger = PrivCust(9999," Honey", 100, "Privilegedcustomer")

regularcustomer.CalculateAmount(100)
privileger.CalculateAmount(100)