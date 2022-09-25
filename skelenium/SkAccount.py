# ACCOUNT
# a simple class that handles log in information and the url that the account is associated with

class Account:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password
