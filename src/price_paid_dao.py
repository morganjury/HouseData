import pandas

column_names = ["ID","Price_Paid","Date","Postcode","Property_Type","Is_New","Duration","Number_Name","Flat_Num","Street","Locality","City","District","County","PPD_Type","Status"]

class PricePaidDao:
    
    def __init__(self, connection):
        self.conn = connection
        self.cursor = connection.cursor()
    
    def insert(self):
        print("INSERT")
        
    def get(self, id):
        print("GET")