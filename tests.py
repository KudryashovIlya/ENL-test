import unittest
from src.pages.base import MainPage
from conf import EMAIL_BCK
from src.helpers import get_random_int, get_random_email, get_random_str


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.page = MainPage()

    def tearDown(self):
        self.page.close()

    def test_login(self):
        """
        Simple positive case
        """
        self.page.open()
        self.page.login(flag=1)

        self.assertEqual(self.page.get_url(), 'https://www.optibet.com/?authShown=true', 'Cannot login!')

    def test_empty_form_login(self):
        """
        Check case when click login button without any values
        """
        self.page.open()
        self.page.login(
            user='',
            password=''
        )

        self.assertEqual(self.page.get_error()[0].text, 'Email is required', 'No error message about email')
        self.assertEqual(self.page.get_error()[1].text, 'Password is required',
                         'No error message about incorrect password')

    def test_valid_username(self):
        """
        Check case when user dosn't exist
        """
        self.page.open()
        self.page.login(
            user='test@test.com',
            password='password'
        )

        self.assertEqual('The username or password is incorrect',
                         self.page.get_error()[0].text, 'Incorrect behavior with unexist user')

    def test_invalid_username(self):
        """
        It seems, that some JS script validate all values that inputs to email form.
        So, we have 2 according equivalence classes:
        1: correct form [a-zA-Z0-9_]*@[a-z0-9].[a-z]^2
        2: incorrect form: any symbols in any sequency without @, also @[0-9a-z]*\

        Checking invalid value in email form
        """
        self.page.open()
        self.page.login(
            user='test'
        )
        self.assertEqual('Please enter a valid email', self.page.get_error()[0].text, 'No error message')

    def test_invalid_username_number(self):
        """
        Check digital in invalid form for email
        """
        self.page.open()
        self.page.login(
            user=get_random_int(8)
        )

        self.assertEqual('Please enter a valid email', self.page.get_error()[0].text, 'No error message')

    def test_invalid_username_big_number(self):
        """
        Check max length email
        """
        self.page.open()
        self.page.login(
            user=get_random_int(254)
        )

        self.assertEqual('Please enter a valid email', self.page.get_error()[0].text,
                         'Exceeded maximum line length')

    def test_big_email(self):
        """
        Check big random email
        """
        self.page.open()
        self.page.login(
            user=get_random_email(126)
        )

        self.assertEqual('Please enter a valid email', self.page.get_error()[0].text,
                         'Exceeded maximum line length')

    def test_blocked_email(self):
        """
        Try to login as user with blocked account
        """
        self.page.open()
        self.page.login(
            user=EMAIL_BCK
        )

        self.assertEqual('Your account has been blocked, please contact support for more info',
                         self.page.get_error()[0].text,
                         'Account did not block')


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.page = MainPage()

    def tearDown(self):
        self.page.close()

    def test_check_search(self):
        """
        True positive test case
        """
        self.page.open()
        self.page.search(category='Casino', game_name='Mega')

        result = self.page.get_result().text
        self.assertEqual('Search result - 62', result, 'Count of game is not equal')

    def test_check_search_and_launch(self):
        """
        Search and launch game
        """
        self.page.open()
        self.page.search(category='Casino', game_name='Book of Dead')

        result = self.page.get_result().text
        self.assertEqual('Search result - 1', result, 'Count of game is not equal')

        self.page.launch()

        self.assertEqual(self.page.get_url(), 'https://www.optibet.com/casino/games/playngo-310/playing',
                         'Game does not launch')


if __name__ == '__main__':
    unittest.main()
