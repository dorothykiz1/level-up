
# parent class to represent the Uber SignUp


class SignUp():
    pass

    def __init__(self, first_name, last_name, phone_number, password, promo_code):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

        self.password = password
        self.promo_code = promo_code

    def combined_name(self):
        name = self.first_name + ' ' + self.last_name
        return name

    @staticmethod
    def validate_email(email):
        return email

    def submit(self):
        pass
# sublass Rider


class Rider(SignUp):

    def __init__(self, city, rider_details):
        self.city = city
        self.rider_details = dict()

    def add(self, name, city):
        self.rider_details[name] = city


class Driver(SignUp):
    pass
