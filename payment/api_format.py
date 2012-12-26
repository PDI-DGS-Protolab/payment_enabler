class UserData:
    'Required data in order to define initial payment'

    tef_account = 0
    city        = ""
    address     = ""
    postal_code = ""
    country     = ""
    phone       = ""

    def __init__(self, tef_account, city, address, postal_code, country, phone):
        self.tef_account = tef_account
        self.city = city
        self.address = address
        self.postal_code = postal_code
        self.country = country
        self.phone = phone

