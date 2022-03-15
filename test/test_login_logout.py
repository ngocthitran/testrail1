from basetest import *
from pages.LoginBase import LoginBase


class Test_login_logout(BaseTest):

    @pytest.mark.dependency(name="test_login")
    def test_login(self):
        login_page = LoginBase(self.driver, self.logger)
        login_page.login(self.credentials)
        assert True == login_page.is_logged(self.credentials)
