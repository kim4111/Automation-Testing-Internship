# This is a list of all of the Test accounts that we can use for our auto testing
# The main class contains the account's username, password and where it should log in

from System_Tests.common import MPGlobals as Gbs


class TestAccount:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url


# USE THIS ACCOUNT 99% OF THE TIME
main_account = TestAccount("pos@qsrdemo21.com", "Quantic21#", Gbs.portal_base_url)

# temp account for parent child (will delete when no longer using)
parent_child_account = TestAccount("10010765", "0YfmTKud", "https://myquantic.com")
pc_child_1_account = TestAccount("10010766", "Pb8BHrYO", "https://myquantic.com")
pc_child_2_account = TestAccount("10010767", "1MR7oadr", "https://myquantic.com")
pc_child_3_account = TestAccount("10010768", "ZjgInbJS", "https://myquantic.com")