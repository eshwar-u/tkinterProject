'''
This class is a subclass of User, and
represents an Employer
Author: Eshwar Umarengan
Date: 12/7/2023
'''
from User import User


class Employer(User):
    def __init__(self, username, password):
        super().__init__(username, password)