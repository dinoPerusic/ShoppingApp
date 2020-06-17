'Customer class'
class Customer:
    'Customer data'
    def __init__(self, customer_id=1, name="name1", last_name="lastname1", username="username1", password="password1"):

        self.customer_id = customer_id
        self.name = name
        self.last_name = last_name
        self.username = username
        self.password = password
