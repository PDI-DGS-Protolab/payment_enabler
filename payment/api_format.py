
""" Required data in order to define initial payment """
class UserData:

    tef_account = 0
    city        = ""
    address     = ""
    postal_code = ""
    country     = ""
    phone       = ""
    email       = ""

    def __init__(self, tef_account, city, address, postal_code, country, phone, email):
        self.tef_account = tef_account
        self.city        = city
        self.address     = address
        self.postal_code = postal_code
        self.country     = country
        self.phone       = phone
        self.email       = email

""" Data structure that models data regarding an order """
class OrderData:

    total           = 0
    currency        = ""
    recurrent_order = ""
    statement       = ""

    def __init__(self, total, currency, recurrent_order, statement):
        self.total           = total
        self.currency        = currency
        self.recurrent_order = recurrent_order
        self.statement       = statement
