class customer:
    def __init__(custID, custNAME):
        def Display_details():
            print(custID+" "+ custNAME)
        @abstractmethod    
        def CalculateAmount(interest, year):
            return
class RegCust(customer):
    def __init__(custID, custNAME, Amount, custType):
        self.custID = custID
        self.custName = cust
        self.custType = custType
        self.amount = Amount

    def CalculateAmount(interest,year):
        interest.p = principal
        interest.r = rate
        interest.t = time

        interest = (p*r*t)/100
        print(interest)

class PrivCust(customer):
    def __init__(custID, custNAME, Amount, custType):
        self.custID = custID
        self.custName = cust
        self.custType = custType
        self.Amount = amount
    def CalculateAmount(interest,year):
        interest.p = principal
        interest.r = rate
        interest.t = time

        interest = (p*r*t)/100
        print(interest)
        privamt = interest - 200
        print(privamt)

regularcustomer = RegCust(12312, Raju Punjabi, 100, Regularcustomer)
privileger = PrivCust(9999, Honey Singh, 100, Privileged Customer)

regularcustomer.CalculateAmount
privileger.CalculateAmount